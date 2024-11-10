from connection import get_db
from core.CoreModel import CoreModel

class PubdosenModel(CoreModel):
    def __init__(self):
        self.table_name = "pubdosen"
        self.table_relation = "dosen"
        self.table_nest = "user"
        self.table_id = "pub_id"