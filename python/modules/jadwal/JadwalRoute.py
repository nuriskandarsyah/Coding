from flask import *
from modules.jadwal.JadwalView import JadwalView

app_jadwal = Blueprint('app_jadwal', __name__, template_folder='templates')
app_jadwal.add_url_rule('/', 'index', JadwalView().index, methods=['GET'])
app_jadwal.add_url_rule('/create', 'create', JadwalView().create, methods=['GET'])
app_jadwal.add_url_rule('/edit/<int:mhs_id>', 'edit', JadwalView().edit, methods=['GET'])
app_jadwal.add_url_rule('/store', 'store', JadwalView().store, methods=['POST'])
app_jadwal.add_url_rule('/update/<int:mhs_id>', 'update', JadwalView().update, methods=['POST'])
app_jadwal.add_url_rule('/delete/<int:mhs_id>', 'delete', JadwalView().delete, methods=['GET'])