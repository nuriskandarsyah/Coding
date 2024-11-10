from flask import *
from modules.kalender_akademik.KalenderAkademikView import KalenderAkademikView

app_kalender_akademik = Blueprint('app_kalender_akademik', __name__, template_folder='templates')
app_kalender_akademik.add_url_rule('/', 'index', KalenderAkademikView().index, methods=['GET'])
app_kalender_akademik.add_url_rule('/create', 'create', KalenderAkademikView().create, methods=['GET'])
app_kalender_akademik.add_url_rule('/edit/<int:kk_id>', 'edit', KalenderAkademikView().edit, methods=['GET'])
app_kalender_akademik.add_url_rule('/store', 'store', KalenderAkademikView().store, methods=['POST'])
app_kalender_akademik.add_url_rule('/update/<int:kk_id>', 'update', KalenderAkademikView().update, methods=['POST'])
app_kalender_akademik.add_url_rule('/delete/<int:kk_id>', 'delete', KalenderAkademikView().delete, methods=['GET'])