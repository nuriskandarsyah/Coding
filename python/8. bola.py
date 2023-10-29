import math

print("Program Menghitung Luas dan Volume Bola")

#Programmer  : Nur Iskandar S
#NIM         : 220511009
#Pertemuan   : 1
#Tanggal     : 22 Oktober 2023


#input nilai
jari_jari = float(input("Masukkan jari-jari bola: "))

# rumus
luas = 4 * math.pi * jari_jari ** 2
volume = (4/3) * math.pi * jari_jari ** 3

# output
print(f"Luas: {luas}")
print(f"Volume: {volume}")
