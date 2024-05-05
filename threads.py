from db import db
from sqlalchemy.sql import text
import users

def get_threads(forum_id):
    sql = text("""SELECT T.id, T.forum_id, T.title, U.username, T.created_at FROM threads T, users U
                WHERE U.id = T.user_id AND T.forum_id = :forum_id ORDER BY T.id""")
    result = db.session.execute(sql, {"forum_id":forum_id})
    return result.fetchall()

def create_thread(title, forum_id):
    user_id = users.get_user_id()
    if user_id == 0:
        return False
    else:
        sql = text("""INSERT INTO threads (title, user_id, forum_id, created_at)
                    VALUES (:title, :user_id, :forum_id, NOW())""")
        db.session.execute(sql, {"title":title, "user_id":user_id, "forum_id":forum_id})
        db.session.commit()
        return True