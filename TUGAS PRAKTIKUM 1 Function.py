def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
panjang = float(input("masukkan panjang persegi: "))
lebar = float(input("masukkan lebar persegi: "))
hasil = luas_persegi_panjang(panjang, lebar)
print("luas persegi panjang ialah:", hasil)