from connection import get_db
from core.CoreModel import CoreModel

class MahasiswaModel(CoreModel):
    def __init__(self):
        self.table_name = "mahasiswa"
        self.table_relation = "user"
        self.table_id = "mhs_id"