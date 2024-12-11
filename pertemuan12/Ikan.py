from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, reproduksi, ordo, jumlah_telur):
        super().__init__(nama, makanan, hidup, reproduksi)
        self.ordo = ordo
        self.jumlah_telur = jumlah_telur

    def cetak_Ikan(self):
        print("======================================================="
              "\nANAKAN DARI INDUK ANIMAL")
        print("nama \t\t: ", self.nama,
              "\nmakanan \t: ", self.makanan,
              "\nhidup \t\t: ", self.hidup,
              "\nreproduksi \t: ", self.reproduksi,
              "\nordo \t\t: ", self.ordo,
              "\njumlah telur \t: ", self.jumlah_telur)
        print("=======================================================")    

Hiu = Ikan("hiu putih besar", "ikan", "laut dalam dengan suhu tropis", "ovovivivar", "Selachimorpha", "sesuai dengan kemampuan induk tersebut")
Badut = Ikan("badut ", "anemon", "laut dengan suhu tropis", "ovivar", "Perciformes", "sesuai dengan kemampuan dari induknya")
Koi = Ikan("koi ", "pelet ikan", "air tawar", "ovivar", "Cypriniformes", "ribuan")
Hiu.cetak_Ikan()
Badut.cetak_Ikan()
Koi.cetak_Ikan()