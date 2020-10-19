#Fungsi Penjumlahan
def penjumlahan(x, y):
    return x + y

#Fungsi Pengurangan
def pengurangan(x, y):
    return x - y

#Fungsi Perkalian
def perkalian(x, y):
    return x * y

#Fungsi Pembagian
def pembagian(x, y):
    return x / y

confirm = "y"

while confirm == "y":

    # Menu Operasi
    print("Pilih Operasi.")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    # Meminta input operasi dan bilangan dari user
    pilihan = input("Masukkan Pilihan (1/2/3/4) : ")
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))

    #Logic Kalkulator
    if pilihan == "1":
        print(bil1, "+", bil2, "=", penjumlahan(bil1, bil2))
    elif pilihan == "2":
        print(bil1, "-", bil2, "=", pengurangan(bil1, bil2))
    elif pilihan == "3":
        print(bil1, "*", bil2, "=", perkalian(bil1, bil2))
    elif pilihan == "4":
        print(bil1, "/", bil2, "=", pembagian(bil1, bil2))
    else:
        print("Input salah")

    # Meminta input user, mau coba lagi ndak
    confirm = input("Mau coba Lagi? (y/t) : ")

    if confirm == "t":
        break

# Selesai
print("Terima Kasih :D")