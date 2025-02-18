import time
class bilgisayar():
    def __init__(self,anakart = "Bilgi Yok", işlemci = "Bilgi Yok",ram = "Bilgi Yok",ekran_kartı = "Bilgi Yok"):
        self.anakart = anakart
        self.işlemci = işlemci
        self.ram = ram
        self.ekran_kartı = ekran_kartı

    def __str__(self):
        return "Anakart : {} \nİşlemci : {} \nRam : {} \nEkran Kartı : {} ".format(self.anakart,self.işlemci,self.ram,self.ekran_kartı)

    def anakart_değişim(self,yeni_anakart):
        print("Anakart Değiştiriliyor...")
        self.anakart = yeni_anakart
        time.sleep(1)
        print("Anakart Değiştirildi....")

    def işlemci_değişim(self,yeni_işlemci):
        print("İşlemci Değiştiriliyor...")
        self.işlemci = yeni_işlemci
        time.sleep(1)
        print("İşlemci Değiştirildi....")

    def ekran_kartı_değişim(self,yeni_ekran_kartı):
        print("Ekran Kartı Değiştiriliyor...")
        self.ekran_kartı = yeni_ekran_kartı
        time.sleep(1)
        print("Ekran Kartı Değiştirildi....")

    def ram_değiştirme(self,yeni_ram):
        print("Ram Değiştiriliyor...")
        self.ram = yeni_ram
        time.sleep(1)
        print("Ram Değiştirildi...")


bilgisayar = bilgisayar()
print("""
Bilgisayarcı

1.Anakart Değiştirme
2.İşlemci Değiştirme
3.Ram Değiştirme
4.Ekran Kartı Değiştime
5.Bilgisayarın Durumu
Çıkmak için 'q' ya basınız



""")
while True:
    işlem = input("İşlemi Seçiniz : ")

    if(işlem=="q"):
        print("Çıkılıyor....")
        break

    elif(işlem=="1"):
        anakart = input("Anakartı Giriniz : ")
        bilgisayar.anakart_değişim(anakart)

    elif(işlem=="2"):
        işlemci = input("İşlemci Giriniz : ")
        bilgisayar.işlemci_değişim(işlemci)

    elif(işlem=="3"):
        ram = input("Ram Giriniz : ")
        bilgisayar.ram_değiştirme(ram)

    elif(işlem=="4"):
        ekran_kartı = input("Ekran Kartı Giriniz : ")
        bilgisayar.ekran_kartı_değişim(ekran_kartı)

    elif(işlem=="5"):
        print(bilgisayar)

    else:
        print("Geçersiz İşlem")
































