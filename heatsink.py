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
                if is_member["is_admin"]:
                    session["admin"] = True
                else:
                    session["admin"] = False

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
    flash("You have been logged out...")
    return render_template("index.html")


@app.route("/heaters", methods=["GET", "POST"])
def heaters():

    # Populate the heaters
    heaters = mongodb.db.heaters.find().sort("name", 1)

    if heaters:
        for heater in heaters:
            for collection_name in mongodb.db.list_collection_names():
                if (heater.name + "_member") in collection_name:
                    collection_specified = mongodb.db[collection_name]
                    collection_specified.insert_one({"username": session.member})

    return render_template("heaters.html")


@app.route("/support", methods=["GET", "POST"])
def support():
    return render_template("support.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():

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


@app.route("/actionMember/", methods=["GET", "POST"])
def actionMember():
    if request.method == "POST":
        # Initialise parameters
        is_update = True if request.form.get("new_updated_member") else False
        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))
        is_admin = True if request.form.get("is_admin") else False

        # Set the criteria
        value_dictionary = {
            "username": username,
            "password": password,
            "is_admin": is_admin
        }

        if is_update:
            # Verify the member
            is_member = mongodb.db.members.find_one({"username": username})

            # Update existing document
            mongodb.db.members.update(
                {"username": is_member.username}, value_dictionary)
        else:
            # insert new document
            mongodb.db.members.insert_one(value_dictionary)

        # Check to see if it worked
        specified_user = mongodb.db.members.find_one(
            {"username": username})
        if specified_user:
            if check_password_hash(
                specified_user.password,
                    password) and specified_user.is_admin == is_admin:
                flash("Member update successful!")
                session["admin"] = is_admin
            else:
                flash("Member update failed!")
                return redirect(url_for("settings"))
        else:
            flash("Adding new member failed!")
            return redirect(url_for("settings"))

    return render_template("settings.html")


@app.route("/actionController/", methods=["GET", "POST"])
def actionController():
    if request.method == "POST":
        # Initialise parameters
        is_update = True if request.form.get(
            "new_updated_controller") else False
        name = request.form.get("controller-name").lower()
        address = request.form.get("controller-address")

        # Set the criteria
        value_dictionary = {
            "name": name,
            "address": address
        }

        if is_update:
            # Verify the controller
            is_controller = mongodb.db.controllers.find_one({"name": name})

            if is_controller:
                # Update existing document
                mongodb.db.controllers.update(
                    {"_id": ObjectId(is_controller._id)}, value_dictionary)
            else:
                flash("Invalid controller name!")
                return redirect(url_for("settings"))

        else:
            # insert new document
            mongodb.db.controllers.insert_one(value_dictionary)

        # Check to see if it worked
        specified_controller = mongodb.db.controllers.find_one({"name": name})
        if specified_controller:
            if specified_controller.address == address:
                flash("Controller update successful!")
            else:
                flash("Controller update failed!")
                return redirect(url_for("settings"))
        else:
            flash("Adding new controller failed!")
            return redirect(url_for("settings"))

    return render_template("settings.html")


@app.route("/actionHeater/", methods=["GET", "POST"])
def actionHeater():
    if request.method == "POST":
        # Initialise parameters
        is_update = True if request.form.get("new_updated_heater") else False
        name = request.form.get("heater-name").lower()
        location = request.form.get("heater-location")
        controller = request.form.get("heater-controller")
        relay = request.form.get("heater-relay")
        is_enabled = True if request.form.get("is_enabled") else False
        is_on = True if request.form.get("is_on") else False

        # Set the criteria
        value_dictionary = {
            "name": name,
            "location": location,
            "controller": controller,
            "relay": int(relay),
            "is_enabled": is_enabled,
            "is_on": is_on
        }

        if is_update:
            # Verify the controller
            is_heater = mongodb.db.heaters.find_one({"name": name})

            if is_heater:
                # Update existing document
                mongodb.db.controllers.update(
                    {"_id": ObjectId(is_heater._id)}, value_dictionary)
            else:
                flash("Invalid heaters name!")
                return redirect(url_for("settings"))

        else:
            # insert new document
            mongodb.db.controllers.insert_one(value_dictionary)

            # Create the member group
            collection_name = name + "_member"
            mongodb.db.createCollection(collection_name)

        # Check to see if it worked
        specified_heater = mongodb.db.heaters.find_one({"name": name})
        if specified_heater:
            if specified_heater == value_dictionary:
                flash("Heater update successful!")
            else:
                flash("Heater update failed!")
                return redirect(url_for("settings"))
        else:
            flash("Adding new controller failed!")
            return redirect(url_for("settings"))

    return render_template("settings.html")


@app.route("/actionGroup/", methods=["GET", "POST"])
def actionGroup():

    # Initialise parameters
    heater = request.form.get("group-heater")
    username = request.form.get("group-member")

    # Add member to the heater
    for collection_name in mongodb.db.list_collection_names():
        if (heater + "_member") in collection_name:
            collection_specified = mongodb.db[collection_name]
            collection_specified.insert_one({"username": username})

    return render_template("settings.html")


@app.route("/actionItems/", methods=["GET", "POST"])
def actionItems():

    # Initialise parameters
    delete_member = request.form.get("delete-user")
    delete_heater = request.form.get("delete-heater")
    delete_controller = request.form.get("delete-controller")

    # Delete member
    if delete_member:
        # Find member
        is_member = mongodb.db.find_one({"username": delete_member})

        # Remove member
        if is_member:
            mongodb.db.delete_one({"_id": ObjectId(is_member._id)})
            flash("Member deleted!")
        else:
            flash("Invalid member!")
            return redirect(url_for("settings"))

    # Delete heater
    elif delete_heater:
        # Find heater
        is_heater = mongodb.db.heaters.find_one({"name": delete_heater})

        # Remove heater
        if is_heater:
            mongodb.db.heaters.delete_one({"_id": ObjectId(is_heater._id)})

            # Remove associated member group
            for collection_name in mongodb.db.list_collection_names():
                if (is_heater.name + "_member") in collection_name:
                    collection_to_drop = mongodb.db[collection_name]
                    collection_to_drop.drop()
            flash("Heater deleted!")
        else:
            flash("Invalid heater name!")
            return redirect(url_for("settings"))

    # Delete controller
    elif delete_controller:
        # Find controller
        is_controller = mongodb.db.controllers.find_one(
            {"name": delete_controller})

        # Remove controller
        if is_controller:
            mongodb.db.heaters.delete_one({"_id": ObjectId(is_controller._id)})
            flash("Controller deleted!")
        else:
            flash("Invalid controller name!")
            return redirect(url_for("settings"))

    return render_template("settings.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
