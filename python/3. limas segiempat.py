import math

print("Program Menghitung Luas dan Volume Limas Segiempat")

#Programmer  : Nur Iskandar S
#NIM         : 220511009
#Pertemuan   : 1
#Tanggal     : 22 Oktober 2023

#input nilai
alas = float(input("Masukkan panjang sisi alas limas segiempat: "))
tinggi = float(input("Masukkan tinggi limas segiempat: "))
sisi_tegak = float(input("Masukkan panjang sisi tegak limas segiempat: "))

#rumus
luas_alas = alas * alas
luas_tegak = 4 * (alas * sisi_tegak) / 2
luas = 4 * (alas * sisi_tegak / 2) + luas_alas
volume = (luas_alas * tinggi) / 3

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")
