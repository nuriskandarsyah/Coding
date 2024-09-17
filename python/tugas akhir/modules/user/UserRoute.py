from flask import *
from modules.user.UserView import UserView

app_user = Blueprint('app_user', __name__, template_folder='templates')
app_user.add_url_rule('/', 'index', UserView().index, methods=['GET'])
app_user.add_url_rule('/create', 'create', UserView().create, methods=['GET'])
app_user.add_url_rule('/edit/<int:id_user>', 'edit', UserView().edit, methods=['GET'])
app_user.add_url_rule('/editMHS', 'editMHS', UserView.editMHS, methods=['GET'])
app_user.add_url_rule('/editDSN', 'editDSN', UserView.editDSN, methods=['GET'])
app_user.add_url_rule('/store', 'store', UserView().store, methods=['POST'])
app_user.add_url_rule('/update/<int:id_user>', 'update', UserView().update, methods=['POST'])
app_user.add_url_rule('/updateMHS/<int:id_user>', 'updateMHS', UserView.updateMHS, methods=['POST'])
app_user.add_url_rule('/updateDSN/<int:id_user>', 'updateDSN', UserView.updateDSN, methods=['POST'])
app_user.add_url_rule('/delete/<int:id_user>', 'delete', UserView().delete, methods=['GET'])