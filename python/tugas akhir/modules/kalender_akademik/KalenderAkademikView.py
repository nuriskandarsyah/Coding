from flask import render_template, request, redirect
from modules.kalender_akademik.KalenderAkademikModel import KalenderAkademikModel

class KalenderAkademikView:

    @staticmethod
    def index():
        data = KalenderAkademikModel().all()
        return render_template('kk_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('kk_create.html')
    
    @staticmethod
    def store():
        kalender_akademik_obj = KalenderAkademikModel()
        post = request.form
        kalender_akademik_obj.kegiatan= post['kegiatan']
        kalender_akademik_obj.waktu = post['waktu']
        KalenderAkademikModel().store(kalender_akademik_obj)
        return redirect('/kalender_akademik')

    @staticmethod
    def edit(kk_id):
        obj = KalenderAkademikModel().find(kk_id)
        if obj:
            return render_template('kk_edit.html', obj=obj)
        else:
            return "Kalender Akademik not found", 404
    
    @staticmethod
    def update(kk_id):
        data = KalenderAkademikModel().find(kk_id)
        if data:
            post = request.form
            kalender_akademik_obj = KalenderAkademikModel()
            kalender_akademik_obj.kegiatan= post['kegiatan']
            kalender_akademik_obj.waktu = post['waktu']
            KalenderAkademikModel().update(kk_id, kalender_akademik_obj)
            return redirect('/kalender_akademik')
        else:
            return "Kalender Akademik not found", 404
        
    @staticmethod
    def delete(kk_id):
        data = KalenderAkademikModel().find(kk_id)
        if data:
            KalenderAkademikModel().delete(kk_id)
            return redirect('/kalender_akademik')
        else:
            return "kalender_akademik not found", 404
