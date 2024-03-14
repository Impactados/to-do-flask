import utils
from models.task import Task

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