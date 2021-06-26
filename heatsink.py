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
    return render_template("heaters.html")


@app.route("/support", methods=["GET", "POST"])
def support():
    return render_template("support.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():

    # Retrieve controllers
    controllers = mongodb.db.controllers.find().sort("name", 1)
    delete_controllers = controllers

    # Retrieve heaters
    heaters = mongodb.db.heaters.find().sort("name", 1)
    delete_heaters = heaters

    # Retrieve controllers
    members = mongodb.db.members.find().sort("username", 1)
    delete_members = members

    return render_template(
        "settings.html",
        controllers=controllers,
        heaters=heaters,
        members=members)


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
        if check_password_hash(
            specified_user.password,
                password) and specified_user.is_admin == is_admin:
            flash("Member update successful!")
            session["admin"] = is_admin
        else:
            flash("Member update failed!")

    return render_template("settings.html")


@app.route("/actionController/", methods=["GET", "POST"])
def actionController():
    return render_template("settings.html")


@app.route("/actionHeater/", methods=["GET", "POST"])
def actionHeater():
    return render_template("settings.html")


@app.route("/actionGroup/", methods=["GET", "POST"])
def actionGroup():
    return render_template("settings.html")


@app.route("/actionItems/", methods=["GET", "POST"])
def actionItems():

    # Initialise parameters
    is_username = request.form.get("user")
    is_heater = request.form.get("heater")
    is_controller = request.form.get("controller")

    if is_username:

        # Find the member
        member_details = mongodb.db.members.find_one(is_username)

        # Remove the member
        mongodb.db.members.delete_one({"_id": ObjectId(member_details._id)})

    elif is_heater:

        # Find heater
        heater_details = mongodb.db.heaters.find_one(is_heater)

        # Remove heater
        mongodb.db.heaters.delete_one({"_id": ObjectId(heater_details._id)})

        # Remove associated member group
        for collection_name in mongodb.db.list_collection_names():
            if (heater_details.name + "_member") in collection_name:
                collection_to_drop = mongodb.db[collection_name]
                collection_to_drop.drop()

    elif is_controller:

        # Find controller
        controller_details = mongodb.db.controllers.find_one(is_controller)

        # Remove controller
        mongodb.db.heaters.delete_one({"_id": ObjectId(controller_details._id)})

    return render_template("settings.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
