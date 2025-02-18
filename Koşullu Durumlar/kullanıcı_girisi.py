print("*************\nKayıt Menüsü\n*************")
sys_kullanıcı_adı = input("Kullanıcı Adı: ")
sys_parola = input("Parola: ")

print("*****\nGiriş\n*****")

kullanıcıadı = input("Kullanıcı Adını Giriniz: ")
parola = input("Parola'yı Giriniz: ")

if (sys_kullanıcı_adı == kullanıcıadı and sys_parola == parola):
    print("Hoşgeldiniz")
elif (sys_kullanıcı_adı == kullanıcıadı and sys_parola != parola):
    print("Parolanız Yanlış")
elif (sys_kullanıcı_adı != kullanıcıadı and sys_parola == parola):
    print("Kullanıcı Adınız Yanlış")
else:
    print("Kullanızı Adı Ve Parloranız Yanlış")

