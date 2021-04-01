a = input("Masukkan Nama anda: ")
b = int(input("Masukkan Nilai anda: "))
nilai = b

if nilai >= 85 and nilai <= 100:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah A")
elif nilai >= 80 and nilai < 85 :
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75 and nilai < 80:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70 and nilai < 75:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah B")
elif nilai >= 65 and nilai < 70:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60 and nilai < 65:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah C")
elif nilai < 60:
    print("Halo", a +'!', "Nilai anda setelah dikonversi adalah E")
else:
    print("Halo", a +'!', "Nilai yang anda masukkan tidak valid")
print()