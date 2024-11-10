"""

from flask import Blueprint, request, session, redirect, url_for, render_template
from modules.user.UserModel import UserModel

app_auth = Blueprint('app_auth', __name__, template_folder='templates')

@app_auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserModel().find_by_username(username)
        if user:
            print(f"User found: {user}")

            # Perbandingan password plaintext
            if user['password'] == password:
                session['logged_in'] = True
                session['username'] = username
                session['nama_lengkap'] = user['nama_lengkap']
                session['role'] = user['role']

                if user['role'] == 'admin':
                    return redirect(url_for('index'))
                elif user['role'] == 'dosen':
                    return redirect(url_for('indexdsn'))
                elif user['role'] == 'mahasiswa':
                    return redirect(url_for('indexmhs'))
            else:
                print("Invalid password")
                
        return "Invalid credentials", 401
    return render_template('login.html')

@app_auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('nama_lengkap', None)
    session.pop('role', None)
    return redirect(url_for('app_auth.login'))
"""