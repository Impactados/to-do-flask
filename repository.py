from models import User
import utils
import psycopg2

def save_user(User: User):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        query = """SELECT * FROM users WHERE nickname = %s"""
        cursor.execute(query, (User.nickname, ))
        result = cursor.fetchone()

        if result is not None:
            return False, f"Nickname '{User.nickname}' já está em uso"

        query = """INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)"""
        cursor.execute(query, (User.name, User.nickname, User.password))
        conn.commit()
        conn.close()

        return True, None

    except psycopg2.errors.UniqueViolation as err:
        return False, f"Nickname '{User.nickname}' já está em uso"

    except Exception as err:
        return False, err


def remove_user(nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """DELETE FROM users WHERE nickname = %s"""
        cursor.execute(query, (nickname, ))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

def get_user(nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """SELECT * FROM users WHERE nickname = %s"""
        cursor.execute(query, (nickname, ))
        user = cursor.fetchone()
        
        conn.close()

        if user:
            return True, user
        else:
            return False, "Usuário não encontrado"
    
    except Exception as err:
        return False, err
    
def update_user(nickname, data):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        if 'nickname' in data and data['nickname'] != nickname:
            query = """SELECT * FROM users WHERE nickname = %s"""
            cursor.execute(query, (data['nickname'],))
            result = cursor.fetchone()

            if result is not None:
                return False, f"Nickname '{data['nickname']}' já está em uso"

        
        update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"""UPDATE users SET {update_fields} WHERE nickname = %s"""

        
        values = list(data.values())
        values.append(nickname)

        
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

