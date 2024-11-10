from flask import render_template, request, redirect
from modules.jadwal.JadwalModel import JadwalModel

class JadwalView:

    @staticmethod
    def index():
        data = JadwalModel().all_mhs()
        return render_template('jadwal_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('jadwal_index.html')
    
    @staticmethod
    def store():
        jadwal_obj = JadwalModel()
        post = request.form
        jadwal_obj.dosen_id= post['dosen_id']
        jadwal_obj.mk_id = post['mk_id']
        jadwal_obj.pertemuan_id = post['pertemuan_id']
        JadwalModel().store(jadwal_obj)
        return redirect('/jadwal')

    @staticmethod
    def edit(jdwl_id):
        obj = JadwalModel().find(jdwl_id)
        if obj:
            return render_template('jadwal_edit.html', obj=obj)
        else:
            return "jadwal not found", 404
    
    @staticmethod
    def update(jdwl_id):
        data = JadwalModel().find(jdwl_id)
        if data:
            post = request.form
            jadwal_obj = JadwalModel()
            jadwal_obj.dosen_id= post['dosen_id']
            jadwal_obj.mk_id = post['mk_id']
            jadwal_obj.pertemuan_id = post['pertemuan_id']
            JadwalModel().update(jdwl_id, jadwal_obj)
            return redirect('/jadwal')
        else:
            return "jadwal not found", 404
        
    @staticmethod
    def delete(jdwl_id):
        data = JadwalModel().find(jdwl_id)
        if data:
            JadwalModel().delete(jdwl_id)
            return redirect('/jadwal')
        else:
            return "jadwal not found", 404
