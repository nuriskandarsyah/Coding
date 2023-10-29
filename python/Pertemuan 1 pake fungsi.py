print("Program Menghitung Luas Permukaan dan Volume Bangun Ruang")

#Programmer : Nur Iskandar S
#NIM        : 220511009
#Pertemuan  : 1
#Tanggal    : 22 Oktober 2023 

import math

# menghitung luas kubus
def hitung_luas_kubus(sisi):
    return 6 * sisi ** 2

# menghitung volume kubus
def hitung_volume_kubus(sisi):
    return sisi ** 3

# menghitung luas balok
def hitung_luas_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# menghitung luas limas segiempat
def hitung_luas_limas_segiempat(alas, tinggi, sisi_tegak):
    luas_alas = alas * alas
    luas_tegak = 4 * (alas * sisi_tegak) / 2
    return luas_alas + luas_tegak

# menghitung volume limas segiempat
def hitung_volume_limas_segiempat(alas, tinggi, sisi_tegak):
    luas_alas = alas * alas
    return (luas_alas * tinggi) / 3

# menghitung luas prisma segitiga
def hitung_luas_prisma_segitiga(alas, tinggi, sisi_tegak):
    luas_alas = 0.5 * alas * tinggi
    luas_tegak = 3 * (alas * sisi_tegak)
    return 2 * luas_alas + luas_tegak

# menghitung volume prisma segitiga
def hitung_volume_prisma_segitiga(alas, tinggi, sisi_tegak):
    luas_alas = 0.5 * alas * tinggi
    return luas_alas * sisi_tegak

# menghitung luas limas segitiga
def hitung_luas_limas_segitiga(alas, tinggi, sisi_tegak):
    luas_alas = 0.5 * alas * tinggi
    luas_tegak = 3 * (alas * sisi_tegak) / 2
    return luas_alas + luas_tegak

# menghitung volume limas segitiga
def hitung_volume_limas_segitiga(alas, tinggi, sisi_tegak):
    luas_alas = 0.5 * alas * tinggi
    return (luas_alas * tinggi) / 3

# menghitung luas silinder
def hitung_luas_silinder(jari_jari, tinggi):
    luas_lingkaran = math.pi * jari_jari ** 2
    luas_selimut = 2 * math.pi * jari_jari * tinggi
    return 2 * luas_lingkaran + luas_selimut

# menghitung volume silinder
def hitung_volume_silinder(jari_jari, tinggi):
    luas_lingkaran = math.pi * jari_jari ** 2
    return luas_lingkaran * tinggi

# menghitung luas kerucut
def hitung_luas_kerucut(jari_jari, tinggi, sisi_miring):
    luas_lingkaran = math.pi * jari_jari ** 2
    luas_selimut = math.pi * jari_jari * sisi_miring
    return luas_lingkaran + luas_selimut

# menghitung volume kerucut
def hitung_volume_kerucut(jari_jari, tinggi):
    luas_lingkaran = math.pi * jari_jari ** 2
    return (luas_lingkaran * tinggi) / 3

# menghitung luas bola
def hitung_luas_bola(jari_jari):
    return 4 * math.pi * jari_jari ** 2

# menghitung volume bola
def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

# Pilihan bangun ruang
print("Pilih bangun ruang yang ingin dihitung:")
print("1. Kubus")
print("2. Balok")
print("3. Limas Segiempat")
print("4. Prisma Segitiga")
print("5. Limas Segitiga")
print("6. Silinder")
print("7. Kerucut")
print("8. Bola")

pilihan = input("Masukkan nomor pilihan (1/2/3/4/5/6/7/8): ")

# Input nilai-nilai yang diperlukan
if pilihan in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    if pilihan == "1":
        sisi = float(input("Masukkan panjang sisi kubus: "))
        luas = hitung_luas_kubus(sisi)
        volume = hitung_volume_kubus(sisi)
    elif pilihan == "2":
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        luas = hitung_luas_balok(panjang, lebar, tinggi)
        volume = hitung_volume_balok(panjang, lebar, tinggi)
    elif pilihan == "3":
        alas = float(input("Masukkan panjang sisi alas limas segiempat: "))
        tinggi = float(input("Masukkan tinggi limas segiempat: "))
        sisi_tegak = float(input("Masukkan panjang sisi tegak limas segiempat: "))
        luas = hitung_luas_limas_segiempat(alas, tinggi, sisi_tegak)
        volume = hitung_volume_limas_segiempat(alas, tinggi, sisi_tegak)
    elif pilihan == "4":
        alas = float(input("Masukkan panjang sisi alas prisma segitiga: "))
        tinggi = float(input("Masukkan tinggi prisma segitiga: "))
        sisi_tegak = float(input("Masukkan panjang sisi tegak prisma segitiga: "))
        luas = hitung_luas_prisma_segitiga(alas, tinggi, sisi_tegak)
        volume = hitung_volume_prisma_segitiga(alas, tinggi, sisi_tegak)
    elif pilihan == "5":
        alas = float(input("Masukkan panjang sisi alas limas segitiga: "))
        tinggi = float(input("Masukkan tinggi limas segitiga: "))
        sisi_tegak = float(input("Masukkan panjang sisi tegak limas segitiga: "))
        luas = hitung_luas_limas_segitiga(alas, tinggi, sisi_tegak)
        volume = hitung_volume_limas_segitiga(alas, tinggi, sisi_tegak)
    elif pilihan == "6":
        jari_jari = float(input("Masukkan jari-jari silinder: "))
        tinggi = float(input("Masukkan tinggi silinder: "))
        luas = hitung_luas_silinder(jari_jari, tinggi)
        volume = hitung_volume_silinder(jari_jari, tinggi)
    elif pilihan == "7":
        jari_jari = float(input("Masukkan jari-jari kerucut: "))
        tinggi = float(input("Masukkan tinggi kerucut: "))
        sisi_miring = 1 / 3 * (jari_jari ** 2 + tinggi ** 2)
        luas = hitung_luas_kerucut(jari_jari, tinggi, sisi_miring)
        volume = hitung_volume_kerucut(jari_jari, tinggi)
    elif pilihan == "8":
        jari_jari = float(input("Masukkan jari-jari bola: "))
        luas = hitung_luas_bola(jari_jari)
        volume = hitung_volume_bola(jari_jari)

    # Output hasil perhitungan
    print(f"Luas: {luas}")
    print(f"Volume: {volume}")
else:
    print("Pilihan tidak valid. Masukkan nomor pilihan yang benar (1/2/3/4/5/6/7/8).")
