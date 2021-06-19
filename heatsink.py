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
            if check_password_hash(
              is_member["password"], request.form.get("password)")):
                session["member"] = request.form.get("username").lower()
                if is_member["type"].lower() == "admin":
                    session["admin"] = True
                else:
                    session["admin"] = False
                return redirect(url_for("heaters.html", member=session[
                    "member"], admin=session["admin"]))
            else:
                flash("Invalid username and/or password!")
                return redirect(url_for("index"))
        else:
            # Incorrect username
            flash("Incorrect username and/or password!")
            return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/")
def logout():
    session.pop("member")
    session.pop("type")
    flash("You have been logged out...")
    return render_template("index.html")


@app.route("/heaters", methods=["GET", "POST"])
def heaters(member, admin):
    member = session["member"]
    admin = session["admin"]
    return render_template("heaters.html", member=member, admin=admin)


@app.route("/settings", methods=["GET", "POST"])
def settings(member, admin):
    member = session["member"]
    admin = session["admin"]
    return render_template("settings.html", member=member, admin=admin)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
