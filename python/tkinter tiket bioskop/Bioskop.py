from db import DBConnection as mydb
import mysql.connector as mysql

class Bioskop:
    def __init__(self):
        self.__id = None
        self.__Nomer_Transaksi = None
        self.__Nama = None
        self.__Nomer_Kursi = None
        self.__Tgl = None
        self.__Harga = None
        self.__Jumlah_Tiket = None
        self.__Total_Bayar = None
        self.conn = None
        self.affected = None
        self.result = None
    
    def getKursiDipesanByTanggal(self, tanggal):
        self.conn = mydb()
        sql = "SELECT Nomer_Kursi FROM freedb_iskandar.bioskop WHERE Tgl=%s"
        val = (tanggal,)
        result = self.conn.findAll(sql, val)
        self.conn.disconnect()
        # Mengubah tuple menjadi daftar string nomor kursi
        kursi_dipesan = [row[0] for row in result]
        return kursi_dipesan
    
    @property
    def id(self):
        return self.__id

    @property
    def Nomer_Transaksi(self):
        return self.__Nomer_Transaksi

    @Nomer_Transaksi.setter
    def Nomer_Transaksi(self, value):
        self.__Nomer_Transaksi = value

    @property
    def Nama(self):
        return self.__Nama

    @Nama.setter
    def Nama(self, value):
        self.__Nama = value

    @property
    def Nomer_Kursi(self):
        return self.__Nomer_Kursi

    @Nomer_Kursi.setter
    def Nomer_Kursi(self, value):
        self.__Nomer_Kursi = value

    @property
    def Tgl(self):
        return self.__Tgl

    @Tgl.setter
    def Tgl(self, value):
        self.__Tgl = value

    @property
    def Harga(self):
        return self.__Harga

    @Harga.setter
    def Harga(self, value):
        self.__Harga = value

    @property
    def Jumlah_Tiket(self):
        return self.__Jumlah_Tiket

    @Jumlah_Tiket.setter
    def Jumlah_Tiket(self, value):
        self.__Jumlah_Tiket = value

    @property
    def Total_Bayar(self):
        return self.__Total_Bayar

    @Total_Bayar.setter
    def Total_Bayar(self, value):
        self.__Total_Bayar = value

    def findOne(self, sql, val=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, val) 
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getHargaByTanggal(self, Nomer_Kursi, tanggal):
        self.conn = mydb()
        sql = "SELECT Harga FROM freedb_iskandar.bioskop WHERE Tgl=%s"
        val = (Nomer_Kursi, tanggal)
        self.result = self.conn.findOne(sql, val)
        self.conn.disconnect()
        if self.result:
            return self.result[0]
        else:
            return None

    def simpan(self):
        self.conn = mydb()
        val = (self.__Nomer_Transaksi, self.__Nama, self.__Nomer_Kursi, self.__Tgl, self.__Harga, self.__Jumlah_Tiket, self.__Total_Bayar)
        sql = "INSERT INTO freedb_iskandar.bioskop (Nomer_Transaksi, Nama, Nomer_Kursi, Tgl, Harga, Jumlah_Tiket, Total_Bayar) VALUES" + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__Nomer_Transaksi, self.__Nama, self.__Nomer_Kursi, self.__Tgl, self.__Harga, self.__Jumlah_Tiket, self.__Total_Bayar, id)
        sql = "UPDATE freedb_iskandar.bioskop SET Nomer_Transaksi = %s, Nama = %s, Nomer_Kursi = %s, Tgl = %s, Harga = %s, Jumlah_Tiket = %s, Total_Bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByNomer_Transaksi(self, Nomer_Transaksi):
        self.conn = mydb()
        val = (self.__Nama, self.__Nomer_Kursi, self.__Tgl, self.__Harga, self.__Jumlah_Tiket, self.__Total_Bayar, Nomer_Transaksi)
        sql = "UPDATE freedb_iskandar.bioskop SET Nama = %s, Nomer_Kursi = %s, Tgl = %s, Harga = %s, Jumlah_Tiket = %s, Total_Bayar = %s WHERE Nomer_Transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM freedb_iskandar.bioskop WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def deleteByNomer_Transaksi(self, Nomer_Transaksi):
        self.conn = mydb()
        sql = "DELETE FROM freedb_iskandar.bioskop WHERE Nomer_Transaksi='" + str(Nomer_Transaksi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM freedb_iskandar.bioskop WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__Nomer_Transaksi = self.result[1]
        self.__Nama = self.result[2]
        self.__Nomer_Kursi = self.result[3]
        self.__Tgl = self.result[4]
        self.__Harga = self.result[5]
        self.__Jumlah_Tiket = self.result[6]
        self.__Total_Bayar = self.result[7]
        self.conn.disconnect()
        return self.result

    def getByNomer_Transaksi(self, Nomer_Transaksi):
        a = str(Nomer_Transaksi)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM freedb_iskandar.bioskop WHERE Nomer_Transaksi=%s"
        self.result = self.conn.findOne(sql)
        if self.result:
            self.__id = self.result[0]
            self.__Nomer_Transaksi = self.result[1]
            self.__Nama = self.result[2]
            self.__Nomer_Kursi = self.result[3]
            self.__Tgl = self.result[4]
            self.__Harga = self.result[5]
            self.__Jumlah_Tiket = self.result[6]
            self.__Total_Bayar = self.result[7]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__id = ""
            self.__Nomer_Transaksi = ""
            self.__Nama = ""
            self.__Nomer_Kursi = ""
            self.__Tgl = ""
            self.__Harga = ""
            self.__Jumlah_Tiket = ""
            self.__Total_Bayar = ""
            self.affected = 0
        self.conn.disconnect()
        return self.result


    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM freedb_iskandar.bioskop"
        self.result = self.conn.findAll(sql)
        self.conn.disconnect()
        return self.result


A = Bioskop()
Nomer_Transaksi = '33567'
A.deleteByNomer_Transaksi(Nomer_Transaksi)
B = A.getAllData()
print(B)