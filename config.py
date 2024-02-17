from dotenv import find_dotenv, load_dotenv
import os 

load_dotenv(find_dotenv('.env'))

database = os.environ.get("database")
host = os.environ.get("host")
password = os.environ.get("password")
port = os.environ.get("port")
user = os.environ.get("user")
secret = os.environ.get("secret")
