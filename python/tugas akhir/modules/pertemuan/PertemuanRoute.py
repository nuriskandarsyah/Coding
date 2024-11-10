from flask import *
from modules.pertemuan.PertemuanView import PertemuanView

app_pertemuan = Blueprint('app_pertemuan', __name__, template_folder='templates')
app_pertemuan.add_url_rule('/', 'index', PertemuanView().index, methods=['GET'])
app_pertemuan.add_url_rule('/create', 'create', PertemuanView().create, methods=['GET'])
app_pertemuan.add_url_rule('/edit/<int:pertemuan_id>', 'edit', PertemuanView().edit, methods=['GET'])
app_pertemuan.add_url_rule('/store', 'store', PertemuanView().store, methods=['POST'])
app_pertemuan.add_url_rule('/update/<int:pertemuan_id>', 'update', PertemuanView().update, methods=['POST'])
app_pertemuan.add_url_rule('/delete/<int:pertemuan_id>', 'delete', PertemuanView().delete, methods=['GET'])