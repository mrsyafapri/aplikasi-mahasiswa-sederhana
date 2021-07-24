class Mahasiswa:
    """Kelas Mahasiswa"""

    def __init__(self, nama, nim, nilai_akhir):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_akhir = nilai_akhir

    def mata_kuliah(self, pilihan):
        if pilihan == 1:
            self.__pilihan = "Pemrograman Fundamental"
        elif pilihan == 2:
            self.__pilihan = "Pemrograman Lanjutan"
        elif pilihan == 3:
            self.__pilihan = "Pemrograman Mobile"
        elif pilihan == 4:
            exit()

    def nilai_huruf(self, nilai):
        if nilai >= 85 and nilai <= 100:
            self.__nilai_huruf = "A"
        elif nilai >= 81 and nilai < 85:
            self.__nilai_huruf = "A-"
        elif nilai >= 75 and nilai < 81:
            self.__nilai_huruf = "B+"
        elif nilai >= 70 and nilai < 75:
            self.__nilai_huruf = "B"
        elif nilai >= 65 and nilai < 70:
            self.__nilai_huruf = "B-"
        elif nilai >= 60 and nilai < 65:
            self.__nilai_huruf = "C+"
        elif nilai >= 55 and nilai < 60:
            self.__nilai_huruf = "C"
        elif nilai >= 50 and nilai < 55:
            self.__nilai_huruf = "D"
        else:
            self.__nilai_huruf = "E"
        return self.__nilai_huruf

    def kelulusan(self, nilai):
        if nilai > 55:
            self.__kelulusan = "Lulus"
        else:
            self.__kelulusan = "Gagal"
        return self.__kelulusan

    def cetak(self):
        print("Nama Mahasiswa  : {}".format(self.__nama))
        print("NIM             : {}".format(self.__nim))
        print("Nama Mata Kuliah: {}".format(self.__pilihan))
        print("Nilai Akhir     : {}".format(self.__nilai_akhir))
        print("Nilai Huruf     : {}".format(self.__nilai_huruf))
        print("Keterangan      : {}".format(self.__kelulusan))
