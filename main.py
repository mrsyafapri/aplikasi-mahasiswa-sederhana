from mahasiswa import Mahasiswa


def decor(func):
    def wrap():
        print("=" * 28)
        func()
        print("=" * 28)

    return wrap


@decor
def menu_matkul():
    print("Menu Mata Kuliah\t:")
    print(
        "1. Pemrograman Fundamental\n2. Pemrograman Lanjutan\n3. Pemrograman Mobile\n4. Keluar"
    )


# Input
nama = input("Masukkan Nama Anda".ljust(30))
nim = input("Masukkan NIM Anda".ljust(30))
nilai_akhir = float(input("Masukkan Nilai Akhir Anda".ljust(30)))
menu_matkul()
pilihan = int(input("Masukkan Jurusan Anda (1-4)".ljust(30)))

# Proses
mahasiswa = Mahasiswa(nama, nim, nilai_akhir)
mahasiswa.mata_kuliah(pilihan)
mahasiswa.nilai_huruf(nilai_akhir)
mahasiswa.kelulusan(nilai_akhir)

# Output
print()
print("=" * 40)
mahasiswa.cetak()
print("=" * 40)
