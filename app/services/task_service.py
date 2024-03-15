import utils
from models.task import Task
import mysql.connector
from mysql.connector import Error

class TaskService:
    def save_task(Task: Task):
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()

            query = """INSERT INTO tasks (title, description, status, timer, user_id) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (Task.title, Task.description, Task.status, Task.timer, Task.user_id))
            conn.commit()
            conn.close()

            return True, None

        except Exception as err:
            return False, err
        
    def get_task(user_id):
        conn = None
        cursor = None
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()
            query = """SELECT id, title, description FROM tasks WHERE user_id = %s"""
            cursor.execute(query, (user_id,))
            data = cursor.fetchall()

            if data:
                return data, True
            else:
                return False, "Usuário não encontrado"
            
        except Error as err:
            return False, err
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()