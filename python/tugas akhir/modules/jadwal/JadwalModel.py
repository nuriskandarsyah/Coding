from connection import get_db
from core.CoreModel import CoreModel

class JadwalModel(CoreModel):
    def __init__(self):
        self.table_name = "jadwal"
        self.table_relation = ""
        self.table_id = "jdwl_id"