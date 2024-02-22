import utils
import models
import repository

def save_user(user: models.User):
    save, err = repository.save_user(user)
    return save, err

def criptografar_password(password):
    return utils.criptografar_password(password)