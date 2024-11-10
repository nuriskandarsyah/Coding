from flask import render_template, request, redirect
from modules.mahasiswa.Model import MahasiswaModel

class MahasiswaView:

    @staticmethod
    def index():
        data = MahasiswaModel().all_mhs()
        return render_template('mahasiswa_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('mahasiswa_create.html')
    
    @staticmethod
    def store():
        mahasiswa_obj = MahasiswaModel()
        post = request.form
        mahasiswa_obj.id_user= post['id_user']
        mahasiswa_obj.prodi = post['prodi']
        MahasiswaModel().store(mahasiswa_obj)
        return redirect('/mahasiswa')

    @staticmethod
    def edit(mhs_id):
        obj = MahasiswaModel().find(mhs_id)
        if obj:
            return render_template('mahasiswa_edit.html', obj=obj)
        else:
            return "Mahasiswa not found", 404
    
    @staticmethod
    def update(mhs_id):
        data = MahasiswaModel().find(mhs_id)
        if data:
            post = request.form
            mahasiswa_obj = MahasiswaModel()
            mahasiswa_obj.id_user= post['id_user']
            mahasiswa_obj.prodi = post['prodi']
            MahasiswaModel().update(mhs_id, mahasiswa_obj)
            return redirect('/mahasiswa')
        else:
            return "Mahasiswa not found", 404
        
    @staticmethod
    def delete(mhs_id):
        data = MahasiswaModel().find(mhs_id)
        if data:
            MahasiswaModel().delete(mhs_id)
            return redirect('/mahasiswa')
        else:
            return "Mahasiswa not found", 404
