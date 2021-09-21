class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def luasSegitiga(self):
        print("Luas segitaga adalah: ")
        print((self.alas*self.tinggi)/2)

class Balok:
    def __init__(self,panjang,lebar,tinggi):
        self.panjang=panjang
        self.lebar=lebar
        self.tinggi=tinggi
    def volumeBalok(self):
        print("\nVolume Balok adalah: ")
        print(self.panjang*self.lebar*self.tinggi)
Segitiga=Segitiga(
    alas=20,
    tinggi=9
)
Balok=Balok(
    panjang=15,
    lebar=6,
    tinggi=5
)

Segitiga.luasSegitiga()
Balok.volumeBalok()

