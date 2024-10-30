# Program untuk GEROBAK FRIED CHICKEN

# Impor modul yang diperlukan
import os  # Modul os digunakan untuk membersihkan layar konsol

# Definisikan menu dan harga
menu = {
    'D': {'nama': 'Dada', 'harga': 2500},  # Mendefinisikan item menu 'Dada' dengan kode 'D' dan harga 2500
    'P': {'nama': 'Paha', 'harga': 2000},  # Mendefinisikan item menu 'Paha' dengan kode 'P' dan harga 2000
    'S': {'nama': 'Sayap', 'harga': 1500}  # Mendefinisikan item menu 'Sayap' dengan kode 'S' dan harga 1500
}

def bersihkan_layar():
    """Membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Menggunakan 'cls' untuk Windows, 'clear' untuk Unix/Linux

def tampilkan_menu():
    """Menampilkan menu kepada pengguna."""
    print("MENU GEROBAK FRIED CHICKEN BAKARAN JOGLO")  # Mencetak judul menu
    print("-" * 35)  # Mencetak garis pemisah
    print("Kode  Jenis Menu  Harga")  # Mencetak header tabel
    print("-" * 35)  # Mencetak garis pemisah
    for kode, item in menu.items():  # Iterasi melalui setiap item dalam menu
        print(f"{kode:<5} {item['nama']:<12} Rp. {item['harga']}")  # Mencetak detail setiap item menu
    print("-" * 35)  # Mencetak garis pemisah

def ambil_pesanan():
    """Mengambil detail pesanan dari pengguna."""
    pesanan = []  # Inisialisasi list kosong untuk menyimpan pesanan
    while True:  # Loop utama untuk mengambil pesanan
        tampilkan_menu()  # Menampilkan menu sebelum setiap pesanan
        print("\nMasukkan pesanan Anda (atau 'selesai' untuk mengakhiri):")
        
        jenis = input("Banyak Jenis Makanan Yang Ingin Dipesan: ")  # Meminta input jumlah jenis pesanan
        if jenis.lower() == 'selesai':  # Jika pengguna mengetik 'selesai', keluar dari loop
            break
        
        try:
            jenis = int(jenis)  # Mencoba mengkonversi input ke integer
        except ValueError:
            print("Input tidak valid. Masukkan angka.")  # Jika konversi gagal, tampilkan pesan error
            continue  # Kembali ke awal loop

        for i in range(jenis):  # Loop untuk setiap jenis pesanan
            print(f"\nJenis Ke-{i+1}")
            kode = input("Kode Menu Makanan [D/P/S]: ").upper()  # Meminta input kode potong dan mengubahnya ke huruf besar
            if kode not in menu:  # Jika kode tidak ada dalam menu
                print("Kode tidak valid. Silakan coba lagi.")
                continue  # Kembali ke awal loop jenis
            
            try:
                banyak = int(input("Berapa Potong Yang Anda Pesan: "))  # Meminta input jumlah potong
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue  # Kembali ke awal loop jenis

            pesanan.append((kode, banyak))  # Menambahkan pesanan ke list
        
        break  # Keluar dari loop utama setelah semua pesanan dimasukkan
    
    return pesanan  # Mengembalikan list pesanan

def hitung_total(pesanan):
    """Menghitung total harga termasuk pajak."""
    subtotal = sum(menu[kode]['harga'] * banyak for kode, banyak in pesanan)  # Menghitung subtotal
    pajak = subtotal * 0.1  # Menghitung pajak (10% dari subtotal)
    total = subtotal + pajak  # Menghitung total (subtotal + pajak)
    return subtotal, pajak, total  # Mengembalikan subtotal, pajak, dan total

def tampilkan_struk(pesanan):
    """Menampilkan struk dengan detail pesanan."""
    bersihkan_layar()  # Membersihkan layar sebelum menampilkan struk
    print("GEROBAK FRIED CHICKEN BAKARAN JOGLO")  # Mencetak judul struk
    print("-" * 50)  # Mencetak garis pemisah
    print("No.  Jenis Menu  Harga Satuan  Banyak  Jumlah Harga")  # Mencetak header tabel struk
    print("-" * 50)  # Mencetak garis pemisah
    
    for i, (kode, banyak) in enumerate(pesanan, 1):  # Iterasi melalui setiap item pesanan
        item = menu[kode]  # Mengambil detail item dari menu
        subtotal = item['harga'] * banyak  # Menghitung subtotal untuk item ini
        print(f"{i:<4} {item['nama']:<13} {item['harga']:<13} {banyak:<7} Rp {subtotal}")  # Mencetak detail item
    
    subtotal, pajak, total = hitung_total(pesanan)  # Menghitung total pesanan
    print("-" * 50)  # Mencetak garis pemisah
    print(f"{'Jumlah Bayar':<41} Rp {subtotal}")  # Mencetak jumlah bayar
    print(f"{'Pajak 10%':<41} Rp {pajak:.0f}")  # Mencetak jumlah pajak
    print(f"{'Total Bayar':<41} Rp {total:.0f}")  # Mencetak total bayar

def main():
    """Fungsi utama untuk menjalankan program."""
    while True:  # Loop utama program
        bersihkan_layar()  # Membersihkan layar di awal setiap iterasi
        print("Selamat datang di GEROBAK FRIED CHICKEN BAKARAN JOGLO!")  # Mencetak pesan selamat datang
        pesanan = ambil_pesanan()  # Mengambil pesanan dari pengguna
        if pesanan:  # Jika ada pesanan
            tampilkan_struk(pesanan)  # Menampilkan struk pesanan
        
        lagi = input("\nApakah Anda ingin memesan lagi? (y/t): ")  # Meminta input untuk pesanan lagi
        if lagi.lower() != 'y':  # Jika jawaban bukan 'y', keluar dari program
            print("Terima kasih telah mampir di lapak kami!")
            break  # Keluar dari loop utama, mengakhiri program

if __name__ == "__main__":
    main()  # Memanggil fungsi main() jika skrip dijalankan sebagai program utama