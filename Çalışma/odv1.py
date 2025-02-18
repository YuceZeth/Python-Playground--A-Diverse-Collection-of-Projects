import veritabani

veritabani.baglanti()
veritabani.tablo_olustur()

while True:

    print("""
    Yeni Kişi Eklemek :1
    Kişi Sil Silmek : 2
    Kişi Bul:3
    Kişi Düzenle :4
    Rehber Bilgisi : 5
    Programdan Çıkış : 6
    """)
    secim = int(input("Seçim : "))

    if secim == 1:
        telno = int(input("Telefon Numarası : "))
        adsoyad = input("Ad-Soyad : ")
        veritabani.veri_ekle(telno, adsoyad)

    elif secim == 2:
        stelno = int(input("Silinecek Numarayı Giriniz : "))
        veritabani.veri_sil(stelno)

    elif secim == 3:
        print("Arama Yapmak İçin\nAd-Soyad 1\nTelefon Numarası 2")
        secim2 = int(input("Seçim : "))
        veritabani.veri_cekme(secim2)

    elif secim == 4:
        print("Arama Yapmak İçin\nAd-Soyad 1\nTelefon Numarası 2")
        secim3 = int(input("Seçim : "))
        veritabani.veri_guncelle(secim3)

    elif secim == 5:
        veritabani.butun_verileri_getir()

    elif secim == 6:
        a = input("Çıkmak istediğinizden emin misiniz?(E/H): ")
        if a == 'E':
            veritabani.baglanti_kapatma()
            break
        elif a == 'H':
            continue
        else:
            print("Geçersiz İşlem...")
    else:
        print("Geçersiz İşlem...")
