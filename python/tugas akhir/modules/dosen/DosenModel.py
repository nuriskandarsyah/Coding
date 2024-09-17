from connection import get_db
from core.CoreModel import CoreModel

class DosenModel(CoreModel):
    def __init__(self):
        self.table_name = "dosen"
        self.table_relation = "user"
        self.table_id = "dosen_id"