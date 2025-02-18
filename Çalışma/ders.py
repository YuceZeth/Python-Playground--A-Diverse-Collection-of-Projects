"""
isim = input("isim giriniz : ")
soyisim = input("soyisim giriniz :  ")
print("{} {}".format(soyisim, isim))
"""
"""
sayac = 0
sozluk = {}
while True:
    isim = input("İsim : ")
    soyisim = input("Soyisim : ")
    sayac = sayac + 1
    sozluk[isim] = soyisim
    if sayac == 9:
        break
print(sozluk)
"""
"""
sayi1 = int(input("sayı giriniz : "))
sayi2 = int(input("sayı giriniz : "))
sayac = 2
enb = sayi1
enk = sayi2
while True:
    sayi = int(input("sayı giriniz : "))
    sayac = sayac + 1
    if sayi > enb:
        enb = sayi
    elif enk > sayi:
        enk = sayi

    if sayac == 9:
        break
print("Toplam : ", enk + enb)
"""
"""
toplam = 0
while True:
    sayi = int(input("Sayı giriniz : "))
    if 0 <= sayi <= 99:
        if sayi == 23:
            break
        if sayi == 33:
            break
        if sayi == 43:
            break
        if sayi == 53:
            break
        if sayi == 63:
            break
        if sayi == 73:
            break
        if sayi == 83:
            break
        toplam = toplam + sayi
    else:
        print("Sayı 0-99 arası olmalıdır...")
print(toplam)
"""
"""
sayac = 232000000
sayac2 = 0
while True:
    for i in range(1, 21):
        if sayac % i == 0:
          sayac2 = sayac2 + 1
    print("Bölünen sayısı : ", sayac2)
    if sayac2 == 20:
        break
    sayac2 = 0
    sayac = sayac + 1
print("Asıl sayı : ", sayac)
"""
"""
kt = 0
t = 0
for i in range(1, 101):
    kt = kt + i ** 2
    t = t + i
tk = t ** 2
print("Karelerinin toplamı :", kt)
print("Toplamının karesi : ", tk)
print("Farkları : ", tk - kt)
"""
"""
toplam = 0
for i in range(1, 200000):
    sayac = 0
    for j in range(1, i+1):
        if i % j == 0:
            sayac += 1
    if sayac == 2:
        toplam = toplam + i
print("Asallar toplamı : ", toplam)
"""
"""
def isim_soyisim(isim, soyisim):
    print("İsim : {} \nSoyisim : {}".format(isim, soyisim))
isim = input("İsim : ")
soyisim = input("Soyisim : ")
isim_soyisim(isim, soyisim)
"""
"""
def yas_hesapla(guncelyil, dogumyil):
    yas = guncelyil - dogumyil
    print("Yaşınız : ", yas)
    if 0 < yas < 6:
        print("çocuk")
    elif 6 < yas < 18:
        print("Genç")
    elif 18 < yas < 30:
        print("Yetişkin")
    else:
        print("Yaşlı")
guncelyil = int(input("Güncel yıl : "))
dogumyil = int(input("Doğum yıl : "))
yas_hesapla(guncelyil, dogumyil)
"""
"""
def ortalama_hesapla(ara, quiz, final):
    ortalama = (ara * 0.3) + (quiz * 0.15) + (final * 0.55)
    if ortalama < 35:
        print("Kaldınız")
    else:
        print("Geçtiniz")
ara = int(input("Ara sınav : "))
quiz = int(input("Quiz : "))
final = int(input("Final : "))
ortalama_hesapla(ara, quiz, final)
"""
"""
dizi = [50, 80, 30, 20]
def fonk(dizi):
    toplam = 0
    for i in dizi:
        toplam = toplam + i
    ortalama = toplam / len(dizi)
    print("Dizideki sayıların \nToplamı : {}\nOrtalaması : {}\nBoyutu : {}".format(toplam, ortalama, len(dizi)))
fonk(dizi)
"""
"""
def bolme(x, y):
    if y == 0:
        print("Payda 0 olamaz...")
    else:
        print("Sonuc : ", x / y)
bolme(0, 5)
"""
"""
def alan(a, b, c, d):
    if a == b and a == c and a == d:
        alan = a ** 2
        print("Alan : {} ve şekil karedir...".format(alan))
    elif a == c and b == d:
        alan = a * b
        print("Alan : {} ve şekil dikdörtgendir...".format(alan))
def cevre(a, b, c, d):
    if a == b and a == c and a == d:
        cevre = a * 4
        print("Çevre : {} ve şekil karedir...".format(cevre))
    elif a == c and b == d:
        cevre = a + b + c + d
        print("Çevre : {} ve şekil dikdörtgendir...".format(cevre))
    else:
        cevre = a + b + c + d
        print("Çevre : {} ve şekil çeşitkenar dörtgendirdır...".format(cevre))
alan(4, 4, 4, 4)
cevre(4, 4, 4, 4)
"""
"""
def toplama():
    top = 0
    for i in range(43, 124):
        top = top + i
    return top
def bolunen():
    top = 0
    for i in range(123, 224):
        if i % 7 == 0 and i % 3 == 0:
            top = top + i
    return top
def azalan():
    sayilar = []
    i = 223
    while True:
        sayilar.append(i)
        i = i - 1
        if i == 152:
            break
        else:
            continue
    return sayilar
while True:
    sayi = int(input("Sayı giriniz : "))
    if 23 < sayi < 223:
        print("43 den 123 e kadar sayılar toplamı : ", toplama())
        print("123 den 223 arasında 3 ve 7 ye bölünen sayılar toplamı : ", bolunen())
        print("Sayılar : ", azalan())
        break
    else:
        continue
"""
"""
def ekleme(adsoyad, numara):
    kisiler.append(adsoyad)
    kisiler.append(numara)
def sil(numara):
    for i in range(0, len(kisiler)):
        if kisiler[i] == numara:
            kisiler.pop(i)
            kisiler.pop(i - 1)
def bul(secim2, istek):
    if secim2 == '1':
        for i in range(0, len(kisiler)):
            if kisiler[i] == istek:
                print("Ad-Soyad : {}    Numara : {}".format(kisiler[i], kisiler[i + 1]))
    elif secim2 == '2':
        for i in range(0, len(kisiler)):
            if kisiler[i] == istek:
                print("Ad-Soyad : {}    Numara : {}".format(kisiler[i - 1], kisiler[i]))
def duzenle(secim2, istek, yadsoyad, ynumara):
    if secim2 == '1':
        for i in range(0, len(kisiler)):
            if kisiler[i] == istek:
                kisiler[i] = yadsoyad
                kisiler[i + 1] = ynumara
    elif secim2 == '2':
        for i in range(0, len(kisiler)):
            if kisiler[i] == istek:
                kisiler[i - 1] = yadsoyad
                kisiler[i] = ynumara
kisiler = []
while True:
    print("Kişi eklemek   için 1Kişi silmek    için 2Kişi bulmak    için 3Kişi düzelemek için 4Çıkış               5")
    secim = int(input("Seçim : "))
    if secim == 1:
        adsoyad = input("Ad soyad giriniz : ")
        numara = input("Numara giriniz : ")
        if numara in kisiler:
            print("{} numara daha önce kayıt edilmiş....".format(numara))
        else:
            print("Başarı ile kişi eklendi...")
            ekleme(adsoyad, numara)
            print(kisiler)
    elif secim == 2:
        numara = str(input("Silinecek numarayı giriniz : "))
        sil(numara)
        print(kisiler)
    elif secim == 3:
        print("Ad-Soyad ile arama için 1 \nNumara ile arama için 2")
        secim2 = str(input("Seçim : "))
        istek = str(input("Arama : "))
        bul(secim2, istek)
    elif secim == 4:
        print("Ad-Soyad ile arama için 1 \nNumara ile arama için 2")
        secim2 = str(input("Seçim : "))
        istek = str(input("Arama : "))
        bul(secim2, istek)
        yadsoyad = str(input("Yeni Ad-Soyad : "))
        ynumara = str(input("Yeni Numara : "))
        duzenle(secim2, istek, yadsoyad, ynumara)
        print(kisiler)
    elif secim == 5:
        print("{} kişi kayıtlı çıkarsanız bütün kayıtlar silinecek çıkmak istiyor musunuz? (E/H)".format(
            len(kisiler) / 2))
        secim3 = input("Seçim = ")
        if secim3 == "E":
            break
        elif secim3 == "H":
            continue
    else:
        print("Geçersiz işlem...")
"""
"""
import random
plakalar = ["", "Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
            "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
            "Diyarbakır",
            "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
            "Hatay",
            "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
            "Kocaeli",
            "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde",
            "Ordu", "Rize",
            "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa",
            "Uşak", "Van",
            "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın",
            "Ardahan", "Iğdır",
            "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
kullanici_isimleri = [""]
birinci_puan = 100
ikinci_puan = 100
birinci_sayisi = random.randint(1, 81)
ikinci_sayisi = random.randint(1, 81)
def kullanici():
    isim = input("Kullanıcı ismini giriniz : ")
    kullanici_isimleri.append(isim)
def tahmin1(ktahmin):
    if birinci_sayisi == ktahmin:
        return 1
    else:
        while True:
            sinir = random.randint(birinci_sayisi - 3, birinci_sayisi + 3)
            if sinir == birinci_sayisi:
                continue
            else:
                break
        print("Tahmininiz {} uzak...".format(plakalar[sinir]))
        global birinci_puan
        birinci_puan = birinci_puan - 10
        print("Puanınız : ", birinci_puan)
        if birinci_puan == 0:
            return 0
def tahmin2(ktahmin):
    if ikinci_sayisi == ktahmin:
        return 1
    else:
        while True:
            sinir = random.randint(ikinci_sayisi - 3, ikinci_sayisi + 3)
            if sinir == ikinci_sayisi:
                continue
            else:
                break
        print("Tahmininiz {} uzak...".format(plakalar[sinir]))
        global ikinci_puan
        ikinci_puan = ikinci_puan - 10
        print("Puanınız : ", ikinci_puan)
        if ikinci_puan == 0:
            return 0
birinci = kullanici()
ikinci = kullanici()
print("Birincinin sayısı : ", birinci_sayisi)
print("İkincinin sayısı : ", ikinci_sayisi)
while True:
    k1tahmin = int(input("{} tahmin giriniz : ".format(kullanici_isimleri[1])))
    x = tahmin1(k1tahmin)
    if x == 1:
        k2tahmin = int(input("{} tahmin giriniz : ".format(kullanici_isimleri[2])))
        y = tahmin2(k2tahmin)
        if y == 1:
            print("{} ve {} tebrikler kazandınız!!!".format(kullanici_isimleri[1], kullanici_isimleri[2]))
            break
        elif y == 0:
            print("{} : {}\n tebrikler kazandınız!!!".format(kullanici_isimleri[1], birinci_puan))
            print("{} başarısız....".format(kullanici_isimleri[2]))
            break
    elif x == 0:
        k2tahmin = int(input("{} tahmin giriniz : ".format(kullanici_isimleri[2])))
        y = tahmin2(k2tahmin)
        if y == 1:
            print("{} başarısız....".format(kullanici_isimleri[1]))
            print("{} : {}\n tebrikler kazandınız!!!".format(kullanici_isimleri[2], ikinci_puan))
            break
        elif y == 0:
            print("{} : {}\n başarısız".format(kullanici_isimleri[1], kullanici_isimleri[2]))
            break
"""
"""
class araba:
    def __init__(self, model, renk, beygir, silindir):
        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir
    def bilgi_goster(self): print("Araç bilgileri \nModel : {} \nRenk : {} \nBeygir : {} \nSilindir : {}".format(
    self.model, self.renk, self.beygir, self.silindir)) 
    araba1 = araba("Peugeot 301", "Beyaz", 90, 4) 
"""
"""
class kus:
    def __init__(self, isim, renk, yas, tur):
        self.isim = isim
        self.renk = renk
        self.yas = yas
        self.tur = tur
kus1 = kus("Efe", "Beyaz", 1, "Hint Bülbülü")
kus2 = kus("Maviş", "Mavi", 2, "Muhabbet Kuşu")
"""
"""
class personel:
    def __init__(self, isim, soyisim, sicil, isegirisyili, maas, cocuksayisi):
        self.isim = isim
        self.soyisim = soyisim
        self.sicil = sicil
        self.isegirisyili = isegirisyili
        self.maas = maas
        self.cocuksayisi = cocuksayisi

    def bilgi_goster(self):
        print("Bilgiler...\nİsim : {} \nSoyisim : {} \nSicil : {} \nİşe Giriş Yılı : {} \nMaaş : {} \nÇocuk Sayısı : {}"
              .format(self.isim, self.soyisim, self.sicil, self.isegirisyili, self.maas, self.cocuksayisi))
    def maas_arttir(self, ilave):
        yil = 2021 - self.isegirisyili
        if 1 <= yil < 5:
            self.maas = self.maas + ilave * 1.1
            print("Yeni Maaş : ", self.maas)
        elif 5 <= yil < 10:
            self.maas = self.maas + ilave * 1.2
            print("Yeni Maaş : ", self.maas)
        elif yil > 10:
            self.maas = self.maas + ilave * 1.3
            print("Yeni Maaş : ", self.maas)
        else:
            print("Bir Hata Oluştu...")
    def cocuk_arttir(self, ycocuk):
        self.cocuksayisi = self.cocuksayisi + ycocuk
        if self.cocuksayisi > 3:
            self.maas = self.maas + self.maas * 0.1
            print("Yeni Maaş : ", self.maas)
personel1 = personel("Kaan", "KAYACAN", "Temiz", 2019, 3500, 2)
personel1.bilgi_goster()
ilave = int(input("\nZam giriniz : "))
personel1.maas_arttir(ilave)
ycocuk = int(input("Çocuk sayısı : "))
personel1.cocuk_arttir(ycocuk)
"""
"""
class ogrenci:
    def __init__(self, numara, ad, yas, bolum, donem, ders=[]):
        self.numara = numara
        self.ad = ad
        self.yas = yas
        self.bolum = bolum
        self.donem = donem
        self.ders = ders
    def donem_degistir(self, ydonem):
        print("Dönem değiştiriliyor...")
        self.donem = ydonem
    def ders_ekle(self, yders):
        print("Ders ekleniyor...")
        self.ders.append(yders)
    def ders_cikar(self, cders):
        if cders in self.ders:
            print("Ders çıkartılıyor...")
            self.ders.remove(cders)
        else:
            print("Ders mevcut değil")
    def ders_goruntule(self):
        print(self.ders)
    def bilgi_goster(self):
        print("Bilgiler :\nNumara : {}\nAd : {}\nYaş : {}\nBölüm : {}\nDönem : {}"
              .format(self.numara, self.ad, self.yas, self.bolum, self.donem))
ogrenciler = []
dersler = []
for i in range(1, 4):
    numara = int(input("Numara giriniz : "))
    ad = input("Ad giriniz : ")
    yas = int(input("Yaş giriniz: "))
    bolum = input("Bölüm giriniz : ")
    donem = int(input("Dönem giriniz : "))
    ds = int(input("Kaç adet ders girilecek : "))
    for j in range(1, ds + 1):
        ders = input("Ders giriniz : ")
        dersler.append(ders)
    ogrenci1 = ogrenci(numara, ad, yas, bolum, donem, dersler)
    ogrenciler.append(ogrenci1)
for k in ogrenciler:
    print(k.bilgi_goster())
    print(k.ders_goruntule())
ogrenci1 = ogrenci(1, "Kaan", 21, "Matematik-Bilgisayar", 2, ["Bilgisayar Programlama", "Ayrık Matematik"])
ogrenci2 = ogrenci(2, "Efe", 20, "Matematik-Bilgisayar", 2, ["Bilgisayar Programlama", "Analitik Geometri"])
ogrenci1.ders_ekle("Analiz")
ogrenci1.ders_goruntule()
ogrenci1.ders_cikar("Bilgisayar Programlama")
ogrenci1.donem_degistir(3)
ogrenci1.ders_goruntule()
ogrenci.bilgi_goster()
"""
"""
class araclar:
    def __init__(self, isim, model, renk, uretim_yili, yakit_turu, durum):
        self.isim = isim
        self.model = model
        self.renk = renk
        self.uretim_yili = uretim_yili
        self.yakit_turu = yakit_turu
        self.durum = durum
    def BilgiGoster(self):
        print("İsim : {}\nModel : {}\nRenk : {}\nÜretim Yılı : {}\nYakıt Türü : {}\nDurum : {}".format(
            self.isim, self.model, self.renk, self.uretim_yili, self.yakit_turu, self.durum))
    def DurumDegistir(self, ydurum):
        self.durum = ydurum
        print("Yeni Durum : ", self.durum)
class arabalar(araclar):
    def __init__(self, isim, model, renk, uretim_yili, yakit_turu, durum, yolcu_sayisi):
        super().__init__(isim, model, renk, uretim_yili, yakit_turu, durum)
        self.yolcu_sayisi = yolcu_sayisi
class motorsikletler(araclar):
    def __init__(self, isim, model, renk, uretim_yili, yakit_turu, durum, kullanim_alani):
        super().__init__(isim, model, renk, uretim_yili, yakit_turu, durum)
        self.kullanim_alani = kullanim_alani
    def ModelDegistir(self, ykullanimalani):
        self.kullanim_alani = ykullanimalani
        print("Yeni Model : ", self.kullanim_alani)
    def BilgiGoster(self):
        print("İsim : {}\nModel : {}\nRenk : {}\nÜretim Yılı : {}\nYakıt Türü : {}\nDurum : {}\nKullanım Alanı : {}"
              .format(self.isim, self.model, self.renk, self.uretim_yili, self.yakit_turu, self.durum,
                      self.kullanim_alani))
A1 = arabalar("Reno", "Clio", "Beyaz", 2020, "Benzinli", "Aktif", 4)
A1.DurumDegistir("Pasif")
A1.BilgiGoster()
M1 = motorsikletler("Pejo", "Motosiklet", "Kırmızı", 2019, "Benzin", "Pasif", "Offroad")
M1.ModelDegistir("Şehir")
M1.BilgiGoster()
"""
