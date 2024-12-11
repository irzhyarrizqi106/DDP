from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, reproduksi, genus, bisa):
        super().__init__(nama, makanan, hidup, reproduksi)
        self.genus = genus
        self.bisa = bisa

    def cetak_ular(self):
        print("======================================================="
              "\nANAKAN DARI INDUK ANIMAL")
        print("nama \t\t: ", self.nama,
              "\nmakanan \t: ", self.makanan,
              "\nhidup \t\t: ", self.hidup,
              "\nreproduksi \t: ", self.reproduksi,
              "\ngenus \t\t: ", self.genus,
              "\nbisa \t\t: ", self.bisa)
        print("=======================================================")
        
King_kobra = Ular("King kobra", "segalanya", "amphibi", "ovovivipar", "naja", "sitotiksik")
Piton = Ular("Piton", "segalanya", "amphibi", "ovovivipar", "Pythonida", "tak berbisa")
Pohon = Ular("Pohon", "segalanya", "amphibi", "ovovivipar", "Rhabdophis", "Ahaetulla prasina")
King_kobra.cetak_ular()
Piton.cetak_ular()
Pohon.cetak_ular()