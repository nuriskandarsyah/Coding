from connection import get_db
from core.CoreModel import CoreModel

class BimbinganModel(CoreModel):
    def __init__(self):
        self.table_name = "bimbingan"
        self.table_relation1 = "dosen"
        self.table_relation2 = "mahasiswa"
        self.table_nest = "user"
        self.table_id = "bimbingan_id"