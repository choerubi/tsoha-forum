from db import db
from sqlalchemy.sql import text
import users

def get_forums():
    sql = text("""SELECT F.id, F.title, U.username, F.created_at FROM forums F, users U
                WHERE U.id = F.user_id AND F.visible = 1 ORDER BY F.id""")
    result = db.session.execute(sql)
    return result.fetchall()
    
def create_forum(title):
    user_id = users.get_user_id()
    if user_id == 0:
        return False
    else:
        sql = text("""INSERT INTO forums (title, user_id, created_at, visible)
                    VALUES (:title, :user_id, NOW(), 1)""")
        db.session.execute(sql, {"title":title, "user_id":user_id})
        db.session.commit()
        return True
    
def remove_forum(forum_id):
    sql = text("UPDATE forums SET visible = 0 WHERE id = :id")
    db.session.execute(sql, {"id":forum_id})
    db.session.commit()