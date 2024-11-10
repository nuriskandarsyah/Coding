from connection import get_db
from core.CoreModel import CoreModel

class UserModel(CoreModel):
    def __init__(self):
        self.table_name = "user"
        self.table_id = "id_user"
    
    def __repr__(self):
        return f'<User {self.username}>'