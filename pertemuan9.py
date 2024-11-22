#mencari celcius
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


#fungsi
def is_genap(genap):
    return genap %2 == 0 

print(is_genap(4))
print(is_genap(7))

#mencetak nilai kelulusan
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'lulus'
    else : 
        return 'gagal'

print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

#bilangan genap
print("\n mencetak bilangan ganjil ")
def bil_ganjil(ganjil):
    for i in range(1, ganjil, 2):
        print(i, end=" ")
#memasukan value        
bil_ganjil(20)