# fitur.py
# Data contoh dan fitur utama SIAP

from utils import garis, input_wajib, input_pilihan

# Jadwal ini hanya data simulasi untuk latihan.
DOKTER = [
    {
        "id": 1,
        "nama": "dr. Andi Pratama",
        "spesialis": "Dokter Umum",
        "hari": "Senin - Jumat",
        "jam": "08.00 - 12.00"
    },
    {
        "id": 2,
        "nama": "dr. Siti Rahma, Sp.A",
        "spesialis": "Dokter Anak",
        "hari": "Senin, Rabu, Jumat",
        "jam": "09.00 - 13.00"
    },
    {
        "id": 3,
        "nama": "dr. Budi Santoso, Sp.PD",
        "spesialis": "Penyakit Dalam",
        "hari": "Selasa - Kamis",
        "jam": "10.00 - 14.00"
    },
    {
        "id": 4,
        "nama": "dr. Maya Putri, Sp.KK",
        "spesialis": "Kulit dan Kelamin",
        "hari": "Senin - Kamis",
        "jam": "13.00 - 16.00"
    }
]

# Data pasien dan antrean disimpan di memori selama program berjalan.
pasien_terdaftar = []
antrean = []
nomor_antrean = 1


def tampilkan_jadwal():
    print("\n=== JADWAL DOKTER ===")
    for dokter in DOKTER:
        print(f"\nID          : {dokter['id']}")
        print(f"Nama        : {dokter['nama']}")
        print(f"Spesialis   : {dokter['spesialis']}")
        print(f"Hari        : {dokter['hari']}")
        print(f"Jam         : {dokter['jam']}")
        garis()


def pilih_dokter():
    tampilkan_jadwal()
    pilihan = input_pilihan(
        "\nMasukkan ID dokter yang ingin dilihat (0 untuk kembali): ",
        [str(d["id"]) for d in DOKTER] + ["0"]
    )

    if pilihan == "0":
        return

    dokter = next(d for d in DOKTER if d["id"] == int(pilihan))
    print("\n=== DETAIL DOKTER ===")
    print(f"Nama       : {dokter['nama']}")
    print(f"Spesialis  : {dokter['spesialis']}")
    print(f"Hari       : {dokter['hari']}")
    print(f"Jam        : {dokter['jam']}")


def pendaftaran_pasien():
    global nomor_antrean

    print("\n=== PENDAFTARAN PASIEN ===")
    nama = input_wajib("Nama lengkap pasien : ")
    umur = input_wajib("Umur pasien         : ")

    while not umur.isdigit() or int(umur) <= 0:
        print("Umur harus berupa angka lebih dari 0.")
        umur = input_wajib("Umur pasien         : ")

    no_hp = input_wajib("Nomor HP            : ")

    print("\nApakah pasien mempunyai surat rujukan?")
    print("1. Ya")
    print("2. Tidak")
    rujukan = input_pilihan("Pilih (1/2): ", ["1", "2"])

    if rujukan == "2":
        print("\nPasien belum memiliki surat rujukan.")
        print("Silakan mengurus rujukan terlebih dahulu melalui fasilitas kesehatan")
        print("tingkat pertama atau petugas yang berwenang.")
        print("Pendaftaran kunjungan spesialis belum dapat dilanjutkan.")
        return

    tampilkan_jadwal()
    id_dokter = input_pilihan(
        "Pilih ID dokter tujuan: ",
        [str(d["id"]) for d in DOKTER]
    )
    dokter = next(d for d in DOKTER if d["id"] == int(id_dokter))

    pasien = {
        "nama": nama,
        "umur": int(umur),
        "no_hp": no_hp,
        "rujukan": True,
        "dokter": dokter["nama"],
        "nomor": nomor_antrean,
        "status": "Menunggu"
    }

    pasien_terdaftar.append(pasien)
    antrean.append(pasien)
    nomor_antrean += 1

    print("\nPendaftaran berhasil!")
    print(f"Nama pasien : {nama}")
    print(f"Dokter      : {dokter['nama']}")
    print(f"No. antrean : A-{pasien['nomor']:03d}")
    print("Status      : Menunggu")


def lihat_antrean():
    print("\n=== DAFTAR ANTREAN PASIEN ===")

    if not antrean:
        print("Belum ada pasien dalam antrean.")
        return

    for pasien in antrean:
        print(f"\nNomor antrean : A-{pasien['nomor']:03d}")
        print(f"Nama pasien   : {pasien['nama']}")
        print(f"Dokter        : {pasien['dokter']}")
        print(f"Status        : {pasien['status']}")
        garis()


def cari_antrean():
    print("\n=== CARI ANTREAN PASIEN ===")
    if not antrean:
        print("Belum ada antrean.")
        return

    nomor = input_wajib("Masukkan nomor antrean (contoh A-001): ").upper()

    for pasien in antrean:
        nomor_pasien = f"A-{pasien['nomor']:03d}"
        if nomor == nomor_pasien:
            print("\nData antrean ditemukan:")
            print(f"Nama pasien : {pasien['nama']}")
            print(f"Dokter      : {pasien['dokter']}")
            print(f"Nomor       : {nomor_pasien}")
            print(f"Status      : {pasien['status']}")
            return

    print("Nomor antrean tidak ditemukan.")


def panggil_pasien():
    print("\n=== PANGGIL PASIEN BERIKUTNYA ===")
    for pasien in antrean:
        if pasien["status"] == "Menunggu":
            pasien["status"] = "Sedang diperiksa"
            print(f"Memanggil A-{pasien['nomor']:03d} - {pasien['nama']}")
            print(f"Dokter: {pasien['dokter']}")
            return

    print("Tidak ada pasien yang sedang menunggu.")
