from flask import render_template, request, redirect, session
from modules.bimbingan.BimbinganModel import BimbinganModel
from werkzeug.utils import secure_filename
import os

class BimbinganView:

    @staticmethod
    def index():
        data = BimbinganModel().all_bimbingan()
        return render_template('bimbingan_index.html', data=data)
    
    @staticmethod
    def mhs_index():
        data = BimbinganModel().all_mhsbimbingan()
        return render_template('bimbinganMhs_index.html', data=data)

    @staticmethod
    def dsn_index():
        data = BimbinganModel().all_dsnbimbingan()
        return render_template('bimbinganDsn_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('bimbingan_create.html')
    
    @staticmethod
    def store():
        bimbingan_obj = BimbinganModel()
        post = request.form
        file = request.files.get('skripsi')
        bimbingan_obj.dosen_id = post['dosen_id']
        bimbingan_obj.mhs_id = post['mhs_id']
        bimbingan_obj.waktu = post['waktu']
        bimbingan_obj.bimbingan_ke = post['bimbingan_ke']
        bimbingan_obj.note = post['note']
        # Handle file upload
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join('static/upload', filename)
            file.save(file_path)
            bimbingan_obj.skripsi = filename  # Store the filename in the database
        else:
            bimbingan_obj.skripsi = None  # Or handle cases where a file is not required
        
        # Save the new bimbingan object
        BimbinganModel().store_bimbingan(bimbingan_obj)
        return redirect('/bimbingan')

    @staticmethod
    def edit(bimbingan_id):
        obj = BimbinganModel().find_bimbingan(bimbingan_id)
        if obj:
            return render_template('bimbingan_edit.html', obj=obj)
        else:
            return "Bimbingan not found", 404

    @staticmethod
    def UImhs_edit(bimbingan_id):
        obj = BimbinganModel().find_bimbingan(bimbingan_id)
        if obj:
            id_user = session.get('id_user')
            if obj.mhs_id == id_user:
                return render_template('bimbinganUIMhs_edit.html', obj=obj)
            else:
                return "Unauthorized", 403
        else:
            return "Bimbingan not found", 404

    @staticmethod
    def UIdsn_edit(bimbingan_id):
        obj = BimbinganModel().find_bimbingan(bimbingan_id)
        if obj:
            id_user = session.get('id_user')
            return render_template('bimbinganUIDsn_edit.html', obj=obj)
        else:
            return "Bimbingan not found", 404
    
    @staticmethod
    def update(bimbingan_id):
        data = BimbinganModel().find_bimbingan(bimbingan_id)
        if data:
            post = request.form
            file = request.files.get('skripsi')
            bimbingan_obj = BimbinganModel()
            bimbingan_obj.dosen_id = post['dosen_id']
            bimbingan_obj.mhs_id = post['mhs_id']
            bimbingan_obj.waktu = post['waktu']
            bimbingan_obj.bimbingan_ke = post['bimbingan_ke']
            bimbingan_obj.note = post['note']
            
            if file and file.filename != '':
                # Handle file upload
                filename = secure_filename(file.filename)
                file_path = os.path.join('static/upload', filename)
                file.save(file_path)
                bimbingan_obj.skripsi = filename  # Store the filename in the database
            else:
                # Preserve existing filename if no new file is uploaded
                bimbingan_obj.skripsi = data.skripsi
            
            BimbinganModel().update_bimbingan(bimbingan_id, bimbingan_obj)
            return redirect('/bimbingan')
        else:
            return "bimbingan not found", 404
        
    @staticmethod
    def delete(bimbingan_id):
        data = BimbinganModel().find_bimbingan(bimbingan_id)
        if data:
            BimbinganModel().delete_bimbingan(bimbingan_id)
            return redirect('/bimbingan')
        else:
            return "bimbingan not found", 404
