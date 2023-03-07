import sys

message = "saya sebuah file module python"
waktu = "sekarang jam 21.05 WIB tanggal 7 Maret 2023"
angka = 42


def sapa(waktu, tempat="sekolah", list_nama=[]):
    for orang in list_nama:
        print("salam " + str(orang))
    print("anda sedang berada di " + tempat + " di " + waktu + " hari.")


if (__name__ == '__main__'):
    print("halo, saya tes.py")

    print("This is the name of the program:", sys.argv[0])

    print("Argument List:", str(sys.argv))

    sapa("pagi", "kantor", sys.argv)


# BREAK sampai jam 21.00
# baru lanjut ke import
# setelah import, kita kembali ke module
# baru lanjut ke package
