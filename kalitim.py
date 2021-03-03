class personel():
    def __init__(self,ad = "Girilmedi",soyad="Bilgi yok",yas=23,maas=0):
        self.ad = ad
        self.soyad=soyad
        self.yas=yas
        self.maas=maas

    def bilgileri_göster(self):
        print("""
        Ad : {}
        Soyad: {}
        Yas : {}
        Maas : {}
        """.format(self.ad,self.soyad,self.yas,self.maas))

    def zam(self,miktar):
        print("Zam ekleniyor.")
        self.maas+=miktar


class yönetici(personel):
    pass

    def __init__(self,pozisyon="Girilmedi"):

        super().__init__()

        self.pozisyon=pozisyon

müdür = yönetici()
müdür.pozisyon="manyak"

print(müdür.pozisyon)



    

