import sqlite3

con = sqlite3.connect("KafiBaklava.db")
cursor = con.cursor()


def Tablo_Baklava():
    cursor.execute("CREATE TABLE IF NOT EXISTS Baklava (Baklava_ID INT PRIMARY KEY, Baklava_Ad TEXT, Baklava_Kilo INT,"
                   "Baklava_Bilgi TEXT,Baklava_Fiyat INT)")
    con.commit()


def Tablo_Sepet():
    cursor.execute("CREATE TABLE IF NOT EXISTS Sepet (Ad TEXT, Kilo INT)")
    con.commit()


def Tablo_Musteri():
    cursor.execute("CREATE TABLE IF NOT EXISTS Musteri (Musteri_ID INT PRIMARY KEY, Musteri_Email "
                   "TEXT, Musteri_Sifre "
                   "TEXT, Musteri_Adres TEXT)")
    con.commit()


def Tablo_Siparis():
    cursor.execute("CREATE TABLE IF NOT EXISTS Siparis (Siparis_ID INT PRIMARY KEY, Musteri_ID INT, "
                   "Baklava_ID INT, "
                   "Tarih TEXT, Baklava_Alis_Kilo INT, FOREIGN KEY(Musteri_ID) REFERENCES Musteri(Musteri_ID), "
                   "FOREIGN KEY(Baklava_ID) REFERENCES Baklava(Baklava_ID))")
    con.commit()


def Tablo_Admin():
    cursor.execute("CREATE TABLE IF NOT EXISTS Admin (Admin_ID INT PRIMARY KEY, Kullanici_Adi TEXT, "
                   "Sifre TEXT)")
    con.commit()


def S_Veri_Ekle(Ad, Kilo):
    cursor.execute("INSERT INTO Sepet VALUES(?,?)", (Ad, Kilo))
    con.commit()


def B_Veri_Ekle(Baklava_ID, Baklava_Ad, Baklava_Kilo, Baklava_Bilgi, Baklava_Fiyat):
    try:
        cursor.execute("INSERT INTO Baklava VALUES(?,?,?,?,?)", (Baklava_ID, Baklava_Ad, Baklava_Kilo, Baklava_Bilgi,
                                                                 Baklava_Fiyat,))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def B_Veri_Sil(Baklava_ID):
    cursor.execute("Select * From Baklava where Baklava_ID = ?", (Baklava_ID,))
    liste = cursor.fetchall()
    if len(liste) == 0:
        return False
    else:
        cursor.execute("DELETE From Baklava where Baklava_ID = ?", (Baklava_ID,))
        con.commit()
        return True


def B_Veri_Guncelle(secim, Baklava_ID, Y_Veri):
    if secim == 'ad':
        cursor.execute("Update Baklava set Baklava_Ad = ? where Baklava_ID = ?", (Y_Veri, Baklava_ID))
        con.commit()
        return True
    elif secim == 'kilo':
        cursor.execute("Update Baklava set Baklava_Kilo = ? where Baklava_ID = ?", (Y_Veri, Baklava_ID))
        con.commit()
        return True
    elif secim == 'bilgi':
        cursor.execute("Update Baklava set Baklava_Bilgi = ? where Baklava_ID = ?", (Y_Veri, Baklava_ID))
        con.commit()
        return True
    elif secim == 'fiyat':
        cursor.execute("Update Baklava set Baklava_Fiyat = ? where Baklava_ID = ?", (Y_Veri, Baklava_ID))
        con.commit()
        return True
    else:
        return False


def M_Veri_Ekle(Musteri_ID, Musteri_Email, Musteri_Sifre, Musteri_Adres):
    try:
        cursor.execute("INSERT INTO Musteri VALUES(?,?,?,?)",
                       (Musteri_ID, Musteri_Email, Musteri_Sifre, Musteri_Adres,))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def A_Ekle():
    cursor.execute("INSERT INTO Admin Values('2','efe','123')")
    con.commit()


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


def M_Kontrol(id, Sifre):
    cursor.execute("Select * From Musteri")
    liste = cursor.fetchall()
    H = 0
    for i in liste:
        if id == i[0] and Sifre == i[2]:
            return True
        else:
            H = H + 1

    if H == len(liste):
        return False


def B_Goster():
    cursor.execute("Select * From Baklava")
    liste = cursor.fetchall()
    for i in liste:
        print("ID: ", i[0])
        print("Ad: ", i[1])
        print("Kilo: ", i[2])
        print("Bilgi: ", i[3])
        print("Fiyat: ", i[4])


def B_Goster_M():
    cursor.execute("Select * From Baklava")
    liste = cursor.fetchall()
    for i in liste:
        print("Ad: ", i[1])
        print("Bilgi: ", i[3])
        print("Fiyat: ", i[4])


def M_Siparis(s_ad, s_kilo):
    cursor.execute("Select * From Baklava")
    liste = cursor.fetchall()
    while 1:
        for i in liste:
            if i[1] == s_ad:
                if i[2] >= s_kilo:
                    return 1
                else:
                    return 2
        return 3


def SSepet():
    Tutar = 0
    cursor.execute("Select * From Baklava")
    liste = cursor.fetchall()
    cursor.execute("Select * From Sepet")
    liste2 = cursor.fetchall()
    for i in liste2:
        print("Ad : ", i[0])
        print("Kilo : ", i[1])
        for j in liste:
            if i[0] == j[1]:
                Tutar = Tutar + i[1] * j[4]
                yeni = j[2]-i[1]
                cursor.execute("Update Baklava set Baklava_Kilo = ? where Baklava_ID = ?", (yeni, j[0]))
                con.commit()
    print("Toplam Tutar : ", Tutar)


def Teslimat(m_id):
    cursor.execute("Select * From Musteri")
    liste = cursor.fetchall()
    for i in liste:
        if i[0] == m_id:
            return i[3]


def S_Sifirla():
    cursor.execute("Select * From Sepet")
    liste = cursor.fetchall()
    for i in liste:
        cursor.execute("DELETE From Sepet where Ad = ?", (i[0],))
        con.commit()