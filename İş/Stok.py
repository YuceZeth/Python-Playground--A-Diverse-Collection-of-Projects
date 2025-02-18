import sqlite3

con = sqlite3.connect("Depo.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ürünler (isim TEXT, giriş_miktar, depo_miktarı INT, kalan_miktar INT, satış_miktarı INT)")
    con.commit()

class ürünler():

    def ürün_ekle(self,ürün_ismi,giriş_miktarı,depo_miktarı,kalan_miktar,satış_miktarı):
        cursor.execute("INSERT INTO ürünler VALUES(?,?,?,?,?)",(ürün_ismi,giriş_miktarı,depo_miktarı,kalan_miktar,satış_miktarı))
        con.commit()

    def ürünleri_göster(self):
        cursor.execute("Select * From ürünler")
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Ürün Bulunmuyor...")
        else:
            for i in liste:
                print("Ürün İsmi: ", i[0])
                print("Giriş Miktarı: ", i[1])
                print("Depo Miktarı: ", i[2])
                print("Kalan Miktar: ", i[3])
                print("Satış Miktarı ",i[4])

    def ürün_göster(self,ürün_ismi):
        cursor.execute("Select * From ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchone()
        if (len(liste) == 0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
            print("Ürün ismi: ", str(liste[0]))
            print("Giriş Miktarı: ", str(liste[1]))
            print("Depo Miktarı: ", str(liste[2]))
            print("Kalan Miktar: ", str(liste[3]))
            print("Satış Miktarı: ",str(liste[4]))

    def ürünleri_güncelle_isim(self,ürün_ismi,eski_ürün_ismi,yeni_ürün_ismi):
        cursor.execute("Select * from ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
          cursor.execute("Update ürünler set isim = ? where isim = ?",(yeni_ürün_ismi,eski_ürün_ismi))
          con.commit()

    def ürünleri_güncelle_giriş_miktarı(self,ürün_ismi,eski_giriş_miktarı,yeni_giriş_miktarı):
        cursor.execute("Select * from ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
          cursor.execute("Update ürünler set giriş_miktarı = ? where giriş_miktarı = ?",(yeni_giriş_miktarı,eski_giriş_miktarı))
          con.commit()

    def ürünleri_güncelle_depo_miktarı(self,ürün_ismi,eski_depo_miktarı,yeni_depo_miktarı):
        cursor.execute("Select * from ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
          cursor.execute("Update ürünler set depo_miktarı = ? where depo_miktarı = ?",(yeni_depo_miktarı,eski_depo_miktarı))
          con.commit()

    def ürünleri_güncelle_kalan_miktar(self,ürün_ismi,eski_kalan_miktar,yeni_kalan_miktar):
        cursor.execute("Select * from ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
          cursor.execute("Update ürünler set kalan_miktar = ? where kalan_miktar = ?",(yeni_kalan_miktar,eski_kalan_miktar))
          con.commit()

    def ürünleri_güncelle_satış_miktarı(self,ürün_ismi,eski_satış_miktarı,yeni_satış_miktarı):
        cursor.execute("Select * from ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if(len(liste)==0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
          cursor.execute("Update ürünler set satış_miktarı = ? where satış_miktarı = ?",(yeni_satış_miktarı,eski_satış_miktarı))
          con.commit()

    def ürün_sil(self,ürün_ismi):
        cursor.execute("Select * From ürünler where isim = ?", (ürün_ismi,))
        liste = cursor.fetchall()
        if (len(liste) == 0):
            print("Böyle Bir Ürün Bulunmuyor...")
        else:
            cursor.execute("DELETE From ürünler where isim = ?", (ürün_ismi,))
            con.commit()

tablo_olustur()
ürünler = ürünler()

print("""
    İşlemler: 
        1.Ürünleri Göster
        2.Seçili Ürünü Göster
        3.Ürün Ekle
        4.Ürün Sil
        5.Ürün Güncelle
        6.Çıkmak İçin 'q' Giriniz
""")

while True:
    işlem = input("İşlem Giriniz: ")

    if(işlem=="1"):
        print("Ürünler: \n")
        ürünler.ürünleri_göster()

    elif(işlem=="2"):
        ürün_ismi = input("Gösterilecek Olan Ürünün İsmi: ")
        ürünler.ürün_göster(ürün_ismi)

    elif (işlem == "3"):
        print("Eklenecek Ürünün Bilgilerini Giriniz...")
        ürün_ismi = input("Ürün İsmi: ")
        giriş_miktarı = input("Giriş Miktarı: ")
        depo_miktarı = input("Depo Miktarı: ")
        kalan_miktar = input("Kalan Miktar: ")
        satış_miktarı = input("Satış Miktarı: ")
        ürünler.ürün_ekle(ürün_ismi,giriş_miktarı,depo_miktarı,kalan_miktar,satış_miktarı)

    elif (işlem == "4"):
        ürün_ismi = input("Silinecek Ürünün İsmi: ")
        ürünler.ürün_sil(ürün_ismi)

    elif (işlem == "5"):
        print("""
            Değiştirilecek Bilgiler
            1.Ürün İsmi
            2.Giriş Miktarı
            3.Depo Miktarı
            4.Kalan Miktar
            5.Satış Miktarı
            6.Çıkmak İçin 'q' Giriniz
        """)
        while True:
            işlem = input("Hangi Bilgiyi Değiştirmek İstiyorsunuz: ")
            if(işlem=="1"):
                ürün_ismi=input("Değiştirilicek Ürünün İsmini Giriniz: ")
                eski_ürün_ismi = input("Ürünün Eski İsmi: ")
                yeni_ürün_ismi = input("Ürünün Yeni İsmi: ")
                ürünler.ürünleri_güncelle_isim(ürün_ismi, eski_ürün_ismi, yeni_ürün_ismi)
            elif(işlem=="2"):
                ürün_ismi = input("Değiştirilicek Ürünün İsmini Giriniz: ")
                eski_giriş_miktarı = input("Ürünün Eski Giriş Miktarı: ")
                yeni_giriş_miktarı = input("Ürünün Yeni Giriş Miktarı: ")
                ürünler.ürünleri_güncelle_giriş_miktarı(ürün_ismi,eski_ürün_ismi,yeni_ürün_ismi)
            elif(işlem=="3"):
                ürün_ismi = input("Değiştirilicek Ürünün İsmini Giriniz: ")
                eski_depo_miktarı=input("Ürünün Eski Depo Miktarı: ")
                yeni_depo_miktarı=input("Ürünün Yeni Depo Miktarı: ")
                ürünler.ürünleri_güncelle_depo_miktarı(ürün_ismi,eski_depo_miktarı,yeni_depo_miktarı)
            elif(işlem=="4"):
                ürün_ismi = input("Değiştirilicek Ürünün İsmini Giriniz: ")
                eski_kalan_miktar = input("Ürünün Eski Kalan Miktarı: ")
                yeni_kalan_miktar = input("Ürünün Yeni Kalan Miktarı: ")
                ürünler.ürünleri_güncelle_kalan_miktar(ürün_ismi,eski_kalan_miktar,yeni_kalan_miktar)
            elif (işlem == "5"):
                ürün_ismi = input("Değiştirilicek Ürünün İsmini Giriniz: ")
                eski_satış_miktarı = input("Ürünün Eski Satış Miktarı: ")
                yeni_satış_miktarı = input("Ürünün Yeni Satış Miktarı: ")
                ürünler.ürünleri_güncelle_satış_miktarı(ürün_ismi,eski_satış_miktarı,yeni_satış_miktarı)
            elif(işlem=="q"):
                print("Çıkılıyor")
                break
            else:
                print("Geçersiz İşlem....")

    elif (işlem == "q"):
        print("Çıkılıyor....")
        break

    else:
        print("İşlem Geçersiz....")

con.close()
