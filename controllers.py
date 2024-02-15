import models
import repository
import utils
from flask import Flask, request, jsonify
from main import jwt, create_access_token, get_jwt_identity

def create_user():

    password = utils.criptografar_password(request.json.get('password'))

    user = models.User(
        request.json.get('name'),
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
    }), 201
    
def login():

    password = utils.criptografar_password(request.json.get('password'))

    user = models.User(
        None,
        request.json.get('nickname'),
        password
        )
    
    login, err = repository.verify_user(user)

    if not login:
        return jsonify({
            "message": "erro no nickname ou senha",
            "error": str(err)
        }), 502
    
    access_token = create_access_token(identity=user.nickname)
    
    return jsonify({
        "message": "usuário encontrado",
        "token": access_token
    }), 200

def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
