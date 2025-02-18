"""
1)
"""
import sqlite3

con = sqlite3.connect("banka_musteriler.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Musteri (TC INT PRIMARY KEY, Ad_Soyad TEXT, Dogum_Tarihi INT,"
               "Dogum_Yeri TEXT, Cinsiyet TEXT)")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS Musteri_Hesap_Hareket (Id INT PRIMARY KEY, Islem_Turu TEXT, Tutar INT,"
               "Musteri_TC INT, Islem_Tarihi INT, FOREIGN KEY(Musteri_TC) REFERENCES Musteri(TC))")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS Musteri_Hesap (Id INT PRIMARY KEY, Hesap_Adi TEXT, Hesap_Acilis_Tarihi INT,"
               "Hesap_Turu TEXT, Bakiye Int)")
con.commit()
"""
1-Bitiş
"""
"""
2)
cursor.execute("INSERT INTO Musteri VALUES('12345678991','Ramazan Aydoğan','23.03.1983','Bağlum','Erkek')")
con.commit()

cursor.execute("INSERT INTO Musteri VALUES('98765432111','Ahmet Demir','23.01.1981','Ankara','Erkek')")
con.commit()

cursor.execute("INSERT INTO Musteri VALUES('93765432133','Ayşe Bayburtlu','23.07.1965','Kayseri','Kız')")
con.commit()

cursor.execute("INSERT INTO Musteri_Hesap_Hareket VALUES('2323','Kira','1.023 TL','12345678991','06.05.2019')")
con.commit()

cursor.execute("INSERT INTO Musteri_Hesap_Hareket VALUES('2324','Havale','2.300 TL','93765432133','13.05.2019')")
con.commit()
-----------------------------------------------------------------------------------------------------------------------
cursor.execute("Select TC,Ad_Soyad,Dogum_Yeri, Islem_Turu, Islem_Tarihi From Musteri INNER JOIN Musteri_Hesap_Hareket "
               "ON Musteri.TC = Musteri_Hesap_Hareket.Musteri_TC")
liste = cursor.fetchall()
for i in liste:
    if i[0] == 12345678991:
        print(i)
2-Bitiş
"""


class Musteri:
    def __init__(self, TC, Ad_Soyad, Dogum_Tarihi, Dogum_Yeri, Cinsiyet):
        self.TC = TC
        self.Ad_Soyad = Ad_Soyad
        self.Dogum_Tarihi = Dogum_Tarihi
        self.Dogum_Yeri = Dogum_Yeri
        self.Cinsiyet = Cinsiyet

    @staticmethod
    def Yas_Goster(Guncel_Yil, Tc):
        cursor.execute("Select * From Musteri")
        liste = cursor.fetchall()
        for i in liste:
            if i[0] == Tc:
                a = i[2]
                print("Yaş :", Guncel_Yil - int(a[6] + a[7] + a[8] + a[9]))

    @staticmethod
    def Bilgi_Goster(Tc):
        cursor.execute("Select * From Musteri")
        liste = cursor.fetchall()
        for i in liste:
            if i[0] == Tc:
                print(i)


Musteri.Yas_Goster(2021, 12345678991)
Musteri.Bilgi_Goster(12345678991)
