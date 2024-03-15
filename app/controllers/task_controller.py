from models.task import Task
from services.task_service import TaskService
from services.user_service import UserService

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

class TaskController:
    def create_task():

        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        user_id = data.get('user_id')

 
        if None in [title, description, user_id]:
            return "Missing data", 400

        task = Task(
            title,
            description,
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

    def get_task(user_id):
        get, err = TaskService.get_task(user_id)

        if not get:
            return jsonify({
                "message": "Erro ao criar task",
                "error": str(err)
            }), 502

        return jsonify({
            "data": get,
            "message": "Task criado com sucesso",
        }), 201
