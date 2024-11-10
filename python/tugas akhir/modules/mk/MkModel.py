from connection import get_db
from core.CoreModel import CoreModel

class MkModel(CoreModel):
    def __init__(self):
        self.table_name = "mk"
        self.table_id = "mk_id"