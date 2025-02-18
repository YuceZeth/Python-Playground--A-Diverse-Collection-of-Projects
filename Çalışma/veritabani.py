import sqlite3

con = sqlite3.connect("Trehberi.db")
cursor = con.cursor()


def baglanti():
    if cursor:
        print("Bağlantı Başarılı...")


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kisiler (tel_no INT PRIMARY KEY, ad_soyad TEXT)")
    con.commit()


def veri_ekle(telno, adsoyad):
    try:
        cursor.execute("INSERT INTO Kisiler Values(?,?)", (telno, adsoyad))
        con.commit()
        print("Başarı İle Kişi Eklendi...")
    except sqlite3.IntegrityError:
        print("Telefon Numarası Tekrarsız Olmalı...")


def veri_sil(stelno):
    cursor.execute("Delete From Kisiler Where tel_no = ?", (stelno,))
    con.commit()
    print("Silme İşlemi Başarıyla Tamamlandı...")


def veri_cekme(secim):
    if secim == 1:
        adsoyad = input("Ad-Soyad Giriniz : ")
        cursor.execute("Select * From Kisiler")
        kisiler = cursor.fetchall()
        hata = 0
        for i in kisiler:
            if i[1] == adsoyad:
                print(i)
            else:
                hata = hata + 1

        if hata == len(kisiler):
            print("Kişi Mevcut Değil...")

    elif secim == 2:
        telno = int(input("Telefon Numarasını Giriniz : "))
        cursor.execute("Select * From Kisiler")
        kisiler = cursor.fetchall()
        hata = 0
        for i in kisiler:
            if i[0] == telno:
                print(i)
            else:
                hata = hata + 1

        if hata == len(kisiler):
            print("Kişi Mevcut Değil...")

    else:
        print("Geçersiz İşlem...")


def veri_guncelle(secim):
    if secim == 1:
        adsoyad = input("Ad-Soyad Giriniz : ")
        cursor.execute("Select * From Kisiler")
        kisiler = cursor.fetchall()
        hata = 0
        for i in kisiler:
            if i[1] == adsoyad:
                print("Düzenleme İçin\nAd-Soyad 1\nTelefon Numarası 2")
                secim4 = int(input("Seçim : "))
                if secim4 == 1:
                    yadsoyad = input("Yeni Ad Soyad : ")

                    cursor.execute("UPDATE Kisiler set ad_soyad = ? Where ad_soyad = ?", (yadsoyad, adsoyad))
                    con.commit()
                    print("Düzenleme Başarıyla Gerçekleştirildi...")
                elif secim4 == 2:

                    ytelno = input("Yeni Telefon Numarası : ")
                    cursor.execute("UPDATE Kisiler set tel_no = ? Where ad_soyad = ?", (ytelno, adsoyad))
                    con.commit()
                    print("Düzenleme Başarıyla Gerçekleştirildi...")
                else:
                    print("Geçersiz İşlem...")
            else:
                hata = hata + 1
        if hata == len(kisiler):
            print("Kişi Mevcut Değil...")

    elif secim == 2:
        telno = int(input("Telefon Numarası Giriniz : "))
        cursor.execute("Select * From Kisiler")
        kisiler = cursor.fetchall()
        hata = 0
        for i in kisiler:
            if i[0] == telno:
                print("Düzenleme İçin\nAd-Soyad 1\nTelefon Numarası 2")
                secim4 = int(input("Seçim : "))
                if secim4 == 1:
                    yadsoyad = input("Yeni Ad Soyad : ")
                    cursor.execute("UPDATE Kisiler set ad_soyad = ? Where tel_no = ?", (yadsoyad, telno))
                    con.commit()
                    print("Düzenleme Başarıyla Gerçekleştirildi...")
                elif secim4 == 2:
                    ytelno = input("Yeni Telefon Numarası : ")
                    cursor.execute("UPDATE Kisiler set tel_no = ? Where tel_no = ?", (ytelno, telno))
                    con.commit()
                    print("Düzenleme Başarıyla Gerçekleştirildi...")
                else:
                    print("Geçersiz İşlem...")
            else:
                hata = hata + 1
        if hata == len(kisiler):
            print("Kişi Mevcut Değil...")
    else:
        print("Geçersiz İşlem...")


def butun_verileri_getir():
    cursor.execute("Select * From Kisiler")
    data = cursor.fetchall()
    print("Rehberinizde {} Kişi vardır...".format(len(data)))


def baglanti_kapatma():
    print("Çıkılıyor...")
    con.close()
