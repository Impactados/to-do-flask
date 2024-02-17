
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
        request.json.get('name'),
        request.json.get('nickname'),
        password
    )

    save, err = repository.save_user(user)

    if not save:
        return jsonify({
            "message": "Erro ao criar usuário",
            "error": str(err)
        }), 502

    return jsonify({
        "message": "Usuário criado com sucesso",
        "requestID": requestid
    }), 201

def delete_user(nickname):

    remove, err = repository.remove_user(nickname)

    if not remove:
        return jsonify({
            "message": "erro ao deletar usuário",
            "error": str(err)
        }), 502

    return jsonify({
        "message": "usuário deletado com sucesso",
    }), 201

def read_user(nickname):

    exists, value = repository.get_user(nickname)
    
    if not exists:
        return jsonify({
            "message": "Usuário não encontrado",
        }), 404

    elif exists:
        return jsonify({
            "message": "Usuário encontrado",
            "user": value
        }), 200
    
    return jsonify({
        "message": "erro ao encontrar usuário",
        "error": value
    }), 502

def update_user(nickname):

    data = request.json
    if 'password' in data:
        new_password = utils.criptografar_password(data['password'])
        data['password'] = new_password

    update, err = repository.update_user(nickname, data)

    if not update:
        return jsonify({
            "message": "erro ao atualizar usuário",
            "error": str(err)
        }), 502

    return jsonify({
        "message": "usuário atualizado com sucesso",
    }), 201


