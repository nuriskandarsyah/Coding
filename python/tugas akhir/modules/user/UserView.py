from flask import render_template, request, redirect, session
from modules.user.UserModel import UserModel

class UserView:

    @staticmethod
    def index():
        data = UserModel().all()
        return render_template('user_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('user_create.html')
    
    @staticmethod
    def store():
        user_obj = UserModel()
        post = request.form
        user_obj.username = post['username']
        user_obj.password = post['password']
        user_obj.role = post['role']
        user_obj.nama_lengkap = post['nama_lengkap']
        user_obj.alamat = post['alamat']
        user_obj.email = post['email']
        user_obj.nim = post['nim']
        user_obj.nidn = post['nidn']
        user_obj.jk = post['jk']
        UserModel().store(user_obj)
        return redirect('/user')

    @staticmethod
    def edit(id_user):
        obj = UserModel().find(id_user)
        if obj:
            return render_template('user_edit.html', obj=obj)
        else:
            return "User not found", 404
    
    @staticmethod
    def editMHS():
        id_user = session.get('id_user')
        if not id_user:
            return redirect('/')
        
        obj = UserModel().find(id_user)
        if obj:
            return render_template('user_editMHS.html', obj=obj)
        else:
            return "User not found", 404
    
    @staticmethod
    def editDSN():
        id_user = session.get('id_user')
        if not id_user:
            return redirect('/')
        
        obj = UserModel().find(id_user)
        if obj:
            return render_template('user_editDSN.html', obj=obj)
        else:
            return "User not found", 404
    
    @staticmethod
    def update(id_user):
        data = UserModel().find(id_user)
        if data:
            post = request.form
            user_obj = UserModel()
            user_obj.username = post['username']
            user_obj.password = post['password']
            user_obj.role = post['role']
            user_obj.nama_lengkap = post['nama_lengkap']
            user_obj.alamat = post['alamat']
            user_obj.email = post['email']
            user_obj.nim = post['nim']
            user_obj.nidn = post['nidn']
            user_obj.jk = post['jk']
            UserModel().update(id_user, user_obj)
            return redirect('/user')
        else:
            return "User not found", 404
    
    @staticmethod
    def updateMHS(id_user):
        data = UserModel().find(id_user)
        if data:
            post = request.form
            user_obj = UserModel()
            user_obj.username = post['username']
            user_obj.password = post['password']
            user_obj.nama_lengkap = post['nama_lengkap']
            user_obj.alamat = post['alamat']
            user_obj.email = post['email']
            user_obj.nim = post['nim']
            user_obj.jk = post['jk']
            UserModel().update(id_user, user_obj)
            return redirect('/')
        else:
            return "User not found", 404
    
    @staticmethod
    def updateDSN(id_user):
        data = UserModel().find(id_user)
        if data:
            post = request.form
            user_obj = UserModel()
            user_obj.username = post['username']
            user_obj.password = post['password']
            user_obj.nama_lengkap = post['nama_lengkap']
            user_obj.alamat = post['alamat']
            user_obj.email = post['email']
            user_obj.nidn = post['nidn']
            user_obj.jk = post['jk']
            UserModel().update(id_user, user_obj)
            return redirect('/')
        else:
            return "User not found", 404

    @staticmethod
    def delete(id_user):
        data = UserModel().find(id_user)
        if data:
            UserModel().delete(id_user)
            return redirect('/user')
        else:
            return "User not found", 404
