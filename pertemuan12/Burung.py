from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, reproduksi, paruh, sayap):
        super().__init__(nama, makanan, hidup, reproduksi)
        self.paruh = paruh
        self.sayap = sayap

    def cetak_burung(self):
        print("======================================================="
              "\nANAKAN DARI INDUK ANIMAL")
        print("nama \t\t: ", self.nama,
              "\nmakanan \t: ", self.makanan,
              "\nhidup \t\t: ", self.hidup,
              "\nreproduksi \t: ", self.reproduksi,
              "\nparuh \t\t: ", self.paruh,
              "\nsayap \t: ", self.sayap)
        print("=======================================================")

elang = Burung("elang peregrine", "daging", "sarang di ketinggian", "ovivar", "paruh tajam", "sayap besar dan dibuat untuk kecepatan atau akselerasi")
kolibri = Burung("kolibri", "nektar", "pepohonan", "ovivar", "paruh tajpanjang dan ramping", "sayap kecil dan cepat")
penguin = Burung("pinguin", "ikan", "koloni di daerah bersalju", "ovivar", "paruh pendek dan kuat", "sayap yang dimodifikasi menjadi sirip")
elang.cetak_burung()
kolibri.cetak_burung()
penguin.cetak_burung()