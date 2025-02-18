import sqlite3

con = sqlite3.connect("Airlines.db")
cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Ucak (ucak_kodu INT PRIMARY KEY, ucak_adi TEXT, ucak_turu TEXT, "
                   "uretim_yili TEXT, yolcu_kapasitesi INT, ucus_kodu INT, FOREIGN KEY(ucus_kodu) references Ucus("
                   "ucus_kodu))")
    con.commit()


def tablo_olustur2():
    cursor.execute("CREATE TABLE IF NOT EXISTS Yolcu (yolcu_tc INT, yolcu_adi_soyadi TEXT, yolcu_yasi INT, "
                   "yolcu_mil INT, ucus_kodu INT, FOREIGN KEY(ucus_kodu) references Ucus(ucus_kodu))")
    con.commit()


def tablo_olustur3():
    cursor.execute("CREATE TABLE IF NOT EXISTS Ucus (ucus_kodu INT,ucus_adi TEXT,ucus_tarihi TEXT,kalkis_yeri TEXT, "
                   "inis_yeri TEXT)")
    con.commit()


class Ucak:
    @staticmethod
    def veri_ekleme(ucak_kodu, ucak_adi, ucak_turu, uretim_yili, yolcu_kapasitesi, ucus_kodu):
        cursor.execute("INSERT INTO Ucak VALUES(?,?,?,?,?,?)", (ucak_kodu, ucak_adi, ucak_turu, uretim_yili,
                                                                yolcu_kapasitesi, ucus_kodu,))
        con.commit()

    @staticmethod
    def verileri_al():
        cursor.execute("Select * From Ucak")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Uçaklar Mevcut Değil...")
        else:
            for i in liste:
                print("Uçak Kodu: ", i[0])
                print("Uçak Adı: ", i[1])
                print("Uçak Türü: ", i[2])
                print("Üretim Yılı: ", i[3])
                print("Yolcu Kapasitesi: ", i[4])
                print("Ucuş Kodu: ", i[5])

    @staticmethod
    def verileri_al2(ucakodu):
        cursor.execute("Select * From Ucak where ucak_kodu = ?", (ucakodu,))
        liste = cursor.fetchone()
        if len(liste) == 0:
            print("Uçak Mevcut Değil...")
        else:
            print("Uçak Kodu: ", str(liste[0]))
            print("Uçak Adı: ", str(liste[1]))
            print("Uçak Türü: ", str(liste[2]))
            print("Üretim Yılı: ", str(liste[3]))
            print("Yolcu Kapasitesi: ", str(liste[4]))
            print("Ucuş Kodu: ", str(liste[5]))

    @staticmethod
    def verileri_guncelle(ucakodu, ucakadi, ucakturu, uretimyili, yolcukapasitesi, ucuskodu):
        cursor.execute("Update Ucak set ucak_adi = ? where ucak_kodu = ?", (ucakadi, ucakodu))
        cursor.execute("Update Ucak set ucak_turu = ? where ucak_kodu = ?", (ucakturu, ucakodu))
        cursor.execute("Update Ucak set uretim_yili = ? where ucak_kodu = ?", (uretimyili, ucakodu))
        cursor.execute("Update Ucak set yolcu_kapasitesi = ? where ucak_kodu = ?", (yolcukapasitesi, ucakodu))
        cursor.execute("Update Ucak set ucus_kodu = ? where ucak_kodu = ?", (ucuskodu, ucakodu))
        con.commit()

    @staticmethod
    def verileri_sil(ucak_kodu):
        cursor.execute("Select * From Ucak where ucak_kodu = ?", (ucak_kodu,))
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Uçak Mevcut Değil...")
        else:
            cursor.execute("DELETE From Ucak where ucak_kodu = ?", (ucak_kodu,))
            con.commit()


