import random

angka_benar = random.randint(11, 20)
kesempatan = 3

print("Selamat datang di permainan Tebak Angka!")
print("Anda harus menebak angka dalam range 11-20.")
print(f"Anda memiliki {kesempatan} kesempatan untuk menebak.")

for i in range(kesempatan):
    tebakan = int(input(f"Masukkan tebakan anda (kesempatan {i+1}): "))

    if tebakan == angka_benar:
        print("Angka yang anda masukkan BENAR!!")
        break
    else:
        print("Angka yang anda masukkan SALAH!!")
    
    if i == kesempatan - 1:
        print(f"Kesempatan kamu sudah habis :( Angka yang benar adalah {angka_benar}.")
