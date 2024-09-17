from flask import *
from .AuthModel import *

class AuthView():

    @staticmethod
    def index():
        data = AuthModel().all()
        return render_template('login.html', data=json.dumps(data))