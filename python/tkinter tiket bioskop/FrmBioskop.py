# FrmBioskop.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QCalendarWidget
from Bioskop import Bioskop

class FormBioskop(QMainWindow):

    MAX_SEATS = 100

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Data Bioskop")
        self.setGeometry(100, 100, 600, 400)
        self.ditemukan = None
        self.kursi_dipesan = set()
        self.setupUI()
        self.onReload()

    def setupUI(self):
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        layoutUtama = QVBoxLayout()
        mainWidget.setLayout(layoutUtama)

        # Form Input Data
        formLayout = QVBoxLayout()
        layoutUtama.addLayout(formLayout)

        formLayout.addWidget(QLabel('Nomer Transaksi:'))
        self.txtNomer_Transaksi = QLineEdit()
        formLayout.addWidget(self.txtNomer_Transaksi)

        formLayout.addWidget(QLabel('Nama:'))
        self.txtNama = QLineEdit()
        formLayout.addWidget(self.txtNama)

        formLayout.addWidget(QLabel('Nomer Kursi:'))
        self.txtNomer_Kursi = QLineEdit()
        formLayout.addWidget(self.txtNomer_Kursi)

        formLayout.addWidget(QLabel('Tanggal:'))
        self.calTanggal = QCalendarWidget()
        self.calTanggal.clicked.connect(self.updateHarga)
        formLayout.addWidget(self.calTanggal)

        formLayout.addWidget(QLabel('Harga:'))
        self.txtHarga = QLineEdit()
        self.txtHarga.setReadOnly(True)
        formLayout.addWidget(self.txtHarga)

        formLayout.addWidget(QLabel('Jumlah Tiket:'))
        self.txtJumlah_Tiket = QLineEdit()
        self.txtJumlah_Tiket.textChanged.connect(self.updateTotalBayar)
        formLayout.addWidget(self.txtJumlah_Tiket)

        formLayout.addWidget(QLabel('Total Bayar:'))
        self.txtTotal_Bayar = QLineEdit()
        self.txtTotal_Bayar.setReadOnly(True)
        formLayout.addWidget(self.txtTotal_Bayar)

        buttonLayout = QHBoxLayout()
        layoutUtama.addLayout(buttonLayout)

        self.btnSimpan = QPushButton('Simpan')
        self.btnSimpan.clicked.connect(self.onSimpan)
        buttonLayout.addWidget(self.btnSimpan)

        self.btnClear = QPushButton('Clear')
        self.btnClear.clicked.connect(self.onClear)
        buttonLayout.addWidget(self.btnClear)

        self.btnHapus = QPushButton('Hapus')
        self.btnHapus.clicked.connect(self.onDelete)
        buttonLayout.addWidget(self.btnHapus)

        # Tabel Data
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Nomer_Transaksi', 'Nama', 'Nomer_Kursi', 'Tgl', 'Harga', 'Jumlah_Tiket', 'Total_Bayar'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        layoutUtama.addWidget(self.tableWidget)

    def onReload(self):
        tanggal = self.calTanggal.selectedDate().toString('yyyy-MM-dd')
        bioskop = Bioskop()
        kursi_dipesan = bioskop.getKursiDipesanByTanggal(tanggal)
        self.kursi_dipesan = kursi_dipesan

        result = bioskop.getAllData()
        self.tableWidget.setRowCount(0)
        for row_data in result:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for column, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, column, item)

    def onSimpan(self):
        Nomer_Transaksi = self.txtNomer_Transaksi.text()
        Nama = self.txtNama.text()
        Nomer_Kursi = self.txtNomer_Kursi.text().strip()
        Tgl = self.calTanggal.selectedDate().toString('yyyy-MM-dd')
        Jumlah_Tiket = self.txtJumlah_Tiket.text()
        Total_Bayar = self.txtTotal_Bayar.text()

        if not Nomer_Transaksi or not Nama or not Nomer_Kursi or not Tgl or not Jumlah_Tiket or not Total_Bayar:
            QMessageBox.warning(self, "Peringatan", "Harap lengkapi semua kolom input.")
            return

        if Nomer_Kursi in self.kursi_dipesan:
            QMessageBox.warning(self, "Peringatan", f"Nomer Kursi {Nomer_Kursi} sudah dipesan pada tanggal yang sama.")
            return

        bioskop = Bioskop()
        bioskop.Nomer_Transaksi = Nomer_Transaksi
        bioskop.Nama = Nama
        bioskop.Nomer_Kursi = Nomer_Kursi
        bioskop.Tgl = Tgl
        bioskop.Harga = self.txtHarga.text()
        bioskop.Jumlah_Tiket = Jumlah_Tiket
        bioskop.Total_Bayar = Total_Bayar

        res = bioskop.simpan()

        if res > 0:
            QMessageBox.information(self, "Informasi", "Data Berhasil Disimpan")
            self.onReload()
            self.onClear()
        else:
            QMessageBox.warning(self, "Peringatan", "Gagal menyimpan data")

    def onDelete(self):
        Nomer_Transaksi = self.txtNomer_Transaksi.text()

        bioskop = Bioskop()
        res = bioskop.deleteByNomer_Transaksi(Nomer_Transaksi)

        if res > 0:
            QMessageBox.information(self, "Informasi", "Data Berhasil Dihapus")
            self.onReload()
            self.onClear()
        else:
            QMessageBox.warning(self, "Peringatan", "Gagal menghapus data")

    def onClear(self):
        self.txtNomer_Transaksi.clear()
        self.txtNama.clear()
        self.txtNomer_Kursi.clear()
        self.txtJumlah_Tiket.clear()
        self.txtHarga.clear()
        self.txtTotal_Bayar.clear()

    def updateHarga(self):
        tanggal = self.calTanggal.selectedDate().toString('yyyy-MM-dd')
        if not tanggal:
            QMessageBox.warning(self, "Peringatan", "Harap pilih tanggal.")
            return

        bioskop = Bioskop()
        kursi_dipesan = bioskop.getKursiDipesanByTanggal(tanggal)
        self.kursi_dipesan = kursi_dipesan

        nomor_kursi = self.txtNomer_Kursi.text().strip()
        if nomor_kursi in kursi_dipesan:
            QMessageBox.warning(self, "Peringatan", f"Nomer Kursi {nomor_kursi} sudah dipesan pada tanggal tersebut.")
            return
        
        harga_default = 35000
        hari = self.calTanggal.selectedDate().dayOfWeek()
        if hari >= 5:
            harga_default = 50000

        self.txtHarga.setText(str(harga_default))
        self.updateTotalBayar()

    def updateTotalBayar(self):
        jumlah_tiket = self.txtJumlah_Tiket.text()
        harga = self.txtHarga.text()
        if jumlah_tiket and harga:
            total_bayar = int(jumlah_tiket) * int(harga)
            self.txtTotal_Bayar.setText(str(total_bayar))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    formBioskop = FormBioskop()
    formBioskop.show()
    sys.exit(app.exec_())

