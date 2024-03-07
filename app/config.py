import os

class Data:
    
    def database():
        return os.environ.get("DATABASE")

    def host():
        return os.environ.get("HOST")

    def password():
        return os.environ.get("PASSWORD")

    def port():
        return os.environ.get("PORT")

    def user():
        return os.environ.get("USER")
        
    def secret():
        return os.environ.get("SECRET")

