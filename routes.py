from app import app
from flask import render_template, request, redirect, session
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        if users.login(email, password):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Incorrect email or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Username must contain 1-20 characters")

        email = request.form["email"]

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if len(password1) < 5:
            return render_template("error.html", message="Password must contain at least five characters")
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")

        role = request.form["role"]

        if users.register(username, email, password1):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/forums")
def forums():
    if session["user_id"]:
        return render_template("forums.html")
    else:
        return render_template("error.html", message="You have to login to view this content")