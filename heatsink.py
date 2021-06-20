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
            session["member"] = is_member["username"].lower()
            session["admin"] = is_member["is_admin"]
            return redirect(url_for(
                "heaters", member=session["member"], admin=session["admin"]))
        else:
            # Incorrect username
            flash("Incorrect username!")
            return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/")
def logout():
    session.pop("member", None)
    session.pop("admin", None)
    flash("You have been logged out...")
    return render_template("index.html")


@app.route("/heaters/<member>&<admin>", methods=["GET", "POST"])
def heaters(member, admin):

    # Initialise parameters
    member = session["member"]
    admin = session["admin"]
    return render_template("heaters.html", member=member, admin=admin)


@app.route("/settings/<member>&<admin>", methods=["GET", "POST"])
def settings(member, admin):
    member = session["member"]
    admin = session["admin"]
    return render_template("settings.html", member=member, admin=admin)


@app.route("/settings", methods=["GET", "POST"])
def updateMember():
    if request.method == "POST":

        # Initialise parameters
        updated_type = "admin" if request.form.get("is_admin") else "user"
        updated_password = generate_password_hash(request.form.get("password"))

        # Verify the member
        is_member = mongodb.db.members.find_one({"username": request.form.get("username").lower()})

        if is_member:

            # Intialise the parameters
            member = is_member["username"].lower()
            admin
            # Set the criteria
            which_member = { "username": is_member["username"].lower() }
            update_to = {
                "$set": {"password": updated_password, "type": updated_type}
            }

            # Update the document
            mongodb.db.members.update_one(which_member, update_to)

            # Check to see if it worked
            specified_user = mongodb.db.members.find_one(
                {"username": request.form.get("username").lower()})
            if check_password_hash(specified_user["password"], request.form.get(
                    "password")) and specified_user["type"] == updated_type:
                flash("Member update successful!")
                return redirect(url_for(
                    'settings', member=session.member, admin=session.admin))
            else:
                flash("Member updatefailed!")


    return render_template(
        "settings.html", member=session.member, admin=session.admin)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
