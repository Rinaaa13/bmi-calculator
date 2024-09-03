def calculate():
    try:
        angka_1 = float(input("Masukkan angka pertama: "))
        angka_2 = float(input("Masukkan angka kedua  : "))

        operasi = input(
            """Operasi matematika yang didukung:
    + untuk penjumlahan
    - untuk pengurangan
    * untuk perkalian
    / untuk pembagian
    ** untuk pangkat
Silahkan pilih operasi matematika: """
        )
        if operasi == "+":
            print("{} + {} = ".format(angka_1, angka_2))
            print(angka_1 + angka_2)
        elif operasi == "-":
            print("{} - {} = ".format(angka_1, angka_2))
            print(angka_1 - angka_2)
        elif operasi == "*":
            print("{} * {} = ".format(angka_1, angka_2))
            print(angka_1 * angka_2)
        elif operasi == "/":
            try:
                print("{} / {} = ".format(angka_1, angka_2))
                print(angka_1 / angka_2)
            except ZeroDivisionError:
                print("Error: Tidak bisa membagi dengan nol.")
        elif operasi == "**":
            print("{} ** {} = ".format(angka_1, angka_2))
            print(angka_1 ** angka_2)
        else:
            print("Operasi yang kamu masukkan tidak didukung. Harap coba sekali lagi.")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

    again()

def again():
    lagi = input("Apakah kamu ingin melakukan kalkulasi lagi (Y/T)? ")

    if lagi.upper() == "Y":
        calculate()
    elif lagi.upper() == "T":
        print("Terima kasih. Sampai jumpa")
    else:
        again()

calculate()