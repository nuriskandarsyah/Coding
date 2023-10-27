import math

print("Program Menghitung Luas dan Volume Prisma Segitiga")

#Programmer  : Nur Iskandar S
#NIM         : 220511009
#Pertemuan   : 1
#Tanggal     : 22 Oktober 2023

#input nilai
alas = float(input("Masukkan panjang sisi alas prisma segitiga: "))
tinggi = float(input("Masukkan tinggi prisma segitiga: "))
sisi_tegak = float(input("Masukkan panjang sisi tegak prisma segitiga: "))

#rumus
luas_alas = 1/2 * alas * tinggi
luas_tegak = 3 * (alas * sisi_tegak)
luas = 2 * luas_alas + luas_tegak
volume = luas_alas * sisi_tegak

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")