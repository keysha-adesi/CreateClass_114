class PersegiPanjang:
    # Konstruktor
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Fungsi menghitung keliling
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    # Fungsi menghitung luas
    def luas(self):
        return self.panjang * self.lebar

    # Fungsi __str__
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


# Membuat object
persegi = PersegiPanjang(3, 2)

print(persegi)
print("Keliling:", persegi.keliling(), "cm")
print("Luas:", persegi.luas(), "cm²")


