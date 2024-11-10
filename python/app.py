from flask import Flask, abort, render_template, send_from_directory, request, redirect, url_for, session
from modules.mahasiswa.Route import app_mahasiswa
from modules.dosen.DosenRoute import app_dosen
from modules.user.UserRoute import app_user
from modules.admin.AdminRoute import app_admin
from modules.mk.MkRoute import app_mk
from modules.pubdosen.PubdosenRoute import app_pubdosen
from modules.bimbingan.BimbinganRoute import app_bimbingan
from modules.auth.AuthRoute import app_auth
from modules.kalender_akademik.KalenderAkademikRoute import app_kalender_akademik
from modules.pertemuan.PertemuanRoute import app_pertemuan
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from modules.pubdosen.PubdosenModel import PubdosenModel
from modules.bimbingan.BimbinganModel import BimbinganModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'umc12345'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/upload')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')
app.register_blueprint(app_dosen, url_prefix='/dosen')
app.register_blueprint(app_user, url_prefix='/user')
app.register_blueprint(app_admin, url_prefix='/admin')
app.register_blueprint(app_auth, url_prefix='/login')
app.register_blueprint(app_mk, url_prefix='/mk')
app.register_blueprint(app_pubdosen, url_prefix='/pubdosen')
app.register_blueprint(app_bimbingan, url_prefix='/bimbingan')
app.register_blueprint(app_kalender_akademik, url_prefix='/kalender_akademik')
app.register_blueprint(app_pertemuan, url_prefix='/pertemuan')


@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('app_auth.login'))
    nama_lengkap = session.get('nama_lengkap', '')
    return render_template('index.html', nama_lengkap=nama_lengkap)

def allowed_file(filename):
    allowed_extensions = {'pdf'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/pubdosen/store', methods=['GET', 'POST'])
def upload_pubdosen_file():
    if request.method == 'POST':
        if 'jurnal' not in request.files:
            return "No file part", 400
        
        jurnal = request.files['jurnal']
        
        if jurnal.filename == '':
            return "No selected file", 400
        
        if jurnal and allowed_file(jurnal.filename):
            filename = secure_filename(jurnal.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            jurnal.save(file_path)
            # Save filename to the database if needed
            return redirect(url_for('download_pubdosen_file'))
        
        return "File type not allowed", 400
    
    return render_template('pubdosen_index.html')

@app.route('/pubdosen/download/<filename>')
def download_pubdosen_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return abort(404) 
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/pubdosen/edit/<int:pub_id>', methods=['GET', 'POST'])
def edit_pubdosen_file(pub_id):
    obj = PubdosenModel().find_pubdosen(pub_id)
    
    if request.method == 'POST':
        if 'jurnal' not in request.files:
            return "No file part", 400
        
        jurnal = request.files['jurnal']
        
        if jurnal.filename == '':
            return "No selected file", 400
        
        if jurnal and allowed_file(jurnal.filename):
            filename = secure_filename(jurnal.filename)
            jurnal_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], obj.jurnal)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
            
            jurnal.save(jurnal_filename)
            
            PubdosenModel().update_pubdosen(pub_id, filename)
            
            return redirect(url_for('edit_pubdosen_file', pub_id=pub_id))
        
        return "File type not allowed", 400
    
    return render_template('pubdosen_edit.html', obj=obj)

@app.route('/bimbingan/store', methods=['GET', 'POST'])
def upload_bimbingan_file():
    if request.method == 'POST':
        if 'skripsi' not in request.files:
            return "No file part", 400
        
        skripsi = request.files['skripsi']
        
        if skripsi.filename == '':
            return "No selected file", 400
        
        if skripsi and allowed_file(skripsi.filename):
            filename = secure_filename(skripsi.filename)
            skripsi_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            skripsi.save(skripsi_filename)
            return redirect(url_for('upload_bimbingan_file'))
        
        return "File type not allowed", 400
    
    return render_template('bimbingan_index.html')

@app.route('/bimbingan/edit/<int:bimbingan_id>', methods=['GET', 'POST'])
def edit_bimbingan_file(bimbingan_id):
    obj = BimbinganModel().find_bimbingan(bimbingan_id)
    
    if request.method == 'POST':
        if 'skripsi' not in request.files:
            return "No file part", 400
        
        skripsi = request.files['skripsi']
        
        if skripsi.filename == '':
            return "No selected file", 400
        
        if skripsi and allowed_file(skripsi.filename):
            filename = secure_filename(skripsi.filename)
            skripsi_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], obj.skripsi)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
            
            skripsi.save(skripsi_filename)
            BimbinganModel().update_bimbingan(bimbingan_id, filename)
            
            return redirect(url_for('edit_bimbingan_file', bimbingan_id=bimbingan_id))
        
        return "File type not allowed", 400
    
    return render_template('bimbingan_edit.html', obj=obj)

if __name__ == '__main__':
    app.debug = True
    app.run()
