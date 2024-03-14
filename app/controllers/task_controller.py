from models.task import Task
from services.task_service import TaskService
from services.user_service import UserService

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

class TaskController:
    def create_task(nickname):
        current_user = get_jwt_identity()
        user, error = UserService.verify_identify(nickname, current_user)
        if not user:
            return jsonify({
                "message": "Unauthorized",
                "error": str(error)
                }), 401

        task = Task(
            request.json.get('titulo'),
            request.json.get('descricao'),
            request.json.get('status'),
            nickname
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