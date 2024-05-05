from db import db
from sqlalchemy.sql import text
import users

def get_messages(thread_id):
    sql = text("""SELECT M.id, M.thread_id, M.content, U.username, M.sent_at FROM messages M, users U
                WHERE U.id = M.user_id AND M.thread_id = :thread_id ORDER BY M.id""")
    result = db.session.execute(sql, {"thread_id":thread_id})
    return result.fetchall()

def send_message(content, thread_id):
    user_id = users.get_user_id()
    if user_id == 0:
        return False
    else:
        sql = text("""INSERT INTO messages (content, user_id, thread_id, sent_at)
                    VALUES (:content, :user_id, :thread_id, NOW())""")
        db.session.execute(sql, {"content":content, "user_id":user_id, "thread_id":thread_id})
        db.session.commit()
        return True