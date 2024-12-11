class Person:
    def _init_(self, nama, umur, gender):
        self.nama = nama 
        self.umur = umur
        self.gender = gender
        
    def jalan(self):
        print(f"{self.nama} bisa berjalan")
        
    def ngomong(self):
        print(f"dia biasa berbicara karena dia {self.gender}")
        
class Supir(Person):
    def _init_(self, nama, umur, gender, sim):
        super()._init_(nama, umur, gender)
        self.sim = sim
        
    def nyupir(self):
        print(f"{self.nama} bisa nyupir karna memiliki sim {self.sim}") 

bayu = Person("bayu", 20, "Laki-Laki")
bayu.jalan()
bayu.ngomong()

andi = Supir("Andi", 30, "Laki=Laki","A")
andi.jalan()

class Mahasiswa(Person):
    def _init_(self, nama, umur, gender, nim):
        super()._init_(nama, umur, gender)
        self.nim = nim
        
    def belajar(self):
        print(f"{self.nama} sedang belajar dengan {self.nim}")
        
bunga = Mahasiswa("bunga", 20, "Perempuan", 2001) 
bunga.belajar()