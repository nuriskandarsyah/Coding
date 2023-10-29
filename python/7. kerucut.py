import math

print("Program Menghitung Luas dan Volume Kerucut")

#Programmer  : Nur Iskandar S
#NIM         : 220511009
#Pertemuan   : 1
#Tanggal     : 22 Oktober 2023

#input nilai
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

#rumus
sisi_miring = 1 / 3 * (jari_jari ** 2 + tinggi ** 2)
luas_lingkaran = math.pi * jari_jari ** 2
luas_selimut = math.pi * jari_jari * sisi_miring
luas = luas_lingkaran + luas_selimut
volume = (luas_lingkaran * tinggi) / 3

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")
