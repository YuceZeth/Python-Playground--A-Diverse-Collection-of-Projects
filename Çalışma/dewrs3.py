import sqlite3

con = sqlite3.connect("Kulup.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Uye_Bilgileri (uye_no INT PRIMARY KEY, ismi TEXT, cinsiyeti TEXT, "
               "sinifi TEXT)")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS Aidat_Bilgileri (id INT PRIMARY KEY,uye_no INT, tutar INT NOT NULL, "
               "Tarih TEXT, FOREIGN KEY(uye_no) references Uye_Bilgileri(uye_no)) ")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS Kulup_Yonetimi (id INT PRIMARY KEY,ismi TEXT, gorevi TEXT, telefonu INT)")
con.commit()

cursor.execute("INSERT INTO Uye_Bilgileri Values('1','ali','5552224422','erkek')")
con.commit()

cursor.execute("INSERT INTO Uye_Bilgileri Values('2','ayse','555222333111','erkek')")
con.commit()

cursor.execute("INSERT INTO Aidat_Bilgileri Values('1','1','100','17.05.2021')")
con.commit()

cursor.execute("INSERT INTO Aidat_Bilgileri Values('2','1','100','17.05.2020')")
con.commit()

cursor.execute("INSERT INTO Kulup_Yonetimi Values('1','ömer','baskan','2323')")
con.commit()

cursor.execute("INSERT INTO Kulup_Yonetimi Values('2','merve','baskan yrd','3232')")
con.commit()

cursor.execute("INSERT INTO Kulup_Yonetimi Values('3','kerem','Yk üyesi','1111')")
con.commit()

cursor.execute("UPDATE Kulup_Yonetimi set telefonu = ? Where ID = ?", (2121, 1))
con.commit()

cursor.execute("UPDATE Uye_Bilgileri set ismi = ? Where uye_no = ?", ("ayse nur", 2))
con.commit()

cursor.execute("Select * From Uye_Bilgileri")
uye_sayisi = cursor.fetchall()
print("Üye Sayısı : ", len(uye_sayisi))

cursor.execute("Select * From Aidat_Bilgileri")
data = cursor.fetchall()
toplam_aidat = 0
for i in data:
    toplam_aidat = toplam_aidat + i[2]

print("Toplam Aidat : ", toplam_aidat)

con.close()

"""
import sqlite3

con = sqlite3.connect("a.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT PRIMARY KEY, name TEXT, priority TEXT,status_id INT, "
               "project_id INT, begin_date TEXT, end_date TEXT, FOREIGN KEY(project_id) references project(id))")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS project (id INT PRIMARY KEY, name TEXT, begin_date TEXT, end_date TEXT) ")
con.commit()
"""