class Yolcu:
    @staticmethod
    def veri_ekleme(yolcu_adi_soyadi, yolcu_tc, yolcu_yasi, yolcu_mil, ucuskodu):
        cursor.execute("INSERT INTO Yolcu VALUES(?,?,?,?,?)", (yolcu_tc, yolcu_adi_soyadi, yolcu_yasi, yolcu_mil,
                                                               ucuskodu,))
        con.commit()

    @staticmethod
    def verileri_al():
        cursor.execute("Select * From Yolcu")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Yolcular Mevcut Değil...")
        else:
            for i in liste:
                print("TC: ", i[0])
                print("Adı Soyadı: ", i[1])
                print("Yaş: ", i[2])
                print("Mil: ", i[3])
                print("Uçuş Kodu: ", i[4])

    @staticmethod
    def verileri_al2(yolcutc):
        cursor.execute("Select * From Yolcu where yolcu_tc = ?", (yolcutc,))
        liste = cursor.fetchone()
        if len(liste) == 0:
            print("Yolcu Mevcut Değil...")
        else:
            print("TC: ", str(liste[0]))
            print("Adı Soyadı: ", str(liste[1]))
            print("Yaş: ", str(liste[2]))
            print("Mil: ", str(liste[3]))
            print("Uçuş Kodu: ", str(liste[4]))

    @staticmethod
    def verileri_guncelle(yolcuadisoyadi, yolcutc, yolcuyasi, yolcumil, ucuskodu):
        cursor.execute("Update Yolcu set yolcu_adi_soyadi = ? where yolcu_tc = ?", (yolcuadisoyadi, yolcutc))
        cursor.execute("Update Yolcu set yolcu_yasi = ? where yolcu_tc = ?", (yolcuyasi, yolcutc))
        cursor.execute("Update Yolcu set yolcu_mil = ? where yolcu_tc = ?", (yolcumil, yolcutc))
        cursor.execute("Update Yolcu set ucus_kodu = ? where yolcu_tc = ?", (ucuskodu, yolcutc))
        con.commit()

    @staticmethod
    def verileri_sil(yolcutc):
        cursor.execute("Select * From Yolcu where yolcu_tc = ?", (yolcutc,))
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Yolcu Mevcut Değil...")
        else:
            cursor.execute("DELETE From Yolcu where yolcu_tc = ?", (yolcutc,))
            con.commit()


class Ucus:
    @staticmethod
    def veri_ekleme(ucus_adi, ucus_kodu, ucus_tarihi, kalkis_yeri, inis_yeri):
        cursor.execute("INSERT INTO Ucus VALUES(?,?,?,?)", (ucus_kodu, ucus_adi, ucus_tarihi, kalkis_yeri, inis_yeri))
        con.commit()

    @staticmethod
    def verileri_al():
        cursor.execute("Select * From Ucus")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Uçuşlar Mevcut Değil...")
        else:
            for i in liste:
                print("Uçuş Kodu: ", i[0])
                print("Uçuş Adı: ", i[1])
                print("Uçuş Tarihi: ", i[2])
                print("Kalkış Yeri: ", i[3])
                print("İniş Yeri: ", i[4])

    @staticmethod
    def verileri_al2(ucus_kodu):
        cursor.execute("Select * From Ucus where ucus_kodu = ?", (ucus_kodu,))
        liste = cursor.fetchone()
        if len(liste) == 0:
            print("Uçuş Mevcut Değil...")
        else:
            print("Uçuş Kodu: ", str(liste[0]))
            print("Uçuş Adı: ", str(liste[1]))
            print("Uçuş Tarihi: ", str(liste[2]))
            print("Kalkış Yeri: ", str(liste[3]))
            print("İniş Yeri: ", str(liste[4]))

    @staticmethod
    def verileri_guncelle(ucus_kodu, ucus_adi, ucus_tarihi, kalkis_yeri, inis_yeri):
        cursor.execute("Update Ucus set ucus_adi = ? where ucus_kodu = ?", (ucus_adi, ucus_kodu))
        cursor.execute("Update Ucus set ucus_tarihi = ? where ucus_kodu = ?", (ucus_tarihi, ucus_kodu))
        cursor.execute("Update Ucus set kalkis_yeri = ? where ucus_kodu = ?", (kalkis_yeri, ucus_kodu))
        cursor.execute("Update Ucus set inis_yeri = ? where ucus_kodu = ?", (inis_yeri, ucus_kodu))
        con.commit()

    @staticmethod
    def verileri_sil(ucus_kodu):
        cursor.execute("Select * From Ucus where yolcu_tc = ?", (ucus_kodu,))
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Uçuş Mevcut Değil...")
        else:
            cursor.execute("DELETE From Ucus where yolcu_tc = ?", (ucus_kodu,))
            con.commit()


tablo_olustur()
tablo_olustur2()
tablo_olustur3()

cursor.execute("INSERT INTO Ucus Values('31','TK223','21-10-2021','İstanbul','Amsterdam')")
con.commit()

cursor.execute("INSERT INTO Ucak Values('25','Alpha 1','Yolcu','2015','350','31')")
con.commit()

for a in range(1, 3):
    yolcuadsoyad = input("Ad-Soyad : ")
    yolcu_Tc = input("TC : ")
    yolcuyas = input("Yaş : ")
    yolcumili = input("Mil : ")
    ucus_Kodu = input("Uçuş Kodu : ")
    Yolcu.veri_ekleme(yolcu_Tc, yolcuadsoyad, yolcuyas, yolcumili, ucus_Kodu)

Yolcu.verileri_al()
