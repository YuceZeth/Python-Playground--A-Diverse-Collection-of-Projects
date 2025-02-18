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
        print("Uçak Bilgileri :\nUçak Adı : {}\nUçak Kodu : {}\nUçak Türü :{}\nÜretim Yılı : {}\nYolcu Kapasitesi : {}"
              "\nUçak Bakım :{}".format(self.ucak_adi, self.ucak_kodu, self.ucak_turu, self.uretim_yili,
                                        self.yolcu_kapasitesi, self.ucak_bakim))


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
        print("Yolcu Bilgileri :\nAd-Soyad : {}\nYolcu TC : {}\nYaş :{}\nMil : {}".format(self.yolcu_adi_soyadi,
                                                                                          self.yolcu_tc, self.yolcu_tc,
                                                                                          self.yolcu_mil))


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
        Ucak1 = Ucak(ucak_adi, ucak_kodu, ucak_turu, uretim_yili,
                     yolcu_kapasitesi, ucak_bakim)
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
        print(
            "Uçuş Bilgileri :\nUçuş Adı : {}\nUçuş Kodu : {}\nUçuş Tarihi: {}\nKalkış Yeri : {}\nİniş Yeri : {}".format(
                self.ucus_adi, self.ucus_kodu, self.ucus_tarihi, self.kalkis_yeri, self.inis_yeri))


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
