
class Ucak:
    def __init__(self, ucak_adi, ucak_kodu, ucak_turu, uretim_yili, yolcu_kapasitesi, ucak_bakim):
        self.ucak_adi = ucak_adi
        self.ucak_kodu = ucak_kodu
        self.ucak_turu = ucak_turu
        self.uretim_yili = uretim_yili
        self.yolcu_kapasitesi = yolcu_kapasitesi
        self.ucak_bakim = ucak_bakim

    def Ucak_Bakim_Tanimla(self, ucak_bakim):
        self.ucak_bakim = ucak_bakim
        
    def Ucak_Bakim_Durum(self):
        print("Uçağın Bakım Durumu : ", self.ucak_bakim)

    def Ucak_Bilgi_Goster(self):
        print("Uçak Bilgileri :\nUçak Adı : {}\nUçak Kodu : {}\nUçak Türü : {}\nÜretim Yılı : {}\n"
              "Yolcu Kapasitesi : {}\nUçak Bakım :{}".format(self.ucak_adi, self.ucak_kodu, self.ucak_turu,
                                                              self.uretim_yili, self.yolcu_kapasitesi, self.ucak_bakim))
class Yolcu:
    def __init__(self, yolcu_adi_soyadi, yolcu_tc, yolcu_yasi, yolcu_mil):
        self.yolcu_adi_soyadi = yolcu_adi_soyadi
        self.yolcu_tc = yolcu_tc
        self.yolcu_yasi = yolcu_yasi
        self.yolcu_mil = yolcu_mil

    def Mil_Ekle(self, bilet_parasi):
        self.yolcu_mil = self.yolcu_mil + bilet_parasi * 0.1

    def Mil_Goster(self):
        print("Yolcu Mili : ", self.yolcu_mil)

    def Yolcu_Bilgi_Goster(self):

        print("Yolcu Bilgileri :\nAd-Soyad : {}\nYolcu TC : {}\nYaş : {}\nMil : {}"
              .format(self.yolcu_adi_soyadi, self.yolcu_tc, self.yolcu_tc, self.yolcu_mil))
class Ucus:
    def __init__(self, ucus_adi, ucus_kodu, ucus_tarihi, kalkis_yeri, inis_yeri, yolcular=[], ucaklar=[]):
        self.ucus_adi = ucus_adi
        self.ucus_kodu = ucus_kodu
        self.ucus_tarihi = ucus_tarihi
        self.kalkis_yeri = kalkis_yeri
        self.inis_yeri = inis_yeri
        self.yolcular = yolcular
        self.ucaklar = ucaklar

    def Ucus_Ucagi_Ekle(self, ucak_adi, ucak_kodu, ucak_turu, uretim_yili, yolcu_kapasitesi, ucak_bakim):
        Ucak1 = Ucak(ucak_adi, ucak_kodu, ucak_turu, uretim_yili, yolcu_kapasitesi, ucak_bakim)
        self.ucaklar.append(Ucak1)

    def Ucak_Goster(self):
        for j in self.ucaklar:
            print(j.Ucak_Bilgi_Goster())

    def Yolcu_Ekle(self, yolcu_adi_soyadi, yolcu_tc, yolcu_yasi, yolcu_mil):
        Yolcu1 = Yolcu(yolcu_adi_soyadi, yolcu_tc, yolcu_yasi, yolcu_mil)
        self.yolcular.append(Yolcu1)

    def Yolcu_Goster(self):
        for k in self.yolcular:
            print(k.Yolcu_Bilgi_Goster())

    def Ucus_Bilgi_Goster(self):
        print("Uçuş Bilgileri :\nUçuş Adı : {}\nUçuş Kodu : {}\nUçuş Tarihi : {}\nKalkış Yeri : {}\nİniş Yeri : {}"
              .format(self.ucus_adi, self.ucus_kodu, self.ucus_tarihi, self.kalkis_yeri, self.inis_yeri))

Ucus1 = Ucus("BKE31", "TK223", "21-10-2021", "İstanbul", "Amsterdam")
Ucus1.Ucus_Ucagi_Ekle("Alpha 1", "TC-A25", "Yolcu", 2015, 350, "true")

for i in range(1, 6):
    yolcu_ad_soyad = input("Ad-Soyad : ")
    yolcutc = input("TC : ")
    yolcu_yas = input("Yaş : ")
    yolcu_mili = input("Mil : ")
    Ucus1.Yolcu_Ekle(yolcu_ad_soyad, yolcutc, yolcu_yas, yolcu_mili)

Ucus1.Ucus_Bilgi_Goster()
Ucus1.Ucak_Goster()
Ucus1.Yolcu_Goster()

