print("Konversi Suhu Fahrenheit")

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")

# Rumus
C = (5/9) * (float(suhu) - 32)
R = (4/9) * (float(suhu) - 32)
K = (5/9) * (float(suhu) - 32) + 273

# Output
print(suhu + " Fahrenheit sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
