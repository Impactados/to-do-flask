class Task():
    def __init__(self, title, description, user_id, status = '', timer = ''):    
        self.title = title
        self.description = description
        self.status = status
        self.timer = timer
        self.user_id = user_id