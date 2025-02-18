a = int(input("Birinci Sayıyı Giriniz: "))
b = int(input("İkinci Sayıyı Giriniz: "))
işlem = input("İşlemi Giriniz (İşlem Sembolü): ")


if (işlem == '+'):
    print("{} İle {} Toplamı {} ".format(a,b,a+b))
elif (işlem == '-'):
    print("{} İle {} Çıkması {}".format(a,b,a-b))
elif (işlem == '*'):
    print("{} İle {} Çarpılması {} ".format(a,b,a*b))
elif (işlem == '/'):
    try:
        print("{} İle {} Bölünmesi {}".format(a,b,a/b))
    except ZeroDivisionError:
        print("Sayı 0 a bölünemez")
else:
    print("Dört İşlem Dışında İşlem Yapılmaz!!!!!!")

