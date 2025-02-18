print("+++Kayıt+++\n")
kullanıcıadı = input("Kullanıcı Adı: ")
parola = input("Parola: ")
bakiye = 0
while True:
    print("***Giriş***\n")
    sys_kullanıcıadı = input("Kullanıcı Adı: ")
    sys_parola = input("Parola: ")

    if (sys_kullanıcıadı == kullanıcıadı and sys_parola == parola):
        bakiye += 1000
        print("Bakiyeniz ", bakiye, "$")
        while True:
            işlem = input("Ürünler\n Anakart = 750$ \n İşlemci = 500$ \n Ram = 250$ \n Laptop = 1500$ \n Almak İstediğiniz Ürünü Giriniz: ")
            if (işlem == "Anakart" and bakiye > 750):
                bakiye -= 750
                print("Yeni Bakiye: ", bakiye)
            elif (işlem == "İşlemci" and bakiye > 500):
                bakiye -= 500
                print("Yeni Bakiye: ", bakiye)
            elif (işlem == "Ram" and bakiye > 250):
                bakiye -= 250
                print("Yeni Bakiye: ", bakiye)
            elif (işlem == "Laptop" and bakiye > 1500):
                bakiye -= 1500
                print("Yeni Bakiye: ", bakiye)
            else:
                print("Bakiye Yetersiz.... \n")
                while True:
                    pk = input("Bakiye Kazanmak İsterminiz? (Y/N):  ")
                    if (pk == "Y"):
                        liste = [x for x in range(1, 21)]
                        print(liste)
                        sayı = int(input("Bir Sayı Seç: "))
                        if (sayı % 2 == 0):
                            bakiye = bakiye * sayı
                            print(bakiye, "$")
                            break
                        else:
                            print("Yanlış Seçim...")
                            exit()
                    elif(pk == "N"):
                        print("Sistemden Çıkılıyor...")
                        exit()
                    else:
                        print("İşlem Geçersiz...")




    elif (sys_kullanıcıadı != kullanıcıadı and sys_parola == parola):
        print("Kullanıcı Adınız Yanlış...")

    elif (sys_kullanıcıadı == kullanıcıadı and sys_parola != parola):
        print("Parolanız Yanlış...")
    else:
        print("Kullanıcı Adı Ve Parola Yanlış")
