# ================================
#   Kalkulator Sederhana - Python
# ================================

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi dengan nol!"
    return a / b


def tampilkan_menu():
    print("\n╔══════════════════════════╗")
    print("║   🧮 KALKULATOR SEDERHANA  ║")
    print("╠══════════════════════════╣")
    print("║  1. Penjumlahan  ( + )   ║")
    print("║  2. Pengurangan  ( - )   ║")
    print("║  3. Perkalian    ( × )   ║")
    print("║  4. Pembagian    ( ÷ )   ║")
    print("║  5. Keluar               ║")
    print("╚══════════════════════════╝")


def minta_angka(label):
    while True:
        try:
            return float(input(f"  Masukkan {label}: "))
        except ValueError:
            print("  ⚠️  Tolong masukkan angka yang valid!")


def jalankan_kalkulator():
    print("\nSelamat datang di Kalkulator Sederhana!")

    while True:
        tampilkan_menu()
        pilihan = input("\nPilih operasi (1-5): ").strip()

        if pilihan == "5":
            print("\nTerima kasih sudah menggunakan kalkulator ini! 👋\n")
            break

        if pilihan not in ["1", "2", "3", "4"]:
            print("⚠️  Pilihan tidak valid. Silakan pilih angka 1-5.")
            continue

        angka1 = minta_angka("angka pertama")
        angka2 = minta_angka("angka kedua")

        if pilihan == "1":
            hasil = tambah(angka1, angka2)
            operasi = "+"
        elif pilihan == "2":
            hasil = kurang(angka1, angka2)
            operasi = "-"
        elif pilihan == "3":
            hasil = kali(angka1, angka2)
            operasi = "×"
        elif pilihan == "4":
            hasil = bagi(angka1, angka2)
            operasi = "÷"

        print(f"\n  ✅ {angka1} {operasi} {angka2} = {hasil}")


# Titik masuk program
if __name__ == "__main__":
    jalankan_kalkulator()
