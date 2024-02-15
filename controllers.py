
import main
import models
import repository
import uuid
import utils
from flask import Flask, request, jsonify

def create_user():

    requestid = str(uuid.uuid4())

    password = utils.criptografar_password(request.json.get('password'))

    user = models.User(
        request.json.get('nome'),
        request.json.get('nickname'),
        password
        )
    
    save, err = repository.save_user(user)

    if not save:
        return jsonify({
            "message": "erro ao criar usuário",
            "error": err
        }), 502

    return jsonify({
        "message": "usuário criado com sucesso",
        "requestID": requestid
    }), 201
    
def login():
    return 