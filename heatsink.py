import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongodb = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        is_member = mongodb.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if is_member:
            # Check for the correct password
            if check_password_hash(is_member["password"], request.form.get(
                    "password")):
                session["member"] = is_member["username"].lower()
                session["admin"] = True if is_member["is_admin"] else False

                # Welcome the member
                flash("Hello, " + session["member"] + ". Welcome back!")

                return redirect(url_for("heaters"))

            else:
                flash("Invalid username and/or password!")
                return redirect(url_for("index"))

        else:
            # Incorrect username
            flash("Invalid username and/or password!")
            return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop("member", None)
    session.pop("admin", None)
    session.pop("my_heaters", None)
    session.pop("_flashes", None)
    return render_template("index.html")


@app.route("/heaters", methods=["GET", "POST"])
def heaters():

    # Initialise parameters
    populate_heaters = []

    # Enumerate the heaters
    heaters = list(mongodb.db.heaters.find().sort("name", 1))

    if heaters:
        for heater in heaters:

            # Capture the elements of the current heater
            current_heater = {
                "name": heater["name"].title(),
                "controller": heater["controller"].upper(),
                "relay": heater["relay"],
                "location": heater["location"].title(),
                "is_enabled": heater["is_enabled"],
                "is_on": heater["is_on"]
            }

            for collection_name in mongodb.db.list_collection_names():
                if (heater["name"] + "_member") in collection_name:
                    collection_specified = mongodb.db[collection_name]

                    # Check if member has access
                    has_access = collection_specified.find_one(
                        {"username": session["member"]})

                    if has_access:
                        populate_heaters.append(current_heater)

        session["my_heaters"] = populate_heaters

    else:
        flash("No heaters found!")
        return redirect(url_for("heaters"))

    return render_template("heaters.html")


@app.route("/heaterSwitch/<name>", methods=["GET", "POST"])
def heaterSwitch(name):

    # Simulate control of the heater
    heater = mongodb.db.heaters.find_one({"name": name.lower()})

    # Check if the heater is on
    new_status = False if heater["is_on"] else True

    # Set the criteria
    switch_values = {
        "name": heater["name"],
        "location": heater["location"],
        "controller": heater["controller"],
        "relay": int(heater["relay"]),
        "is_enabled": heater["is_enabled"],
        "is_on": new_status
    }

    # Update existing document
    mongodb.db.heaters.update(
        {"name": heater["name"]}, switch_values)

    return redirect(url_for("heaters"))


