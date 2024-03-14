import utils
import mysql.connector
from mysql.connector import Error
from models.user import User

class UserService:
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

        except mysql.connector.IntegrityError as err:
            conn.rollback()
            return False, f"Nickname '{User.nickname}' já está em uso"
        except Error as err:
            conn.rollback()
            return False, err
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return True, None


    def remove_user(nickname):
        conn = None
        cursor = None
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()
            query = """DELETE FROM users WHERE nickname = %s"""
            cursor.execute(query, (nickname,))
            conn.commit()

        except Error as err:
            conn.rollback()
            return False, err

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

        return True, None

    def get_user(nickname):
        conn = None
        cursor = None
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()
            query = """SELECT * FROM users WHERE nickname = %s"""
            cursor.execute(query, (nickname,))
            user = cursor.fetchone()

            if user:
                return True, user
            else:
                return False, "Usuário não encontrado"
            
        except Error as err:
            return False, err

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
        
    def update_user(nickname, data):
        conn = None
        cursor = None
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

        except Error as err:
            conn.rollback()  # Adicionado rollback em caso de erro.
            return False, err

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

        return True, None

    def verify_user(User):
        conn = None
        cursor = None
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (User.nickname, User.password))
            user = cursor.fetchone()

            if user is None:
                return False, "Usuário não encontrado no banco de dados"
            
            return True, None

        except Error as err:
            return False, err

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
        
    def verify_identify(nickname, current_user):
        if current_user != nickname:
            return False, f"Autorização necessária"
        return True, None

    def criptografar_password(password):
        return utils.criptografar_password(password)