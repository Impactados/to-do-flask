import mysql.connector
import hashlib
import os

def connect_database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST", "db"),
            user=os.getenv("DATABASE_USER", "your_user"),
            password=os.getenv("DATABASE_PASSWORD", "your_user_password"),
            database=os.getenv("DATABASE_NAME", "your_database")
        )
        
        return connection
    except mysql.connector.Error as err:
        raise err
    
def criptografar_password(password):
    password_codificado = password.encode('utf-8')
    hash_sha256 = hashlib.sha256(password_codificado).hexdigest()
    return hash_sha256


