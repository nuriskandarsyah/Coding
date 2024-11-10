from flask import *
from modules.mahasiswa.View import MahasiswaView

app_mahasiswa = Blueprint('app_mahasiswa', __name__, template_folder='templates')
app_mahasiswa.add_url_rule('/', 'index', MahasiswaView().index, methods=['GET'])
app_mahasiswa.add_url_rule('/create', 'create', MahasiswaView().create, methods=['GET'])
app_mahasiswa.add_url_rule('/edit/<int:mhs_id>', 'edit', MahasiswaView().edit, methods=['GET'])
app_mahasiswa.add_url_rule('/store', 'store', MahasiswaView().store, methods=['POST'])
app_mahasiswa.add_url_rule('/update/<int:mhs_id>', 'update', MahasiswaView().update, methods=['POST'])
app_mahasiswa.add_url_rule('/delete/<int:mhs_id>', 'delete', MahasiswaView().delete, methods=['GET'])