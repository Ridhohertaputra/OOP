# Program OOP untuk menghitung luas dan keliling lingkaran
class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        luas = 3.14 * self.jari_jari ** 2
        return luas

    def hitung_keliling(self):
        keliling = 2 * 3.14 * self.jari_jari
        return keliling
lingkaran = Lingkaran(4)
print("Luas lingkaran: ", lingkaran.hitung_luas())
print("Keliling lingkaran: ", lingkaran.hitung_keliling())
print("\n")

# Program FP untuk menghitung total harga belanjaan
keranjang = [
    {"nama": "Buku Tulis", "harga": 5000},
    {"nama": "Pensil", "harga": 1000},
    {"nama": "Buku Gambar", "harga": 8000},
    {"nama": "Penghapus", "harga": 500}
]
total_harga = sum(map(lambda item: item["harga"], keranjang))
print("Total harga: ", total_harga)
