import sqlite3

con = sqlite3.connect("Sirket.db")
cursor = con.cursor()


def TabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Isciler (Tc INTEGER AUTO_INCREMENT PRIMARY KEY  NOT NULL, Ad TEXT,"
                   "Soyad TEXT, Maas INT, Izingun INT, Cocuksayisi INT)")
    con.commit()


def TabloOlustur2():
    cursor.execute("CREATE TABLE IF NOT EXISTS Yoneticiler (Tc INTEGER AUTO_INCREMENT PRIMARY KEY  NOT NULL, Ad TEXT,"
                   "Soyad TEXT, Maas INT, Izingun INT)")
    con.commit()


class Islemler:
    @staticmethod
    def IsciEkleme(Tc, Ad, Soyad, Maas, Izingun, Cocuksayisi):
        try:
            cursor.execute("INSERT INTO Isciler VALUES(?,?,?,?,?,?)", (Tc, Ad, Soyad, Maas, Izingun, Cocuksayisi))
            con.commit()
        except sqlite3.IntegrityError:
            print("Tc Tekrarsız Olmalı...")

    @staticmethod
    def YoneticiEkleme(Tc, Ad, Soyad, Maas, Izingun):
        try:
            cursor.execute("INSERT INTO Yoneticiler VALUES(?,?,?,?,?)", (Tc, Ad, Soyad, Maas, Izingun))
            con.commit()
        except sqlite3.IntegrityError:
            print("Tc Tekrarsız Olmalı...")

    @staticmethod
    def CalisanSilme(Tc, Pozisyon):
        if Pozisyon == 'Isci':
            cursor.execute("Select * From Isciler where Tc = ?", (Tc,))
            liste = cursor.fetchall()
            if len(liste) == 0:
                print("Böyle Bir İşçi Yok...")
            else:
                cursor.execute("DELETE From Isciler where Tc = ?", (Tc,))
                con.commit()
        elif Pozisyon == 'Yonetici':
            cursor.execute("Select * From Yoneticiler where Tc = ?", (Tc,))
            liste = cursor.fetchall()
            if len(liste) == 0:
                print("Böyle Bir Yönetici Yok...")
            else:
                cursor.execute("DELETE From Yoneticiler where Tc = ?", (Tc,))
                con.commit()

    @staticmethod
    def IsciGuncelle(Tc, Ad, Soyad, Maas, Izingun, Cocuksayisi, Dg):
        if Dg == 1:
            cursor.execute("Update Isciler set Ad = ? where Tc = ?", (Ad, Tc))
            con.commit()
        elif Dg == 2:
            cursor.execute("Update Isciler set Soyad = ? where Tc = ?", (Soyad, Tc))
            con.commit()
        elif Dg == 3:
            cursor.execute("Update Isciler set Maas = ? where Tc = ?", (Maas, Tc))
            con.commit()
        elif Dg == 4:
            cursor.execute("Update Isciler set Izingun = ? where Tc = ?", (Izingun, Tc))
            con.commit()
        elif Dg == 5:
            cursor.execute("Update Isciler set Cocuksayisi = ? where Tc = ?", (Cocuksayisi, Tc))
            con.commit()
        else:
            print("Geçersiz İşlem...")

    @staticmethod
    def YoneticiGuncelle(Tc, Ad, Soyad, Maas, Izingun, Dg):
        if Dg == 1:
            cursor.execute("Update Yoneticiler set Ad = ? where Tc = ?", (Ad, Tc))
            con.commit()
        elif Dg == 2:
            cursor.execute("Update Yoneticiler set Soyad = ? where Tc = ?", (Soyad, Tc))
            con.commit()
        elif Dg == 3:
            cursor.execute("Update Yoneticiler set Maas = ? where Tc = ?", (Maas, Tc))
            con.commit()
        elif Dg == 4:
            cursor.execute("Update Isciler set Izingun = ? where Tc = ?", (Izingun, Tc))
            con.commit()
        else:
            print("Geçersiz İşlem...")

    @staticmethod
    def VerileriAl(Pozisyon):
        if Pozisyon == 'Isci':
            cursor.execute("Select * From Isciler")
            liste = cursor.fetchall()
            if len(liste) == 0:
                print("İşçi Bulunmuyor...")
            else:
                for i in liste:
                    print("Tc: ", i[0])
                    print("Ad: ", i[1])
                    print("Soyad: ", i[2])
                    print("Maas: ", i[3])
                    print("İzin Günü: ", i[4])
                    print("Çocuk Sayısı: ", i[5])

        elif Pozisyon == 'Yonetici':
            cursor.execute("Select * From Yoneticiler")
            liste = cursor.fetchall()
            if len(liste) == 0:
                print("Yönetici Bulunmuyor...")
            else:
                for i in liste:
                    print("Tc: ", i[0])
                    print("Ad: ", i[1])
                    print("Soyad: ", i[2])
                    print("Maas: ", i[3])
                    print("İzin Günü: ", i[4])

    @staticmethod
    def VerileriAl2(Tc, Pozisyon):
        if Pozisyon == 'Isci':
            cursor.execute("Select * From Isciler where Tc = ?", (Tc,))
            liste = cursor.fetchone()
            if len(liste) == 0:
                print("Böyle Bir İşçi Bulunmuyor...")
            else:
                print("Tc: ", str(liste[0]))
                print("Ad: ", str(liste[1]))
                print("Soyad: ", str(liste[2]))
                print("Maas: ", str(liste[3]))
                print("İzin Günü: ", str(liste[4]))
                print("Çocuk Sayısı: ", str(liste[5]))

        elif Pozisyon == 'Yonetici':
            cursor.execute("Select * From Isciler where Tc = ?", (Tc,))
            liste = cursor.fetchone()
            if len(liste) == 0:
                print("Böyle Bir Yönetici Bulunmuyor...")
            else:
                print("Tc: ", str(liste[0]))
                print("Ad: ", str(liste[1]))
                print("Soyad: ", str(liste[2]))
                print("Maas: ", str(liste[3]))
                print("İzin Günü: ", str(liste[4]))

    @staticmethod
    def Iverilerial():
        cursor.execute("Select * From Isciler")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("İşçi Bulunmuyor...")
        else:
            for i in liste:
                print("Tc: ", i[0])
                print("Ad: ", i[1])
                print("Soyad: ", i[2])
                print("Maas: ", i[3])
                print("İzin Günü: ", i[4])
                print("Çocuk Sayısı: ", i[5])

    @staticmethod
    def Terfi(Tc, Ad, Soyad, Maas, Izingun):
        Islemler.Iverilerial()
        cursor.execute("DELETE From Isciler where Tc = ?", (Tc,))
        con.commit()
        cursor.execute("INSERT INTO Yoneticiler VALUES(?,?,?,?,?)", (Tc, Ad, Soyad, Maas, Izingun))
        con.commit()