"""
class yonetici:
    def __init__(self, id="kaan", passw="123", calisanlar=[""]):
        self.id = id
        self.passw = passw
        self.calisanlar = calisanlar
    def calisan_ekle(self, ad, tc, maas):
        self.calisanlar.append(ad)
        self.calisanlar.append(tc)
        self.calisanlar.append(maas)
        print(self.calisanlar)
    def calisan_sil(self, tc):
        k = 0
        for i in range(1, len(self.calisanlar)):
            if self.calisanlar[i] == tc:
                self.calisanlar.pop(i + 1)
                self.calisanlar.pop(i)
                self.calisanlar.pop(i - 1)
                print(self.calisanlar)
                break
            else:
                k = k + 1
            if k == len(self.calisanlar) - 1:
                print("Böyle bir çalışan yok")
    def maas_arttir(self, tc, ymaas):
        k = 0
        for i in range(0, len(self.calisanlar) - 1):
            if self.calisanlar[i] == tc:
                self.calisanlar[i + 1] = self.calisanlar[i + 1] + ymaas
                print(self.calisanlar)
            else:
                k = k + 1
            if k == len(self.calisanlar) - 1:
                print("Böyle bir çalışan yok...")
print("Panel...Çalışan  girişi  için 1Yönetici girişi için 2")
yonetici = yonetici()
secim = int(input("Seçim : "))
if secim == 1:
    print("İşe HG")
elif secim == 2:
    while True:
        ka = input("Kullanıcı adı : ")
        passw = input("Şifre : ")
        if yonetici.id == ka and yonetici.passw == passw:
            while True:
                print("Çalışan ekle 1Çalışan sil  2Maas arttır  3Çıkmak için  0")
                secim2 = int(input("Seçim : "))
                if secim2 == 1:
                    kad = input("Adınızı giriniz : ")
                    ktc = int(input("TC : "))
                    kmaas = int(input("Maas : "))
                    yonetici.calisan_ekle(kad, ktc, kmaas)
                elif secim2 == 2:
                    print(yonetici.calisanlar)
                    stc = int(input("Silinecek tc gir : "))
                    yonetici.calisan_sil(stc)
                elif secim2 == 3:
                    print(yonetici.calisanlar)
                    mtc = int(input("Maaşı arttırılacak calışan tcsi : "))
                    mas = int(input("Zam miktarı : "))
                    yonetici.maas_arttir(mtc, mas)
                elif secim == 0:
                    print("bb")
                    break
                else:
                    print("Geçersiz işlem...")
        else:
            print("Yanlış kullanıcı adı şifre...")
"""
"""
class Satici:
    def __init__(self, ram_adedi = 10, ram_para = 350, kad="kaan", sifre="123"):
        self.kad = kad
        self.sifre = sifre
        self.ram_adedi = ram_adedi
        self.ram_para = ram_para
    def ram_ekle(self, adet):
        self.ram_adedi = self.ram_adedi + adet
        print("Ram Adedi : ", self.ram_adedi)
    def ram_satis(self, sadet):
        if self.ram_adedi >= sadet:
            if alici.para >= sadet*satici.ram_para:
                self.ram_adedi = self.ram_adedi - sadet
                print("Ram'ler Kargolanmıştır...\n")
            else:
                print("Yetersiz Bakiye...\n")
        else:
            print("Yeterli Ram Adedi Bulunmamaktadır...\n")
class Alici:
    def __init__(self, para = 350):
        self.para = para
    def para_ekle(self, ypara):
        self.para = self.para + ypara
        print("Yeni Para : ", self.para)
alici = Alici()
satici = Satici()
while True:
    print("Müşteri Girişi 1\nYönetici Girişi 2")
    secim = int(input("Seçim : "))
    if secim == 1:
        print("Ram Almak İçin 1\nPara Eklemek İçin 2")
        secim3 = int(input("Seçim : "))
        if secim3 == 1:
            salis = int(input("Kaç Adet Ram Alınacak : "))
            satici.ram_satis(salis)
        elif secim3 == 2:
            epara = int(input("Para Miktarı : "))
            alici.para_ekle(epara)
        else:
            print("Geçersiz İşlem...\n")
    elif secim == 2:
        kadi = input("Kullanıcı Adı : ")
        sire = input("Şifre : ")
        if kadi == satici.kad and sire == satici.sifre:
            while True:
                print("Ram Eklemek İçin 1\nÇıkmak İçin 0")
                secim2 = int(input("Seçim : "))
                if secim2 == 1:
                    ram = int(input("Kaç Adet Ram Eklenecek : "))
                    satici.ram_ekle(ram)
                elif secim2 == 0:
                    break
                else:
                    print("Geçersiz İşlem...")
        else:
            print("Yanlış Kullnıcı Adı Şifre...")
"""