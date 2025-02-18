print("""

*************************
Kullanıcı Girişi Programı
*************************

""")


kullanıcıadı = input("Kullanıcı Adı: ")
parola = input("Parola: ")

giris_hakkı=3

while True:

    sys_kullanıcı_adı = input("Kullanıcı Adını Giriniz: ")
    sys_parola = input("Parola'yı Giriniz: ")

    if (sys_kullanıcı_adı != kullanıcıadı and sys_parola == parola):
        print("\nKullanıcı Adı Hatalı...\n")
        giris_hakkı -=1

    elif (sys_kullanıcı_adı == kullanıcıadı and sys_parola != parola):
        print("\nŞifre Hatalı...\n")
        giris_hakkı -= 1

    elif (sys_kullanıcı_adı != kullanıcıadı and sys_parola != parola):
        print("\nKullanıcı Adı Ve Şifre Hatalı...\n")
        giris_hakkı -= 1

    else:
        print("Giriş Yapılıyor...")
        break

    if (giris_hakkı == 0):
        print("Giriş Hakkını Bitti....")
        break


