import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = "mongodb+srv://daudi:dAUdi@myprojectdb.jh9w6.mongodb.net/personal_portfolio?retryWrites=true&w=majority"
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_fields")
def get_fields():
    fields = mongo.db.fields.find()
    return render_template("fields.html", fields=fields)


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        flash("You must be logged out to register!")
        return redirect(url_for("my_contact"))
    if request.method == "POST":
        # Checking if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
        return redirect(url_for("my_contact"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking usernane if already exits in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):  # noqa
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("my_contact"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

                # username doesn't exits
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You were logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/contact_detail/<string:id>")
def contact_detail(id):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        contact = mongo.db.contacts.find_one({
            "created_by": user["_id"],
            "_id": ObjectId(id)
        })
        if contact:
            return render_template("contact_detail.html", contact=contact)
        flash("You have to own the contact in order to open it!")
        return redirect(url_for("my_contact"))
    flash("You have to be loggedin in order to see the contact")
    return redirect(url_for("login"))


@app.route("/add_contact", methods=["GET", "POST"])
def add_contact():
    if session["user"]:
        user = mongo.db.users.find_one({
            "username": session["user"]
        })
        if request.method == "POST":
            field = {
                        "contact_name": request.form.get("contact_name"),
                        "industry_name": request.form.get("industry_name"),
                        "email_name": request.form.get("email_name"),
                        "person_detail": request.form.get("person_detail"),
                        "is_helpful": request.form.get("is_helpful"),
                        "created_on": datetime.today().strftime('%Y-%m-%d'),
                        "created_by": user["_id"]
                }
            mongo.db.contacts.insert_one(field)
            flash("Contact Successfully Added")
            return redirect(url_for("my_contact"))

        fields = mongo.db.fields.find().sort("field_name", 1)
        return render_template("add_contact.html", industrys=fields)
    flash("You must be logged to add a contact")
    return redirect(url_for("login"))


@app.route("/edit_contact/<string:id>", methods=["GET", "POST"])
def edit_contact(id):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        contact = mongo.db.contacts.find_one({
            "created_by": user["_id"],
            "_id": ObjectId(id)
        })
        if contact:
            if request.method == "POST":
                field = {
                        "contact_name": request.form.get("contact_name"),
                        "industry_name": request.form.get("industry_name"),
                        "email_name": request.form.get("email_name"),
                        "person_detail": request.form.get("person_detail"),
                        "is_helpful": request.form.get("is_helpful"),
                        "updated_on": datetime.today().strftime('%Y-%m-%d'),
                        "created_on": contact['created_on'],
                        "created_by": contact['created_by']
                    }
                mongo.db.contacts.update({"_id": ObjectId(contact["_id"])},
                                         field)
                flash("Contacts Successfully Updated")
                return redirect(url_for("contact_detail", id=contact['_id']))
            else:
                fields = mongo.db.fields.find().sort("field_name", 1)
                return render_template("edit_contact.html", industrys=fields,
                                       user=user, contact=contact)
        flash("You have to own the contact in order to edit it!")
        return redirect(url_for("my_contact"))
    flash("You have to be loggedin in order to edit the contact")
    return redirect(url_for("login"))


@app.route("/my_contact")
def my_contact():
    if session["user"]:
        user = mongo.db.users.find_one({
            "username": session["user"]
        })
        contacts = mongo.db.contacts.find({"created_by": user["_id"]})
        return render_template("my_contact.html", user=user,
                               contacts=list(contacts))
    flash("You must be loged in to access your contacts!")
    return redirect(url_for("login"))


@app.route("/delete_contact/<string:id>")
def delete_contact(id):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        contact = mongo.db.contacts.find_one({
            "created_by": user["_id"],
            "_id": ObjectId(id)
        })
        if contact:
            mongo.db.contacts.remove({"_id": ObjectId(id)})
            flash("You have successfully deleted the contact!")
            return redirect(url_for("my_contact"))

        flash("You have to own the contact in order to Delete it!")
        return redirect(url_for("my_contact"))
    flash("You have to be loggedin in order to delete the contact!")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=False)