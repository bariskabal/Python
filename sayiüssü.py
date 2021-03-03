def usHesapla(sayi,us):
    sonuc=1
    for i in range(0,us):
        sonuc*=sayi
    return sonuc

def usHesapla2(sayi,us):
    return sayi**us

print(usHesapla2(2,3))
print(pow(3,4))