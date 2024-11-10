from flask import render_template, request, redirect
from modules.admin.AdminModel import AdminModel

class AdminView:

    @staticmethod
    def index():
        data = AdminModel().all_adm()
        print(data)
        return render_template('admin_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('admin_create.html')
    
    @staticmethod
    def store():
        admin_obj = AdminModel()
        post = request.form
        admin_obj.id_user= post['id_user']
        AdminModel().store(admin_obj)
        return redirect('/admin')

    @staticmethod
    def edit(admin_id):
        obj = AdminModel().find(admin_id)
        if obj:
            return render_template('admin_edit.html', obj=obj)
        else:
            return "admin not found", 404
    
    @staticmethod
    def update(admin_id):
        data = AdminModel().find(admin_id)
        if data:
            post = request.form
            admin_obj = AdminModel()
            admin_obj.id_user= post['id_user']
            AdminModel().update(admin_id, admin_obj)
            return redirect('/admin')
        else:
            return "admin not found", 404
        
    @staticmethod
    def delete(admin_id):
        data = AdminModel().find(admin_id)
        if data:
            AdminModel().delete(admin_id)
            return redirect('/admin')
        else:
            return "admin not found", 404
