from models.task import Task
from services.task_service import TaskService
from services.user_service import UserService

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

class TaskController:
    def create_task(nickname):
        user_id = UserService.check_id(nickname)
        task = Task(
            request.form.get('title'),
            request.form.get('description'),
            request.form.get('status'),
            request.form.get('timer'),
            user_id
        )

        save, err = TaskService.save_task(task)

        if not save:
            return jsonify({
                "message": "Erro ao criar task",
                "error": str(err)
            }), 502

        return jsonify({
            "message": "Task criado com sucesso",
        }), 201
