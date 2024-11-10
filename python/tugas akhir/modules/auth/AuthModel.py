from core.CoreModel import CoreModel

class AuthModel(CoreModel):

    def __init__(self):
        self.table_name = "user"
        self.table_id = "id_user"