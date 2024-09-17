from flask import *
from modules.krs.KrsView import KrsView

app_krs = Blueprint('app_krs', __name__, template_folder='templates')
app_krs.add_url_rule('/', 'index', KrsView().index, methods=['GET'])
app_krs.add_url_rule('/create', 'create', KrsView().create, methods=['GET'])
app_krs.add_url_rule('/edit/<int:mhs_id>', 'edit', KrsView().edit, methods=['GET'])
app_krs.add_url_rule('/store', 'store', KrsView().store, methods=['POST'])
app_krs.add_url_rule('/update/<int:mhs_id>', 'update', KrsView().update, methods=['POST'])
app_krs.add_url_rule('/delete/<int:mhs_id>', 'delete', KrsView().delete, methods=['GET'])