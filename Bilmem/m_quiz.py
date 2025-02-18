import sqlite3

con = sqlite3.connect("AYemek.db")
cursor = con.cursor()


def Tablo_Menu():
    cursor.execute("CREATE TABLE IF NOT EXISTS Menu (Yemek_ID INT PRIMARY KEY, Yemek_Ad TEXT, Yemek_Fiyat INT,"
                   "Yemek_Bilgi TEXT)")
    con.commit()


def Tablo_Kullanici():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kullanici (Telefon_No INT PRIMARY KEY, Sifre TEXT, Adres TEXT)")
    con.commit()


def Tablo_Sepet():
    cursor.execute("CREATE TABLE IF NOT EXISTS Sepet (Yemek_Ad TEXT, Adet INT)")
    con.commit()


def Tablo_Teslimat():
    cursor.execute("CREATE TABLE IF NOT EXISTS Teslimat (Telefon_No INT, Adres TEXT, Tutar INT, Odeme_Tipi TEXT,"
                   "FOREIGN KEY(Telefon_No) REFERENCES Kullanici(Telefon_No) )")
    con.commit()


def Tablo_Admin():
    cursor.execute("CREATE TABLE IF NOT EXISTS Admin (Admin_ID INT PRIMARY KEY, Kullanici_Adi TEXT, "
                   "Sifre TEXT)")
    con.commit()


def Admin_Ekle():
    cursor.execute("INSERT INTO Admin VALUES('1', 'kaan', '123')")
    con.commit()


def M_Veri_Ekle(Yemek_ID, Yemek_Ad, Yemek_Fiyat, Yemek_Bilgi):
    try:
        cursor.execute("INSERT INTO Menu VALUES(?,?,?,?)", (Yemek_ID, Yemek_Ad, Yemek_Fiyat, Yemek_Bilgi,))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def A_Kontrol(Kullanici_Adi, Sifre):
    cursor.execute("Select * From Admin")
    liste = cursor.fetchall()
    H = 0
    for i in liste:
        if Kullanici_Adi == i[1] and Sifre == i[2]:
            return True
        else:
            H = H + 1
    if H == len(liste):
        return False


def A_Goster():
    cursor.execute("Select * From Menu")
    liste = cursor.fetchall()
    for i in liste:
        print("Ad: ", i[1])
        print("Fiyat: ", i[2])
        print("Bilgi: ", i[3])


def A_Veri_Sil(Yemek_ID):
    cursor.execute("Select * From Menu where Yemek_ID = ?", (Yemek_ID,))
    liste = cursor.fetchall()
    if len(liste) == 0:
        return False
    else:
        cursor.execute("DELETE From Menu where Yemek_ID = ?", (Yemek_ID,))
        con.commit()
        return True


def A_Veri_Guncelle(secim, Yemek_ID, Y_Veri):
    if secim == 'ad':
        cursor.execute("Update Menu set Yemek_Ad = ? where Yemek_ID = ?", (Y_Veri, Yemek_ID))
        con.commit()
        return True
    elif secim == 'bilgi':
        cursor.execute("Update Menu set Yemek_Bilgi = ? where Yemek_ID = ?", (Y_Veri, Yemek_ID))
        con.commit()
        return True
    elif secim == 'fiyat':
        cursor.execute("Update Menu set Yemek_Fiyat = ? where Yemek_ID = ?", (Y_Veri, Yemek_ID))
        con.commit()
        return True
    else:
        return False


def K_Veri_Ekle(Telefon_No, Sifre, Adres):
    try:
        cursor.execute("INSERT INTO Kullanici VALUES(?,?,?)", (Telefon_No, Sifre, Adres,))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def K_Kontrol(Telefon_No, Sifre):
    cursor.execute("Select * From Kullanici")
    liste = cursor.fetchall()
    H = 0
    for i in liste:
        if Telefon_No == i[0] and Sifre == i[1]:
            return True
        else:
            H = H + 1
    if H == len(liste):
        return False


def M_Kontrol_Sepet(yemek_ad):
    cursor.execute("Select * From Menu")
    liste = cursor.fetchall()
    H = 0
    for i in liste:
        if i[1] == yemek_ad:
            return True
        else:
            H = H + 1
    if H == len(liste):
        return False


def SSepet(yemek_ad, yemek_adet):
    cursor.execute("INSERT INTO Sepet VALUES(?,?)", (yemek_ad, yemek_adet,))
    con.commit()


def S_Goster():
    cursor.execute("Select * From Sepet")
    liste = cursor.fetchall()
    for i in liste:
        print("Ad : ", i[0])
        print("Adet : ", i[1])


def T_Veri_Ekle(Telefon_No, Odeme_Tipi):
    cursor.execute("Select * From Kullanici")
    liste = cursor.fetchall()
    cursor.execute("Select * From Sepet")
    liste2 = cursor.fetchall()
    cursor.execute("Select * From Menu")
    liste3 = cursor.fetchall()
    Tutar = 0
    for i in liste:
        if i[0] == Telefon_No:
            for j in liste2:
                for k in liste3:
                    if j[0] == k[1]:
                        Tutar = Tutar + j[1] * k[2]
    for m in liste:
        if m[0] == Telefon_No:
            Adres = m[2]
            cursor.execute("INSERT INTO Teslimat VALUES(?,?,?,?)", (Telefon_No, Adres, Tutar, Odeme_Tipi,))
            con.commit()
            return True


def TT_Goster(Telefon_no):
    cursor.execute("Select * From Teslimat")
    liste = cursor.fetchall()
    a = 0
    for i in liste:
        if a == len(liste) - 1:
            if i[0] == Telefon_no:
                print("Adres : ", i[1])
                print("Tutar : ", i[2])
                print("Ödeme Tipi : ", i[3])
        else:
            a = a + 1


def S_Sifirla():
    cursor.execute("Select * From Sepet")
    liste = cursor.fetchall()
    for i in liste:
        cursor.execute("DELETE From Sepet where Yemek_Ad = ?", (i[0],))
        con.commit()


def TTeslimat(Telefon_no):
    cursor.execute("Select * From Teslimat")
    liste = cursor.fetchall()
    for i in liste:
        if i[0] == Telefon_no:
            print("Adres : ", i[1])
            print("Tutar : ", i[2])
            print("Ödeme Tipi : ", i[3])


def K_Goster():
    cursor.execute("Select * From Kullanici")
    liste = cursor.fetchall()
    for i in liste:
        print("Telefon No : ", i[0])
