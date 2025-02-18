print("""

************************
Atm Makinesine Hoşgelniz
************************

İşlemler; 

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Çıkmak İçin 'q' Giriniz

************************

""")

bakiye = 1000

while True:
    işlem = input("İşlem Giriniz: ")

    if(işlem == '1'):
        print("Bakiyeniz: ",bakiye)

    elif (işlem == '2'):
        miktar = int(input("Yatırmak İstediğiniz Miktar: "))
        bakiye = bakiye + miktar
        print("Paranız Yüklenmiştir Yeni Bakiye: ",bakiye)

    elif (işlem == '3'):
        çmiktar = int(input("Çekilecek Miktarı Giriniz: "))
        if(çmiktar>bakiye):
            print("Bakiye Yetersiz")
        else:
            bakiye = bakiye - çmiktar
            print("Para Çekilmiştir Yeni Bakiye: ",bakiye)

    elif(işlem == 'q'):
        print("Çıkış Yapılıyor...")
        break

    else:
        print("Geçersiz İşlem...")

