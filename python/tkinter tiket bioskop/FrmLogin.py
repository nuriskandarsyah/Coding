import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Users import Users
from Dashboard import Dashboard

class FormLogin(QWidget):
    def __init__(self, update_main_window):
        super().__init__()
        self.update_main_window = update_main_window
        self.setWindowTitle("Aplikasi Data Login")
        self.setGeometry(100, 100, 250, 150)
        self.setupUI()

    def setupUI(self):
        self.setStyleSheet("background-color: white;")

        label_username = QLabel('Username:', self)
        label_username.setGeometry(20, 20, 80, 20)
        label_password = QLabel('Password:', self)
        label_password.setGeometry(20, 50, 80, 20)

        self.txtusername = QLineEdit(self)
        self.txtusername.setGeometry(100, 20, 120, 20)
        self.txtpassword = QLineEdit(self)
        self.txtpassword.setGeometry(100, 50, 120, 20)
        self.txtpassword.setEchoMode(QLineEdit.Password)

        btnSubmit = QPushButton('Submit', self)
        btnSubmit.setGeometry(20, 90, 100, 30)
        btnSubmit.clicked.connect(self.onSubmit)

        btnCancel = QPushButton('Cancel', self)
        btnCancel.setGeometry(130, 90, 100, 30)
        btnCancel.clicked.connect(self.close)

        # Ganti font
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        label_username.setFont(font)
        label_password.setFont(font)
        self.txtusername.setFont(font)
        self.txtpassword.setFont(font)
        btnSubmit.setFont(font)
        btnCancel.setFont(font)

    def onSubmit(self):
        username = self.txtusername.text()
        password = self.txtpassword.text()

        obj = Users()
        if obj.login(username, password):
            self.update_main_window(True)
            self.close()
            self.showDashboard()
            QMessageBox.information(self, "Login Berhasil", "Login berhasil!")
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah!")
            print("Percobaan gagal:", obj.validation)

    def showDashboard(self): 
        self.dashboard = Dashboard()
        self.dashboard.show()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    app = QApplication(sys.argv)
    form_login = FormLogin(update_main_window)
    form_login.show()
    sys.exit(app.exec_())
