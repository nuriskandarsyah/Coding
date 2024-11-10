from connection import get_db
from core.CoreModel import CoreModel

class AdminModel(CoreModel):
    def __init__(self):
        self.table_name = "admin"
        self.table_relation = "user"
        self.table_id = "adm_id"