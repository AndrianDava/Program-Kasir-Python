import datetime
import random
import string

# Dictionary untuk menyimpan daftar barang dan harganya
barang = {
    "Pensil": 1500,
    "Penghapus": 1000,
    "Penggaris": 2000,
    "Buku Tulis": 5000,
    "Pensil Warna": 3000,
    "Spidol": 4000,
    "Stapler": 10000,
    "Sticky Notes": 3000,
    "Kertas HVS": 15000,
    "Map Plastik": 2000
}

# Menampilkan daftar barang
def tampilkan_barang():
    print("Daftar Barang ATK:")
    for item, harga in barang.items():
        print(item, ":", harga)

# Menghitung total harga pesanan
def hitung_total(pesanan):
    total = 0
    for item, jumlah in pesanan.items():
        if item in barang:
            total += barang[item] * jumlah
        else:
            print("Barang", item, "tidak tersedia.")
    return total

# Mencetak struk belanjaan
def cetak_struk(pesanan, total_harga, nama_kasir, id_pesanan, waktu_pembelian):
    print("\n===== Struk Belanja =====")
    print("ID Pesanan:", id_pesanan)
    print("Tanggal Pembelian:", waktu_pembelian.strftime("%Y-%m-%d %H:%M:%S"))
    print("Kasir:", nama_kasir)
    print("Pesanan:")
    for item, jumlah in pesanan.items():
        print("-", item, "x", jumlah)
    print("Total harga yang harus dibayar:", total_harga)
    print("=========================")

# Membuat ID pesanan secara acak
def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Membuat barcode secara acak
def generate_random_barcode():
    return ''.join(random.choices(string.digits, k=10))

# Meminta jumlah barang yang dipesan
def masukkan_jumlah(item):
    while True:
        try:
            jumlah = int(input("Masukkan jumlah {} yang ingin Anda pesan: ".format(item)))
            if jumlah > 0:
                return jumlah
            else:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Masukkan jumlah dalam angka.")

# Memeriksa keberadaan ID pesanan
def cek_id_pesanan(daftar_pesanan, id_pesanan):
    return any(pesanan['id_pesanan'] == id_pesanan for pesanan in daftar_pesanan)

# Memeriksa pesanan berdasarkan ID
def cek_pesanan_by_id(daftar_pesanan, id_pesanan):
    for pesanan in daftar_pesanan:
        if pesanan['id_pesanan'] == id_pesanan:
            return pesanan
    return None

# Fungsi utama
def main():
    daftar_pesanan = []

    while True:
        print("\nMenu:")
        print("1. Tampilkan Barang")
        print("2. Pesan Barang")
        print("3. Cek ID Pesanan")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            pesanan = {}
            while True:
                item = input("Masukkan barang yang ingin Anda pesan (kosongkan untuk selesai): ")
                if not item:
                    break
                if item in barang:
                    jumlah = masukkan_jumlah(item)
                    pesanan[item] = jumlah
                else:
                    print("Barang", item, "tidak tersedia.")

            total_harga = hitung_total(pesanan)
            nama_kasir = input("Masukkan nama kasir: ")
            waktu_pembelian = datetime.datetime.now()
            id_pesanan = generate_random_id()
            barcode = generate_random_barcode()

            if cek_id_pesanan(daftar_pesanan, id_pesanan):
                print("ID pesanan sudah digunakan. Silakan coba lagi.")
            else:
                daftar_pesanan.append({'id_pesanan': id_pesanan, 'pesanan': pesanan, 'total_harga': total_harga, 'waktu_pembelian': waktu_pembelian, 'barcode': barcode})
                cetak_struk(pesanan, total_harga, nama_kasir, id_pesanan, waktu_pembelian)
        elif pilihan == "3":
            id_pesanan = input("Masukkan ID Pesanan yang ingin Anda cek: ")
            pesanan = cek_pesanan_by_id(daftar_pesanan, id_pesanan)
            if pesanan:
                print("Pesanan dengan ID", id_pesanan, "ditemukan:")
                print("Pesanan:", pesanan['pesanan'])
                print("Total harga:", pesanan['total_harga'])
            else:
                print("Pesanan dengan ID", id_pesanan, "tidak ditemukan.")
        elif pilihan == "4":
            print("Terima kasih! Program akan keluar.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
