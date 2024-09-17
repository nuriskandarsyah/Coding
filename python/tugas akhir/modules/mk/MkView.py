from flask import render_template, request, redirect
from modules.mk.MkModel import MkModel

class MkView:

    @staticmethod
    def index():
        data = MkModel().all()
        return render_template('mk_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('mk_create.html')
    
    @staticmethod
    def store():
        mk_obj = MkModel()
        post = request.form
        mk_obj.matkul = post['matkul']
        MkModel().store(mk_obj)
        return redirect('/mk')

    @staticmethod
    def edit(mk_id):
        obj = MkModel().find(mk_id)
        if obj:
            return render_template('mk_edit.html', obj=obj)
        else:
            return "mk not found", 404
    
    @staticmethod
    def update(mk_id):
        data = MkModel().find(mk_id)
        if data:
            post = request.form
            mk_obj = MkModel()
            mk_obj.matkul = post['matkul']
            MkModel().update(mk_id, mk_obj)
            return redirect('/mk')
        else:
            return "mk not found", 404
        
    @staticmethod
    def delete(mk_id):
        data = MkModel().find(mk_id)
        if data:
            MkModel().delete(mk_id)
            return redirect('/mk')
        else:
            return "mk not found", 404
