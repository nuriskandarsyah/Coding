import math

print("Program Menghitung Luas dan Volume Silinder")

#Programmer  : Nur Iskandar S
#NIM         : 220511009
#Pertemuan   : 1
#Tanggal     : 22 Oktober 2023

#input nilai
jari_jari = float(input("Masukkan jari-jari silinder: "))
tinggi = float(input("Masukkan tinggi silinder: "))

#rumus
luas_lingkaran = math.pi * jari_jari ** 2
luas_selimut = 2 * math.pi * jari_jari * tinggi
luas = 2 * luas_lingkaran + luas_selimut
volume = luas_lingkaran * tinggi

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")
