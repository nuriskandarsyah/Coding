from connection import get_db
from core.CoreModel import CoreModel

class KalenderAkademikModel(CoreModel):
    def __init__(self):
        self.table_name = "kalender_akademik"
        self.table_id = "kk_id"