@app.route("/settings", methods=["GET", "POST"])
def settings():

    # Method POST button code provided by Andrew Clark(
    # https://stackoverflow.com/questions/66618070/
    # flask-differentiating-between-different-post-requests)
    # and adjusted for my requirements

    if request.method == "POST":

        # Process member actions
        if 'member-button' in request.form:

            # Initialise parameters
            is_member_update = True if request.form.get(
                "new_updated_member") else False
            username = request.form.get("member-username").lower()
            password = generate_password_hash(
                request.form.get("member-password"))
            is_admin = True if request.form.get("is_admin") else False
            verify_password = request.form.get("member-password")

            # Set the criteria
            member_values = {
                "username": username,
                "password": password,
                "is_admin": is_admin
            }

            # Update the member document
            if is_member_update:

                # Verify the member
                is_member = mongodb.db.members.find_one({"username": username})

                if is_member:
                    # Update existing document
                    mongodb.db.members.replace_one(
                        {"_id": ObjectId(is_member["_id"])}, member_values)
                else:
                    flash("Invalid member!")
                    return redirect(url_for("settings"))

            # Insert a new member document
            else:

                # Check to see if the controller exists
                member_exists = mongodb.db.controllers.find_one(
                    {"username": username})

                if member_exists:
                    flash("Specified member already exists!")
                    return redirect(url_for("settings"))
                else:
                    # insert new document
                    mongodb.db.members.insert_one(member_values)

            # Check to see if it worked

            specified_user = mongodb.db.members.find_one(
                {"username": username})

            if specified_user:
                if check_password_hash(specified_user[
                        "password"], verify_password) and specified_user[
                                "is_admin"] == is_admin:
                    flash("Member update/insert successful!")
                    session["admin"] = is_admin
                else:
                    flash("Member update/insert failed!")
                    return redirect(url_for("settings"))
            else:
                flash("Adding new member failed!")
                return redirect(url_for("settings"))

        # Process controller actions
        elif 'controller-button' in request.form:

            # Initialise parameters
            is_controller_update = True if request.form.get(
                "new_updated_controller") else False
            controller_name = request.form.get("controller-name").lower()
            controller_address = request.form.get("controller-address").lower()

            # Set the criteria
            controller_values = {
                "name": controller_name,
                "address": controller_address
            }

            if is_controller_update:

                # Verify the controller
                is_controller = mongodb.db.controllers.find_one(
                    {"name": controller_name})

                if is_controller:
                    # Update existing document
                    mongodb.db.controllers.replace_one(
                        {"_id": ObjectId(
                            is_controller["_id"])}, controller_values)
                else:
                    flash("Invalid controller!")
                    return redirect(url_for("settings"))

            else:

                # Check to see if the controller exists
                is_existing = mongodb.db.controllers.find_one(
                    {"name": controller_name})

                if is_existing:
                    flash("Specified controller exists!")
                    return redirect(url_for("settings"))
                else:
                    # insert new document
                    mongodb.db.controllers.insert_one(controller_values)

            # Check to see if it worked
            specified_controller = mongodb.db.controllers.find_one(
                {"name": controller_name})

            if specified_controller:
                if specified_controller["address"] == controller_address:
                    flash("Controller update/insert successful!")
                else:
                    flash("Controller update/insert failed!")
                    return redirect(url_for("settings"))
            else:
                flash("Adding new controller failed!")
                return redirect(url_for("settings"))

        # Process heater actions
        elif 'heater-button' in request.form:

            # Initialise parameters
            is_heater_update = True if request.form.get(
                "new_updated_heater") else False
            heater_name = request.form.get("heater-name").lower()
            heater_location = request.form.get("heater-location").lower()
            heater_controller = request.form.get("heater-controller").lower()
            heater_relay = request.form.get("heater-relay")
            is_enabled = True if request.form.get("is_enabled") else False
            is_on = True if request.form.get("is_on") else False

            # Set the criteria
            heater_values = {
                "name": heater_name,
                "location": heater_location,
                "controller": heater_controller,
                "relay": int(heater_relay),
                "is_enabled": is_enabled,
                "is_on": is_on
            }

            # Update the heater document
            if is_heater_update:
                # Verify the controller
                is_heater = mongodb.db.heaters.find_one({"name": heater_name})

                if is_heater:
                    # Update existing document
                    mongodb.db.heaters.replace_one(
                        {"_id": ObjectId(heater_name)}, heater_values)
                else:
                    flash("Invalid heater!")
                    return redirect(url_for("settings"))

            # Insert a new heater document
            else:
                # Check to see if the heater exists
                heater_exists = mongodb.db.heaters.find_one(
                    {"name": heater_name})

                if heater_exists:
                    flash("Specified heater exists!")
                    return redirect(url_for("settings"))
                else:
                    # insert new document
                    mongodb.db.heaters.insert_one(heater_values)

                    # Create the member group
                    new_collection_name = heater_name + "_members"
                    new_collection = mongodb.db[new_collection_name]
                    new_collection.insert_one({"username": session["member"]})

            # Check to see if it worked
            specified_heater = mongodb.db.heaters.find_one(
                {"name": heater_name})

            if specified_heater:
                if specified_heater == heater_values:
                    flash("Heater update/insert successful!")

                    # Check for the heater group
                    for collection_name in mongodb.db.list_collection_names():
                        if new_collection_name in collection_name:
                            flash("Heater group created!")

                else:
                    flash("Heater update/insert failed!")
                    return redirect(url_for("settings"))

            else:
                flash("Adding new heater failed!")
                return redirect(url_for("settings"))

        # Process heater group actions
        elif 'groups-button' in request.form:

            # Initialise parameters
            is_group_update = True if request.form.get(
                "add_remove_group") else False
            groups_heater = request.form.get("group-heater")
            groups_username = request.form.get("group-member")

            group_values = {
                "username": groups_username
            }

            # Enumerate the collection
            for collection_name in mongodb.db.list_collection_names():
                if (groups_heater + "_members") in collection_name:
                    collection_specified = mongodb.db[collection_name]

                    if is_group_update:
                        # Remove the member from the group
                        collection_specified.delete_one(group_values)
                    else:
                        # Add the member to the group
                        collection_specified.insert_one(group_values)

            # Check to see if it worked
            specified_group = collection_specified.find_one(
                {"username": groups_username})

            if specified_group:
                flash("Member added to group!")
            else:
                flash("Member removed from group!")

        # Process delete items actions
        elif 'items-button' in request.form:

            # Initialise parameters
            is_member_delete = True if request.form.get(
                "delete-members") else False
            delete_member = request.form.get("delete-member")
            is_heater_delete = True if request.form.get(
                "delete-heaters") else False
            delete_heater = request.form.get("delete-heater")
            is_controller_delete = True if request.form.get(
                "delete-controllers") else False
            delete_controller = request.form.get("delete-controller")

            # Delete member
            if is_member_delete:
                # Find member
                is_member = mongodb.db.members.find_one(
                    {"username": delete-member})

                # Remove member
                if is_member:
                    mongodb.db.members.remove_one(
                        {"_id": ObjectId(is_member["_id"])})
                    flash("Member deleted!")
                else:
                    flash("Invalid member!")
                    return redirect(url_for("settings"))

            # Delete heater
            elif is_heater_delete:
                # Find heater
                is_heater = mongodb.db.heaters.find_one(
                    {"name": delete_heater})

                # Remove heater
                if is_heater:
                    mongodb.db.heaters.remove_one(
                        {"_id": ObjectId(is_heater._id)})

                    # Remove associated member group
                    for collection_name in mongodb.db.list_collection_names():
                        if (is_heater["name"] + "_members") in collection_name:
                            collection_to_drop = mongodb.db[collection_name]
                            collection_to_drop.drop()
                    flash("Heater deleted!")

                else:
                    flash("Invalid heater name!")
                    return redirect(url_for("settings"))

            # Delete controller
            elif is_controller_delete:
                # Find controller
                is_controller = mongodb.db.controllers.find_one(
                    {"name": delete_controller})

                # Remove controller
                if is_controller:
                    mongodb.db.heaters.remove_one(
                        {"_id": ObjectId(is_controller._id)})
                    flash("Controller deleted!")
                else:
                    flash("Invalid controller name!")
                    return redirect(url_for("settings"))

    # Retrieve member
    members = mongodb.db.members.find().sort("username", 1)

    # Retrieve heaters
    heaters = mongodb.db.heaters.find().sort("name", 1)

    # Retrieve controller
    controllers = mongodb.db.controllers.find().sort("name", 1)

    return render_template(
        "settings.html",
        members=members,
        heaters=heaters,
        controllers=controllers)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
