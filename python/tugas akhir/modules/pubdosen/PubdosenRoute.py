from flask import *
from modules.pubdosen.PubdosenView import PubdosenView

app_pubdosen = Blueprint('app_pubdosen', __name__, template_folder='templates')
app_pubdosen.add_url_rule('/', 'index', PubdosenView().index, methods=['GET'])
app_pubdosen.add_url_rule('/create', 'create', PubdosenView().create, methods=['GET'])
app_pubdosen.add_url_rule('/edit/<int:pub_id>', 'edit', PubdosenView().edit, methods=['GET'])
app_pubdosen.add_url_rule('/store', 'store', PubdosenView().store, methods=['POST'])
app_pubdosen.add_url_rule('/update/<int:pub_id>', 'update', PubdosenView().update, methods=['POST'])
app_pubdosen.add_url_rule('/delete/<int:pub_id>', 'delete', PubdosenView().delete, methods=['GET'])
