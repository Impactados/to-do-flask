import utils
from models.task import Task

class TaskService:
    def save_task(Task: Task):
        try:
            conn = utils.connect_database()
            cursor = conn.cursor()

            query = """INSERT INTO tasks (titulo, descricao, status, nickname) VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (Task.titulo, Task.descricao, Task.status, Task.nickname))
            conn.commit()
            conn.close()

            return True, None

        except Exception as err:
            return False, err