import sqlite3

con = sqlite3.connect("Bilgisayarcı.db")
cursor = con.cursor()


def TabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Malzemeler (Id INTEGER AUTO_INCREMENT PRIMARY KEY  NOT NULL, Misim TEXT,"
                   "Adet INT)")
    con.commit()


class veto:
    @staticmethod
    def MalzemeEkleme(Id, Misim, Adet):
        try:
            cursor.execute("INSERT INTO Malzemeler VALUES(?,?,?)", (Id, Misim, Adet))
            con.commit()
        except sqlite3.IntegrityError:
            print("Id Tekrarsız Olmalı...")

    @staticmethod
    def MalzemeSilme(Misim):
        cursor.execute("Select * From Malzemeler where Misim = ?", (Misim,))
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Malzeme Yok...")
        else:
            cursor.execute("DELETE From Malzemeler where Misim = ?", (Misim,))
            con.commit()

    @staticmethod
    def MalzemeGuncelle(Misim, Yadet):
        cursor.execute("Update Malzemeler set Adet = ? where Misim = ?", (Yadet, Misim))
        con.commit()

    @staticmethod
    def VerileriAl():
        cursor.execute("Select * From Malzemeler")
        liste = cursor.fetchall()
        if len(liste) == 0:
            print("Malzeme Bulunmuyor...")
        else:
            for i in liste:
                print("Id: ", i[0])
                print("Malzeme İsmi: ", i[1])
                print("Adedi: ", i[2])

    @staticmethod
    def VerileriAl2(Misim):
        cursor.execute("Select * From Malzemeler where Misim = ?", (Misim,))
        liste = cursor.fetchone()
        if len(liste) == 0:
            print("Malzeme Bulunmuyor...")
        else:
            print("Id: ", str(liste[0]))
            print("Malzeme İsmi: ", str(liste[1]))
            print("Adedi: ", str(liste[2]))


TabloOlustur()
veto = veto()

print("\n1.Malzemeleri Göster\n2.Seçili Malzemeyi Göster\n3.Malzeme Ekle\n4.Malzeme Sil\n5.Malzeme Güncelle\n6.Çıkmak"
      "İçin '0' Giriniz\n")

while True:
    islem = int(input("İşlem Giriniz: "))

    if islem == 1:
        veto.VerileriAl()

    elif islem == 2:
        misim = input("Gösterilecek Malzemenin İsmini Giriniz: ")
        veto.VerileriAl2(misim)

    elif islem == 3:
        d = input("Id: ")
        misim = input("Malzeme ismi: ")
        adet = input("Adet: ")
        veto.MalzemeEkleme(d, misim, adet)

    elif islem == 4:
        misim = input("Silinecek Malzemenin İsmini Giriniz: ")
        veto.MalzemeSilme(misim)

    elif islem == 5:
        misim = input("Değiştirilecek Malzemeyi Giriniz: ")
        yadet = input("Yeni Adedi Giriniz: ")
        veto.MalzemeGuncelle(misim, yadet)

    elif islem == 0:
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz İşlem...")

con.close()
