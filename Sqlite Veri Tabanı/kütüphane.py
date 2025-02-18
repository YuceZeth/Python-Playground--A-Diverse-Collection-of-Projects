import sqlite3

con = sqlite3.connect("gelismiskütüphane.db")
cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()


class kitaplar:

    @staticmethod
    def kitap_ekleme(kitap_isim, yazar, yayinevi, sayfa_saysisi):
        cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)", (kitap_isim, yazar, yayinevi, sayfa_saysisi,))
        con.commit()

    @staticmethod
    def verileri_al():
        cursor.execute("Select * From kitaplık")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("kitap bulunmuyor")
        else:
            for i in liste:
                print("Kitap İsmi: ", i[0])
                print("Yazar: ", i[1])
                print("Yayınevi: ", i[2])
                print("Sayfa Sayısı: ", i[3])

    @staticmethod
    def verileri_al2(yazar):
        cursor.execute("Select * From kitaplık where Yazar = ?", (yazar,))
        liste = cursor.fetchone()
        if len(liste) == 0:
            print("kitap bulunmuyor...")
        else:
            print("Kitap ismi: ", str(liste[0]))
            print("Yazar: ", str(liste[1]))
            print("Yayınevi: ", str(liste[2]))
            print("Sayfa Sayısı: ", str(liste[3]))

    @staticmethod
    def verileri_guncelle(eski_yayinevi, yeni_yayinevi):
        cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?", (yeni_yayinevi, eski_yayinevi))
        con.commit()

    @staticmethod
    def verileri_sil(yazar):
        cursor.execute("Select * From kitaplık where Yazar = ?", (yazar,))
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Yazarın Kitabı Yok...")
        else:
            cursor.execute("DELETE From kitaplık where Yazar = ?", (yazar,))
            con.commit()


tablo_olustur()
kitaplar = kitaplar()

print("""
    1.Verileri Göster
    2.Seçili Veriyi Göster
    3.Veri Ekle
    4.Veri Sil
    5.Veri Güncelle
    6.Çıkmak İçin 'q' Giriniz
""")

while True:
    islem = input("İşlemi Giriniz: ")

    if islem == "1":
        kitaplar.verileri_al()

    elif islem == "2":
        Yazar = input("Gösterilecek Kitabın/Kitapların Yazarını Giriniz: ")
        kitaplar.verileri_al2(Yazar)

    elif islem == "3":
        Kitap_isim = input("Kitap İsimi: ")
        Yazar = input("Yazar: ")
        Yayinevi = input("Yayınevi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        kitaplar.kitap_ekleme(Kitap_isim, Yazar, Yayinevi, sayfa_sayisi)

    elif islem == "4":
        Yazar = input("Silinecek Kitabın/Kitapların Yazarını Giriniz: ")
        kitaplar.verileri_sil(Yazar)

    elif islem == "5":
        Yayinevi = input("Değiştirilecek Yayınevini Giriniz: ")
        Yeni_yayinevi = input("Yeni Yayınevi Giriniz: ")
        kitaplar.verileri_guncelle(Yayinevi, Yeni_yayinevi)

    elif islem == "q":
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz İşlem...")

con.close()
