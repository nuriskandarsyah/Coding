from flask import *
from modules.admin.AdminView import *

app_admin = Blueprint('app_admin', __name__, template_folder='templates')
app_admin.add_url_rule('/', 'index', AdminView().index, methods=['GET'])
app_admin.add_url_rule('/create', 'create', AdminView().create, methods=['GET'])
app_admin.add_url_rule('/edit/<int:adm_id>', 'edit', AdminView().edit, methods=['GET'])
app_admin.add_url_rule('/store', 'store', AdminView().store, methods=['POST'])
app_admin.add_url_rule('/update/<int:adm_id>', 'update', AdminView().update, methods=['POST'])
app_admin.add_url_rule('/delete/<int:adm_id>', 'delete', AdminView().delete, methods=['GET'])