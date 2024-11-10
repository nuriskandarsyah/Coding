from flask import *
from modules.mk.MkView import MkView

app_mk = Blueprint('app_mk', __name__, template_folder='templates')
app_mk.add_url_rule('/', 'index', MkView().index, methods=['GET'])
app_mk.add_url_rule('/create', 'create', MkView().create, methods=['GET'])
app_mk.add_url_rule('/edit/<int:mk_id>', 'edit', MkView().edit, methods=['GET'])
app_mk.add_url_rule('/store', 'store', MkView().store, methods=['POST'])
app_mk.add_url_rule('/update/<int:mk_id>', 'update', MkView().update, methods=['POST'])
app_mk.add_url_rule('/delete/<int:mk_id>', 'delete', MkView().delete, methods=['GET'])