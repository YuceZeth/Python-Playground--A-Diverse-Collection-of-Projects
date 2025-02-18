import sqlite3

con = sqlite3.connect("Yemekler.db")
cursor = con.cursor()

"""
cursor.execute("CREATE TABLE IF NOT EXISTS Yemek (ID INT, Yemek_Ad TEXT, Yemek_Kalori INT, Yemek_Icerigi TEXT)")
con.commit()

cursor.execute("INSERT INTO Yemek Values('23','Adana Kebab','3000','Kıyma,Bulgur,Soğan')")
con.commit()

ID = "33"
Yad = "Hamburger"
Ykalori = 2000
Yicerik = "Peynir,Köfte,Soğan"
cursor.execute("INSERT INTO Yemek Values(?,?,?,?)", (ID, Yad, Ykalori, Yicerik))
con.commit()

cursor.execute("INSERT INTO Yemek Values('43','Yaprak Sarması','1000','ZeytinYağı,Düğ,Soğan')")
con.commit()
"""
cursor.execute("UPDATE Yemek set Yemek_Kalori = ? Where ID = ?", (2500, 23))
con.commit()

cursor.execute("Delete From Yemek Where ID = ?", (43,))
con.commit()

cursor.execute("Select * From Yemek")
data = cursor.fetchall()
for i in data:
    print(i)

con.close()
