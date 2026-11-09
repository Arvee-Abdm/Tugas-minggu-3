# main.py
# Program utama SIAP (Sistem Antri Pasien)

from utils import tampilkan_judul, jeda, input_pilihan
from fitur import (
    pilih_dokter,
    tampilkan_jadwal,
    pendaftaran_pasien,
    lihat_antrean,
    cari_antrean,
    panggil_pasien
)


def menu():
    while True:
        tampilkan_judul()
        print("MENU UTAMA")
        print("1. Melihat jadwal dokter")
        print("2. Melihat jadwal dokter tertentu")
        print("3. Pendaftaran pasien")
        print("4. Melihat semua antrean")
        print("5. Mencari nomor antrean")
        print("6. Panggil pasien berikutnya")
        print("0. Keluar")

        pilihan = input_pilihan("\nPilih menu: ", ["0", "1", "2", "3", "4", "5", "6"])

        if pilihan == "1":
            tampilkan_jadwal()
            jeda()
        elif pilihan == "2":
            pilih_dokter()
            jeda()
        elif pilihan == "3":
            pendaftaran_pasien()
            jeda()
        elif pilihan == "4":
            lihat_antrean()
            jeda()
        elif pilihan == "5":
            cari_antrean()
            jeda()
        elif pilihan == "6":
            panggil_pasien()
            jeda()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan SIAP.")
            print("Semoga lekas sehat!")
            break


if __name__ == "__main__":
    menu()
