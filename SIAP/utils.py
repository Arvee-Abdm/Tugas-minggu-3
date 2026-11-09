# utils.py
# Fungsi bantuan untuk aplikasi SIAP

def garis():
    print("=" * 55)


def tampilkan_judul():
    print(r"""
███████╗██╗ █████╗ ██████╗
██╔════╝██║██╔══██╗██╔══██╗
███████╗██║███████║██████╔╝
╚════██║██║██╔══██║██╔═══╝
███████║██║██║  ██║██║
╚══════╝╚═╝╚═╝  ╚═╝╚═╝

       SIAP = Sistem Antri Pasien
""")
    garis()


def jeda():
    input("\nTekan ENTER untuk kembali ke menu...")


def input_wajib(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def input_pilihan(pesan, pilihan):
    while True:
        nilai = input(pesan).strip()
        if nilai in pilihan:
            return nilai
        print("Pilihan tidak valid. Silakan coba lagi.")
