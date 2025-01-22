import json

# Data produk di gudang
produk = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nSistem Manajemen Produk di Gudang")
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Cari Produk")
    print("4. Hapus Produk")
    print("5. Simpan Data ke File")
    print("6. Muat Data dari File")
    print("7. Keluar")

# Fungsi untuk menambah produk
def tambah_produk():
    nama = input("Masukkan nama produk: ")
    jumlah = int(input("Masukkan jumlah produk: "))
    lokasi = input("Masukkan lokasi produk: ")
    produk.append({"nama": nama, "jumlah": jumlah, "lokasi": lokasi})
    print(f"Produk '{nama}' berhasil ditambahkan.")

# Fungsi untuk melihat daftar produk
def lihat_produk():
    if not produk:
        print("Belum ada produk di gudang.")
    else:
        print("\nDaftar Produk:")
        for i, p in enumerate(produk, 1):
            print(f"{i}. Nama: {p['nama']}, Jumlah: {p['jumlah']}, Lokasi: {p['lokasi']}")

# Fungsi untuk mencari produk
def cari_produk():
    nama = input("Masukkan nama produk yang dicari: ")
    hasil = [p for p in produk if p['nama'].lower() == nama.lower()]
    if hasil:
        for p in hasil:
            print(f"Ditemukan: Nama: {p['nama']}, Jumlah: {p['jumlah']}, Lokasi: {p['lokasi']}")
    else:
        print(f"Produk dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk menghapus produk
def hapus_produk():
    nama = input("Masukkan nama produk yang akan dihapus: ")
    global produk
    produk_baru = [p for p in produk if p['nama'].lower() != nama.lower()]
    if len(produk_baru) < len(produk):
        produk = produk_baru
        print(f"Produk '{nama}' berhasil dihapus.")
    else:
        print(f"Produk dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk menyimpan data ke file
def simpan_data():
    with open("data_produk.json", "w") as file:
        json.dump(produk, file)
    print("Data produk berhasil disimpan ke file 'data_produk.json'.")

# Fungsi untuk memuat data dari file
def muat_data():
    global produk
    try:
        with open("data_produk.json", "r") as file:
            produk = json.load(file)
        print("Data produk berhasil dimuat dari file 'data_produk.json'.")
    except FileNotFoundError:
        print("File 'data_produk.json' tidak ditemukan.")
    except json.JSONDecodeError:
        print("File 'data_produk.json' rusak atau tidak dapat dibaca.")

# Program utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            cari_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            simpan_data()
        elif pilihan == "6":
            muat_data()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
