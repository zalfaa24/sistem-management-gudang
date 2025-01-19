from collections import deque

class Produk:
    def __init__(self, kode, nama, kategori, stok, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.stok = stok
        self.harga = harga

def tambah_produk(produk_list, log_aktivitas):
    kode = "P001"
    nama = "Produk A"
    kategori = "Elektronik"
    stok = 10
    harga = 150000.0
    produk = Produk(kode, nama, kategori, stok, harga)
    produk_list.append(produk)
    log_aktivitas.append(f"Menambahkan produk: {kode}, {nama}")
    print("Produk berhasil ditambahkan: Kode=P001, Nama=Produk A, Kategori=Elektronik, Stok=10, Harga=150000.0")

def tampilkan_produk(produk_list):
    if not produk_list:
        print("Belum ada produk yang terdaftar.")
        return
    print("\nDaftar Produk:")
    for produk in produk_list:
        print(f"Kode: {produk.kode}, Nama: {produk.nama}, Kategori: {produk.kategori}, Stok: {produk.stok}, Harga: {produk.harga}")

def cari_produk(produk_list):
    keyword = "P001"
    hasil = [produk for produk in produk_list if keyword in produk.kode or keyword in produk.nama]
    if hasil:
        print("\nHasil Pencarian:")
        for produk in hasil:
            print(f"Kode: {produk.kode}, Nama: {produk.nama}, Kategori: {produk.kategori}, Stok: {produk.stok}, Harga: {produk.harga}")
    else:
        print("Produk tidak ditemukan.")

def hapus_produk(produk_list, log_aktivitas):
    kode = "P001"
    for produk in produk_list:
        if produk.kode == kode:
            produk_list.remove(produk)
            log_aktivitas.append(f"Menghapus produk: {kode}")
            print("Produk berhasil dihapus: Kode=P001")
            return
    print("Produk tidak ditemukan.")

def urutkan_produk(produk_list, log_aktivitas):
    produk_list.sort(key=lambda x: x.nama)
    log_aktivitas.append("Mengurutkan produk berdasarkan nama")
    print("Produk berhasil diurutkan.")

def tampilkan_log(log_aktivitas):
    if not log_aktivitas:
        print("Belum ada aktivitas yang dicatat.")
        return
    print("\nLog Aktivitas (Stack - LIFO):")
    while log_aktivitas:
        print(log_aktivitas.pop())

def antrian_pengiriman(queue_pengiriman):
    print("\nAntrian Pengiriman (Queue - FIFO):")
    while queue_pengiriman:
        print(queue_pengiriman.popleft())

def main():
    produk_list = []
    log_aktivitas = []
    queue_pengiriman = deque(["Pesanan #001", "Pesanan #002", "Pesanan #003"])
    print("\nMenambah Produk")
    tambah_produk(produk_list, log_aktivitas)
    print("\nMenampilkan Produk")
    tampilkan_produk(produk_list)
    print("\nMencari Produk")
    cari_produk(produk_list)
    print("\nMenghapus Produk")
    hapus_produk(produk_list, log_aktivitas)
    print("\nMenampilkan Produk Setelah Penghapusan")
    tampilkan_produk(produk_list)
    print("\nMengurutkan Produk")
    urutkan_produk(produk_list, log_aktivitas)
    print("\nMenampilkan Produk Setelah Pengurutan")
    tampilkan_produk(produk_list)
    print("\nMenampilkan Log Aktivitas")
    tampilkan_log(log_aktivitas)
    print("\nMenampilkan Antrian Pengiriman")
    antrian_pengiriman(queue_pengiriman)

if __name__ == "__main__":
    main()
