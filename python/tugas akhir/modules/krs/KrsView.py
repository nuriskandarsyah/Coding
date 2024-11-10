from flask import render_template, request, redirect
from modules.krs.KrsModel import KrsModel

class KrsView:

    @staticmethod
    def index():
        data = KrsModel().all_mhs()
        return render_template('krs_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('krs_create.html')
    
    @staticmethod
    def store():
        krs_obj = KrsModel()
        post = request.form
        krs_obj.jdwl_id= post['jdwl_id']
        KrsModel().store(krs_obj)
        return redirect('/krs')

    @staticmethod
    def edit(krs_id):
        obj = KrsModel().find(krs_id)
        if obj:
            return render_template('krs_create.html', obj=obj)
        else:
            return "Krs not found", 404
    
    @staticmethod
    def update(krs_id):
        data = KrsModel().find(krs_id)
        if data:
            post = request.form
            krs_obj = KrsModel()
            krs_obj.jdwl_id= post['jdwl_id']
            KrsModel().update(krs_id, krs_obj)
            return redirect('/krs')
        else:
            return "Krs not found", 404
        
    @staticmethod
    def delete(krs_id):
        data = KrsModel().find(krs_id)
        if data:
            KrsModel().delete(krs_id)
            return redirect('/krs')
        else:
            return "Krs not found", 404