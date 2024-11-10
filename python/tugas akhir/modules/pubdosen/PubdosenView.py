from flask import render_template, request, redirect
from modules.pubdosen.PubdosenModel import PubdosenModel
from werkzeug.utils import secure_filename
import os

class PubdosenView:

    @staticmethod
    def index():
        data = PubdosenModel().all_pubdosen()
        return render_template('pubdosen_index.html', data=data)

    @staticmethod
    def create():
        return render_template('pubdosen_create.html')
    
    @staticmethod
    def store():
        pubdosen_obj = PubdosenModel()
        post = request.form
        file = request.files.get('jurnal')
        pubdosen_obj.dosen_id= post['dosen_id']
        pubdosen_obj.judul = post['judul']
        pubdosen_obj.tgl_terbit = post['tgl_terbit']
         # Handle file upload
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join('static/upload', filename)
            file.save(file_path)
            pubdosen_obj.jurnal = filename  # Store the filename in the database
        else:
            pubdosen_obj.jurnal = None  # Or handle cases where a file is not required
        
        # Save the new pubdosen object
        PubdosenModel().store_pubdosen(pubdosen_obj)
        return redirect('/pubdosen')

    @staticmethod
    def edit(pub_id):
        obj = PubdosenModel().find_pubdosen(pub_id)
        if obj:
            return render_template('pubdosen_edit.html', obj=obj)
        else:
            return "pubdosen not found", 404
    
    @staticmethod
    def update(pub_id):
        data = PubdosenModel().find_pubdosen(pub_id)
        if data:
            post = request.form
            file = request.files.get('jurnal')
            pubdosen_obj = PubdosenModel()
            pubdosen_obj.dosen_id= post['dosen_id']
            pubdosen_obj.judul = post['judul']
            pubdosen_obj.tgl_terbit = post['tgl_terbit']
            
            if file and file.filename != '':
                # Handle file upload
                filename = secure_filename(file.filename)
                file_path = os.path.join('static/upload', filename)
                file.save(file_path)
                pubdosen_obj.jurnal = filename  # Store the filename in the database
            else:
                # Preserve existing filename if no new file is uploaded
                pubdosen_obj.jurnal = data.jurnal
            
            PubdosenModel().update_pubdosen(pub_id, pubdosen_obj)
            return redirect('/pubdosen')
        else:
            return "pubdosen not found", 404
        
    @staticmethod
    def delete(pub_id):
        data = PubdosenModel().find_pubdosen(pub_id)
        if data:
            PubdosenModel().delete_pubdosen(pub_id)
            return redirect('/pubdosen')
        else:
            return "pubdosen not found", 404
