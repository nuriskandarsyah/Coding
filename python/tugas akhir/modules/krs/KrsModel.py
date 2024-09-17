from connection import get_db
from core.CoreModel import CoreModel

class KrsModel(CoreModel):
    def __init__(self):
        self.table_name = "krs"
        self.table_relation = ""
        self.table_id = "krs_id"