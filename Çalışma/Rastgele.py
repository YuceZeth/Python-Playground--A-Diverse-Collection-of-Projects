"""
r = int(input("Yarı Çapı Giriniz = "))
h = int(input("Yüksekliği Giriniz = "))
pi = 3.14

def silindirhacim(r,h):
    hesap = pi * (r*r) * h;
    return hesap

print("Silindirin Hacmi = ",silindirhacim(r,h))
"""
"""
a = int(input("A = "))
n = int(input("N = "))
r = int(input("R = "))

print(a,"x^",n,"+",r,sep="")

def türev(a,n):
    a,n=a*n,n-1
    print(a,"x^",n,sep="")

print(türev(a,n))
"""

"""
top=0
while True:
    sayı = input("Sayı Giriniz = ")
    if (sayı == "q"):
        break
    else:
        isayi =int(sayı)
        top += isayi

print("Toplamları = ",top)
"""


class yazılımcı():
    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgilerigöster(self):
        print("""
        Yazılımcı Objesinin Özellikleri

        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {}

        """.format(self.isim, self.soyisim, self.numara, self.maaş, self.diller))

    def zam_yap(self, zam_miktarı):
        print("Zam Yapılıyor...")

        self.maaş += zam_miktarı

    def dil_ekle(self, yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)

    def numara_de(self, yeni_numara):
        print("Numara Değiştiliyor...")
        self.numara = yeni_numara



yazılımcı.numara_de(345)

yazılımcı.bilgilerigöster()
















