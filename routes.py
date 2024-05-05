from app import app
from flask import render_template, request, redirect
import forums, messages, results, threads, users

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
        if len(password1) < 5 or len(password2) < 5:
            return render_template("error.html", message="Password must contain at least five characters")
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")

        role = request.form["role"]

        if users.register(username, email, password1, role):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/forums")
def show_forums():
    forums_list = forums.get_forums()
    user = users.get_username()

    if users.get_user_id() > 0:
        return render_template("forums.html", count=len(forums_list), forums=forums_list, username=user)
    else:
        return render_template("error.html", message="You have to login to view this content")

@app.route("/new-forum")
def new_forum():
    return render_template("new-forum.html")

@app.route("/create-forum", methods=["POST"])
def create_forum():
    users.check_csrf()

    title = request.form["title"]

    if len(title) < 1 or len(title) > 100:
        return render_template("error.html", message="Title must contain 1-100 characters")

    if forums.create_forum(title):
        return redirect("/forums")
    else:
        return render_template("error.html", message="Failed to create forum")
    
@app.route("/threads")
def show_threads():
    threads_list = threads.get_threads()
    user = users.get_username()

    if users.get_user_id() > 0:
        return render_template("threads.html", threads=threads_list, username=user)
    else:
        return render_template("error.html", message="You have to login to view this content")

@app.route("/threads/<int:id>")
def threads_in_forum(id):
    forum_threads = threads.get_threads(id)
    if users.get_user_id() > 0:
        return render_template("threads.html", count=len(forum_threads), threads=forum_threads, forum_id=id)
    else:
        return render_template("error.html", message="You have to login to view this content")

@app.route("/new-thread/<int:id>")
def new_thread(id):
    return render_template("new-thread.html", forum_id=id)

@app.route("/create-thread", methods=["POST"])
def create_thread():
    users.check_csrf()

    title = request.form["title"]
    forum_id = request.form["forum_id"]

    if len(title) < 1 or len(title) > 100:
        return render_template("error.html", message="Title must contain 1-100 characters")

    if threads.create_thread(title, forum_id):
        url = "/threads/" + str(forum_id)
        return redirect(url)
    else:
        return render_template("error.html", message="Failed to create thread")
    
@app.route("/messages")
def show_messages():
    messages_list = messages.get_messages()
    user = users.get_username()

    if users.get_user_id() > 0:
        return render_template("messages.html", messages=messages_list, username=user)
    else:
        return render_template("error.html", message="You have to login to view this content")

@app.route("/messages/<int:id>")
def messages_in_thread(id):
    thread_messages = messages.get_messages(id)
    if users.get_user_id() > 0:
        return render_template("messages.html", count=len(thread_messages), messages=thread_messages, thread_id=id)
    else:
        return render_template("error.html", message="You have to login to view this content")

@app.route("/new-message/<int:id>")
def new_message(id):
    return render_template("new-message.html", thread_id=id)

@app.route("/send-message", methods=["POST"])
def send_message():
    users.check_csrf()

    content = request.form["content"]
    thread_id = request.form["thread_id"]

    if len(content) < 1 or len(content) > 5000:
        return render_template("error.html", message="Message must contain 1-5000 characters")
    
    if messages.send_message(content, thread_id):
        url = "/messages/" + str(thread_id)
        return redirect(url)
    else:
        return render_template("error.html", message="Failed to send message")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    users.require_role(2)

    if request.method == "GET":
        forums_list = forums.get_forums()
        return render_template("remove.html", forums=forums_list)

    if request.method == "POST":
        users.check_csrf()

        if "forum" in request.form:
            forum = request.form["forum"]
            forums.remove_forum(forum)

        return redirect("/forums")

@app.route("/result")
def show_results():
    results_list = results.get_results()
    return render_template("results.html", results=results_list)