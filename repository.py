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

def verify_user(User: User):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE nickname = %s AND password = %s", (User.nickname, User.password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user == None:
            return False, "usuario nao encontrado no banco de dados"
        
        return True, None

    except Exception as err:
        return False, err
