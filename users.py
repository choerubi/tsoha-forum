import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def login(email, password):
    sql = text("SELECT id, password, role FROM users WHERE email=:email")
    result = db.session.execute(sql, {"email":email})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_role"] = user.role
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_role"]

def register(username, email, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = text("""INSERT INTO users (username, email, password, role)
                    VALUES (:username, :email, :password, :role)""")
        db.session.execute(sql, {"username":username, "email":email, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return login(email, password)

def user_id():
    return session.get("user_id", 0)

def check_role(role):
    if role > session.get("user_role", 0):
        abort(403)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)