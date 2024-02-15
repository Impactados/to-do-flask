from models import User
import utils

def save_user(User: User):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)"""
        cursor.execute(query, (User.name, User.nickname, User.password))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

