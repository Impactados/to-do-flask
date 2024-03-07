import psycopg2
import config
import hashlib

def connect_database():
    
    try:
        connection = psycopg2.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password,
            port=config.port
        )

        return connection
    
    except Exception as err:

        return None
    
def criptografar_password(password):
    password_codificado = password.encode('utf-8')
    hash_sha256 = hashlib.sha256(password_codificado).hexdigest()
    return hash_sha256


