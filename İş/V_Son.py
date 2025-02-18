import tkinter
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk

con = sqlite3.connect("Depo.db")
cur = con.cursor()

if cur:
    print("Bağlantı Başarılı...")


def mesaj():
    msg = messagebox.showinfo("Sonuç", "İşlem Tamamlandı.")


def tablo_olustur():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS ürünler (Id INTEGER AUTO_INCREMENT PRIMARY KEY  NOT NULL,urun_adi TEXT, "
        "giris_miktari INT,  "
        "depo_miktari INT, kalan_miktar INT, satis_miktari INT)")
    con.commit()


def listele():
    liste.delete(*liste.get_children())
    conn = sqlite3.connect("Depo.db")
    sql = "SELECT * FROM ürünler"
    cur.execute(sql)
    results = cur.fetchall()
    for rs in results:
        liste.insert("", tk.END, text=rs[0], values=(
            rs[1], rs[2], rs[3], rs[4], rs[5]))
    conn.close()


def datagetir(event):
    idno = liste.item(liste.selection()[0])['text']
    sql = "SELECT * FROM ürünler WHERE Id=%s" % idno
    cur.execute(sql)
    results = cur.fetchone()
    idtxt.delete(0, END)
    idtxt.insert(0, results[0])
    e_urun_adi.delete(0, END)
    e_urun_adi.insert(0, results[1])
    e_giris_miktari.delete(0, END)
    e_giris_miktari.insert(0, results[2])
    e_depo_miktari.delete(0, END)
    e_depo_miktari.insert(0, results[3])
    e_kalan_miktar.delete(0, END)
    e_kalan_miktar.insert(0, results[4])
    e_satis_miktari.delete(0, END)
    e_satis_miktari.insert(0, results[5])


def ekle():
    try:
        cur.execute("INSERT INTO ürünler VALUES (?,?,?,?,?,?)", (
            idtxt.get(), e_urun_adi.get(), e_giris_miktari.get(), e_depo_miktari.get(), e_kalan_miktar.get(),
            e_satis_miktari.get()))
        con.commit()
        listele()
        mesaj()
    except sqlite3.IntegrityError:
        msg = messagebox.showinfo("Sonuç", "ID Değeri Tekrarsız Olmalı...")


def sil():
    sql = "DELETE FROM ürünler WHERE Id=%s" % (idtxt.get())
    cur.execute(sql)
    con.commit()
    listele()
    mesaj()


def guncelle():
    sql = "UPDATE ürünler SET urun_adi='%s' ,giris_miktari='%s' ,depo_miktari='%s' ,kalan_miktar='%s', " \
          "satis_miktari='%s' WHERE Id=%s " % (e_urun_adi.get(), e_giris_miktari.get(), e_depo_miktari.get(),
                                               e_kalan_miktar.get(), e_satis_miktari.get(), idtxt.get())
    cur.execute(sql)
    con.commit()
    listele()
    mesaj()


def temizle():
    idtxt.delete(0, END)
    e_urun_adi.delete(0, END)
    e_giris_miktari.delete(0, END)
    e_kalan_miktar.delete(0, END)
    e_depo_miktari.delete(0, END)
    e_satis_miktari.delete(0, END)


top = tkinter.Tk()
top.title("Stok Programı")
top.geometry('1210x400')

l_id = Label(top, text="ID: ").place(x=10, y=250)
idtxt = Entry(top, bd=1)
idtxt.place(x=100, y=250)
l_msg = Label(top, text="İşlem Yaparken Bu Kısmı Tekrarsız Kullanınız...").place(x=240, y=250)

l_urun_adi = Label(top, text="Ürün İsmi: ").place(x=10, y=275)
e_urun_adi = Entry(top, bd=1)
e_urun_adi.place(x=100, y=275)

l_giris_miktari = Label(top, text="Giriş Miktarı: ").place(x=10, y=300)
e_giris_miktari = Entry(top, bd=1)
e_giris_miktari.place(x=100, y=300)

l_depo_miktari = Label(top, text="Depo Miktarı: ").place(x=10, y=325)
e_depo_miktari = Entry(top, bd=1)
e_depo_miktari.place(x=100, y=325)

l_kalan_miktar = Label(top, text="Kalan Miktar: ").place(x=10, y=350)
e_kalan_miktar = Entry(top, bd=1)
e_kalan_miktar.place(x=100, y=350)

l_satis_miktari = Label(top, text="Satış Miktarı: ").place(x=10, y=375)
e_satis_miktari = Entry(top, bd=1)
e_satis_miktari.place(x=100, y=375)

b_ekle = Button(top, text="Ekle", command=ekle)
b_ekle.place(x=500, y=250, width=100, height=50)

b_sil = Button(top, text="Sil", command=sil)
b_sil.place(x=500, y=320, width=100, height=50)

b_guncelle = Button(top, text="Güncelle", command=guncelle)
b_guncelle.place(x=630, y=250, width=100, height=50)

b_temizle = Button(top, text="Temizle", command=temizle)
b_temizle.place(x=630, y=320, width=100, height=50)

liste = ttk.Treeview(top, column=("column1", "column2", "column3", "column4", "column5"))
liste.place(x=0, y=0)
liste.heading("#0", text="Id")
liste.heading("column1", text="Ürün Adı")
liste.heading("column2", text="Giriş Miktarı")
liste.heading("column3", text="Depo Miktarı")
liste.heading("column4", text="Kalan Miktar")
liste.heading("column5", text="Satış Miktarı")
liste.pack()
liste.bind('<ButtonRelease-1>', datagetir)

tablo_olustur()
listele()
top.mainloop()
