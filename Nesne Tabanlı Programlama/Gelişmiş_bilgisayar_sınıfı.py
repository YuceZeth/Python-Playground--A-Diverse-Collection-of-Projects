import time

class Yönetici():

    def __init__(self,id="",parola="",ram_listesi=[],ram_sayısı=[]):
        self.id = "kaan"
        self.parola = "123"
        self.ram_listesi = ram_listesi
        self.ram_sayısı = ram_sayısı

    def ram_ekleme(self, ram_ismi, ram_stoku):
        self.ram_listesi.append(ram_ismi)
        self.ram_sayısı.append(ram_stoku)

    def __str__(self):
        return "Ram Listesi : {} \nRam Stoğu : {}".format(self.ram_listesi,self.ram_sayısı)

class müşteri(Yönetici):
    def ram_alma(self,ram_ismi,ram_adedi):
        if ram_ismi in yönetici.ram_listesi:
            print("Stokda Var")
            yönetici.ram_sayısı[0] = yönetici.ram_sayısı[0]-ram_adedi


müşteri = müşteri()

yönetici = Yönetici()
print("Yönetici Girişi İçin = 1 \nMuşteri Girişi İçin = 2")
while True:
    işlem = input("İşlem = ")
    if(işlem=="1"):
        while True:
            print("Çıkmak İçin Kullanıcı Adını Ve Parolayı 'q' Giriniz")
            id = input("Kullanıcı Adı Giriniz : ")
            parola = input("Parola Giriniz : ")

            if(id == yönetici.id and parola == yönetici.parola ):
                print("Giriş Yapılıyor...\n")
                time.sleep(1)
                print("""
                1.Ram Ekleme
                2.Stok Göster 
                Çıkış için 'q' ya basınız
                """)
                while True:
                    işlem = input("İşlem Seçiniz : ")
                    if(işlem=="q"):
                        print("Çıkılıyor.....")
                        break

                    elif(işlem=="1"):
                        ram_ismi = input("Ram İsmini Giriniz :")
                        time.sleep(1)
                        ram_stoku = int(input("Ram Stoğunu Giriniz : "))
                        time.sleep(1)
                        yönetici.ram_ekleme(ram_ismi,ram_stoku)

                    elif(işlem=="2"):
                        print(yönetici)

            elif (id == "q" and parola == "q"):
                print("Yönetici Panelinden Çıkılıyor.....")
                break
            elif(id != yönetici.id and parola == yönetici.parola):
                print("Kullanıcı Adı Yanlış....")
            elif(id == yönetici.id and parola != yönetici.parola):
                print("Parola Yanlış....")
            elif(id != yönetici.id and parola != yönetici.parola):
                print("Kullanıcı Adı Ve Parola Yanlış....")
            else:
                print("Geçersiz İşlem.....")

    elif(işlem=="2"):
        print(yönetici)
        ram_ismi=input("İsim gir : ")
        ram_adedi=int(input("Adet Giriniz : "))
        müşteri.ram_alma(ram_ismi,ram_adedi)

    














    else:
        print("Geçeriz İşlem.............")










































