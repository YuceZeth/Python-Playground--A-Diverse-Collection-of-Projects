import random
import time


class kumanda:
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi = ["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon Zaten Açık...")
        else:
            print("Televizyon Açılıyor....")
            self.tv_durum = "Açık"

    def tv_kapat(self):

        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı...")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            islem = input("Sesi Azalt = '-' \nSesi Arttır = '+' \nÇıkış = Çık \nİşlem= ")
            if islem == "-" and self.tv_ses == 0:
                print("Ses Daha Fazla Azaltılamaz....")

            elif islem == "-" and self.tv_ses != 0:
                print("Ses Azaltılıyor...")
                self.tv_ses -= 1
                print("Ses: ", self.tv_ses)

            elif islem == "+" and self.tv_ses == 10:
                print("Ses Daha Fazla Arttırılamaz....")

            elif islem == "+" and self.tv_ses != 10:
                print("Ses Arttırılıyor...")
                self.tv_ses += 1
                print("Ses: ", self.tv_ses)

            elif islem == "Çık":
                print("Çıkılıyor...")
                print("Ses Güncellendi", self.tv_ses)
                break

    def kanal_ekle(self, yeni_kanal):
        print("Kanal Ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(yeni_kanal)
        print("Kanal Eklendi")

    def kanal_silme(self, silinecek_kanal):
        print("Kanal Siliniyor...")
        self.kanal_listesi.remove(silinecek_kanal)
        time.sleep(1)
        print("Kanal Silindi....")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {} \nTv Ses: {} \nKanal Listesi: {} \nŞu Anki Kanal: {}".format(self.tv_durum, self.tv_ses,
                                                                                           self.kanal_listesi,
                                                                                           self.kanal)


kumanda = kumanda()

print("""
1.Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Silme

6.Kanal Sayısını Öğrenme

7.Rastgele Kanala Geçme

8.Televizyoz Bilgileri

Çıkmak için 'q' ya basınız
""")

while True:
    islem = input("İşlem Giriniz: ")

    if islem == "q":
        print("Programdan Çıkılıyor....")
        break

    elif islem == "1":
        kumanda.tv_ac()

    elif islem == "2":
        kumanda.tv_kapat()

    elif islem == "3":
        kumanda.ses_ayarlari()

    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz : ")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif islem == "5":
        print(kumanda.kanal_listesi)
        silinecek_kanal = input("Silinecek Kanalı Giriniz: ")
        kumanda.kanal_silme(silinecek_kanal)

    elif islem == "6":
        print("Kanal Sayısı : ", len(kumanda))

    elif islem == "7":
        kumanda.rastgele_kanal()

    elif islem == "8":
        print(kumanda)
    else:
        print("Geçersiz İşlem....")
