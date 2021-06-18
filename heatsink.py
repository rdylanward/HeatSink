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
                session["type"] = is_member["type"].lower()
                return redirect(url_for("heaters.html"))
            else:
                flash("Invalid password!")
                return redirect(url_for("index"))
        else:
            # Incorrect username
            flash("Incorrect username!")
            return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/heaters", methods=["GET", "POST"])
def heaters(member, type):
    member = session["member"]
    type = session["type"]
    return render_template("heaters.html", member=member, type=type)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