TabloOlustur()
TabloOlustur2()
Islemler = Islemler()

print("\n1.Çalışanları Göster\n2.Seçili Çalışanı Göster\n3.Çalışan Ekle\n4.Çalışan Sil\n5.Çalışan "
      "Güncelle\n6.Terfi\nÇıkmak İçin '0'")

while True:
    islem = int(input("İşlem Giriniz: "))

    if islem == 1:
        pozisyon = input("Pozisyon Giriniz :")
        Islemler.VerileriAl(pozisyon)

    elif islem == 2:
        pozisyon = input("Pozisyon Giriniz :")
        tc = int(input("Gösterilecek Çalışanın Tc'sini Giriniz :"))
        Islemler.VerileriAl2(tc, pozisyon)

    elif islem == 3:
        pozisyon = input("Pozisyon Giriniz :")
        if pozisyon == 'Isci':
            tc = int(input("Tc: "))
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            izingun = int(input("İzin Gün Giriniz :"))
            cocuksayisi = int(input("Çocuk Sayısını Giriniz :"))
            if 0 <= cocuksayisi < 3:
                maas = 2350 + 150
                Islemler.IsciEkleme(tc, ad, soyad, maas, izingun, cocuksayisi)
            elif 3 <= cocuksayisi < 5:
                maas = 2350 + 250
                Islemler.IsciEkleme(tc, ad, soyad, maas, izingun, cocuksayisi)
            elif 5 <= cocuksayisi:
                maas = 2350 + 650
                Islemler.IsciEkleme(tc, ad, soyad, maas, izingun, cocuksayisi)
        elif pozisyon == 'Yonetici':
            tc = int(input("Id: "))
            ad = input("Malzeme ismi: ")
            soyad = input("Adet: ")
            izingun = int(input("İzin Gün Giriniz :"))
            maas = 5000
            Islemler.YoneticiEkleme(tc, ad, soyad, maas, izingun)

    elif islem == 4:
        pozisyon = input("Pozisyon Giriniz :")
        tc = int(input("Silinecek Malzemenin İsmini Giriniz: "))
        Islemler.CalisanSilme(tc, pozisyon)

    elif islem == 5:
        pozisyon = input("Pozisyon Giriniz :")
        if pozisyon == 'Isci':
            tc = int(input("Güncellenecek Çalışanın Tc'si :"))
            cursor.execute("Select * From Isciler where Tc = ?", (tc,))
            li = cursor.fetchone()
            if len(li) == 0:
                print("Böyle Bir İşçi Bulunmuyor...")
            else:
                print("Ad 1\nSoyad 2\nMaas 3\nİzin Günü 4\nÇocuk Sayısı 5")
                dg = int(input("Değiştirilecek Özelliği Giriniz : "))
                if dg == 1:
                    nad = input("Yeni Ad :")
                    Islemler.IsciGuncelle(tc, nad, li[2], li[3], li[4], li[5], dg)
                elif dg == 2:
                    nsoyad = input("Yeni Soyad :")
                    Islemler.IsciGuncelle(tc, li[1], nsoyad, li[3], li[4], li[5], dg)
                elif dg == 3:
                    nmaas = input("Yeni Maaş :")
                    Islemler.IsciGuncelle(tc, li[1], li[2], nmaas, li[4], li[5], dg)
                elif dg == 4:
                    nizingun = input("Yeni İzin Günü :")
                    Islemler.IsciGuncelle(tc, li[1], li[2], li[3], nizingun, li[5], dg)
                elif dg == 5:
                    ncocuksayisi = input("Yeni Çocuk Sayısı :")
                    Islemler.IsciGuncelle(tc, li[1], li[2], li[3], li[4], ncocuksayisi, dg)
                else:
                    print("Geçersiz İşlem...")

        elif pozisyon == 'Yonetici':
            tc = int(input("Güncellenecek Çalışanın Tc'si :"))
            cursor.execute("Select * From Yoneticiler where Tc = ?", (tc,))
            li = cursor.fetchone()
            if len(li) == 0:
                print("Böyle Bir Yönetici Bulunmuyor...")
            else:
                print("Ad 1\nSoyad 2\nMaas 3\nİzin Günü 4")
                dg = int(input("Değiştirilecek Özelliği Giriniz : "))
                if dg == 1:
                    nad = input("Yeni Ad :")
                    Islemler.IsciGuncelle(tc, nad, li[2], li[3], li[4], li[5], dg)
                elif dg == 2:
                    nsoyad = input("Yeni Soyad :")
                    Islemler.IsciGuncelle(tc, li[1], nsoyad, li[3], li[4], li[5], dg)
                elif dg == 3:
                    nmaas = input("Yeni Maaş :")
                    Islemler.IsciGuncelle(tc, li[1], li[2], nmaas, li[4], li[5], dg)
                elif dg == 4:
                    nizingun = input("Yeni İzin Günü :")
                    Islemler.IsciGuncelle(tc, li[1], li[2], li[3], nizingun, li[5], dg)
                else:
                    print("Geçersiz İşlem...")
    elif islem == 6:
        tc = int(input("Terfi Edilecek Çalışanın Tc'si :"))
        cursor.execute("Select * From Isciler where Tc = ?", (tc,))
        li = cursor.fetchone()
        if len(li) == 0:
            print("Böyle Bir Çalışan Bulunmuyor...")
        else:
            Islemler.Terfi(li[0], li[1], li[2], 5000, li[4])
    elif islem == 0:
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz İşlem...")

con.close()
