class Animal:
    def __init__(self, nama, makanan, hidup, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.reproduksi = reproduksi

    def cetak(self):
        print("======================================================="
              "\nINDUKAN ANIMAL")
        print("nama \t\t: ", self.nama,
              "\nmakanan \t: ", self.makanan,
              "\nhidup \t\t: ", self.hidup,
              "\nreproduksi \t: ", self.reproduksi)
        print("=======================================================")

buaya = Animal("buaya", "daging", "amphibi", "bertelur")
buaya.cetak()