from flask import render_template, request, redirect
from modules.pertemuan.PertemuanModel import PertemuanModel

class PertemuanView:

    @staticmethod
    def index():
        data = PertemuanModel().all_pertemuan()
        return render_template('pertemuan_index.html', data=data)

    @staticmethod
    def mhs_index():
        data = PertemuanModel().all_mhspertemuan()
        return render_template('pertemuanMhs_index.html', data=data)

    @staticmethod
    def dsn_index():
        data = PertemuanModel().all_dsnpertemuan()
        return render_template('pertemuanDsn_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('pertemuan_create.html')
    
    @staticmethod
    def store():
        pertemuan_obj = PertemuanModel()
        post = request.form
        pertemuan_obj.dosen_id = post['dosen_id']
        pertemuan_obj.mhs_id = post['mhs_id']
        pertemuan_obj.hari = post['hari']
        pertemuan_obj.waktu = post['waktu']
        pertemuan_obj.jenis = post['jenis']
        pertemuan_obj.absensi = post['absensi']
        PertemuanModel().store_pertemuan(pertemuan_obj)
        return redirect('/pertemuan')

    @staticmethod
    def edit(pertemuan_id):
        obj = PertemuanModel().find_pertemuan(pertemuan_id)
        if obj:
            return render_template('pertemuan_edit.html', obj=obj)
        else:
            return "pertemuan not found", 404
    
    @staticmethod
    def update(pertemuan_id):
        data = PertemuanModel().find_pertemuan(pertemuan_id)
        if data:
            post = request.form
            pertemuan_obj = PertemuanModel()
            pertemuan_obj.dosen_id= post['dosen_id']
            pertemuan_obj.mhs_id = post['mhs_id']
            pertemuan_obj.hari= post['hari']
            pertemuan_obj.waktu = post['waktu']
            pertemuan_obj.jenis= post['jenis']
            pertemuan_obj.absensi = post['absensi']
            PertemuanModel().update_pertemuan(pertemuan_id, pertemuan_obj)
            return redirect('/pertemuan')
        else:
            return "pertemuan not found", 404
        
    @staticmethod
    def delete(pertemuan_id):
        data = PertemuanModel().find_pertemuan(pertemuan_id)
        if data:
            PertemuanModel().delete_pertemuan(pertemuan_id)
            return redirect('/pertemuan')
        else:
            return "pertemuan not found", 404
