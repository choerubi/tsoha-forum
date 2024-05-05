from db import db
from flask import request
from sqlalchemy.sql import text

def get_results():
    query = request.args["query"]
    sql = text("SELECT title FROM forums WHERE title LIKE :query AND visible = 1")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()