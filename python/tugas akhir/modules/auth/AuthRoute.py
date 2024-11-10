from flask import *
from .AuthView import *
from modules.user.UserModel import UserModel

app_auth = Blueprint('app_auth', __name__, template_folder='templates')
@app_auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserModel().find_by_username(username)
        if user and user['password'] == password:
            print(f"User found: {user}")
            session['logged_in'] = True
            session['username'] = username
            session['nama_lengkap'] = user['nama_lengkap']
            session['role'] = user['role']
            session['id_user'] = user['id_user']
            return redirect(url_for('index'))
        else:
            flash('Username atau Password salah!', 'error')
            return redirect(url_for('app_auth.login'))
    return render_template('login.html')

@app_auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('role', None)
    session.pop('id_user', None)
    return redirect(url_for('app_auth.login'))