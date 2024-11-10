from flask import *
from modules.bimbingan.BimbinganView import BimbinganView

app_bimbingan = Blueprint('app_bimbingan', __name__, template_folder='templates')

app_bimbingan.add_url_rule('/', 'index', BimbinganView.index, methods=['GET'])
app_bimbingan.add_url_rule('/mhs', 'mhs_index', BimbinganView.mhs_index, methods=['GET'])
app_bimbingan.add_url_rule('/dsn', 'dsn_index', BimbinganView.dsn_index, methods=['GET'])
app_bimbingan.add_url_rule('/create', 'create', BimbinganView.create, methods=['GET'])
app_bimbingan.add_url_rule('/edit/<int:bimbingan_id>', 'edit', BimbinganView.edit, methods=['GET'])
app_bimbingan.add_url_rule('/UImhs_edit/<int:bimbingan_id>', 'UImhs_edit', BimbinganView.UImhs_edit, methods=['GET'])
app_bimbingan.add_url_rule('/UIdsn_edit/<int:bimbingan_id>', 'UIdsn_edit', BimbinganView.UIdsn_edit, methods=['GET'])
app_bimbingan.add_url_rule('/store', 'store', BimbinganView.store, methods=['POST'])
app_bimbingan.add_url_rule('/update/<int:bimbingan_id>', 'update', BimbinganView.update, methods=['POST'])
app_bimbingan.add_url_rule('/delete/<int:bimbingan_id>', 'delete', BimbinganView.delete, methods=['GET'])
