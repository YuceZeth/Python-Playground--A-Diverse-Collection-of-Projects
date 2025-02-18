import tkinter
import pymysql
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
import mysql.connector

conn = pymysql.connect(host='localhost', user='root',passwd=None, db='ürünler')
cur = conn.cursor(pymysql.cursors.DictCursor)

if cur:
    print("Bağlantı Başarılı...")

def mesaj():
    msg = messagebox.showinfo("Sonuç","İşlem Tamamlandı.")

def ekle():
    sql = "INSERT INTO ürünler (urun_adi,giris_miktari,depo_miktari,kalan_miktar,satis_miktari) VALUES ('%s','%s','%s','%s','%s') " %(e_urun_adi.get(),e_giris_miktari.get(),e_depo_miktari.get(),e_kalan_miktar.get(),e_satis_miktari.get())
    cur.execute(sql)
    conn.commit()
    listele()
    mesaj()

def listele():
    liste.delete(*liste.get_children())
    sql="SELECT * FROM ürünler"
    cur.execute(sql)
    results = cur.fetchall(sql)
    for rs in results:
        liste.insert("", 0, text=rs['Id'], values=(rs['urun_adi'], rs['giris_miktari'], rs['depo_miktari'], rs['kalan_miktar'], rs['satis_miktari']))

def datagetir(event):
    idno = liste.item(liste.selection()[0])['text']
    sql="SELECT * FROM ürünler WHERE Id=%s" % (idno)
    cur.execute(sql)
    results = cur.fetchone()
    idtxt.delete(0,END)
    idtxt.insert(0,results['Id'])
    e_urun_adi.delete(0,END)
    e_urun_adi.insert(0,results['urun_adi'])
    e_giris_miktari.delete(0, END)
    e_giris_miktari.insert(0, results['giris_miktari'])
    e_depo_miktari.delete(0, END)
    e_depo_miktari.insert(0, results['depo_miktari'])
    e_kalan_miktar.delete(0, END)
    e_kalan_miktar.insert(0, results['kalan_miktar'])
    e_satis_miktari.delete(0, END)
    e_satis_miktari.insert(0, results['satis_miktari'])

def guncelle():
    sql = "UPDATE ürünler SET urun_adi='%s' ,giris_miktari='%s' ,depo_miktari='%s' ,kalan_miktar='%s', satis_miktari='%s' WHERE Id=%s " % (e_urun_adi.get(), e_giris_miktari.get(), e_depo_miktari.get(), e_kalan_miktar.get(), e_satis_miktari.get(),idtxt.get())
    cur.execute(sql)
    conn.commit()
    listele()
    mesaj()

def sil():
    sql = "DELETE FROM ürünler WHERE Id=%s" %(idtxt.get())
    cur.execute(sql)
    conn.commit()
    listele()
    mesaj()

def temizle():
    idtxt.delete(0,END)
    e_urun_adi.delete(0,END)
    e_giris_miktari.delete(0,END)
    e_kalan_miktar.delete(0,END)
    e_depo_miktari.delete(0,END)
    e_satis_miktari.delete(0,END)

top = tkinter.Tk()
top.title("Stok Programı")
top.geometry('1204x400')

l_id = Label(top,text="ID: ").place(x=10,y=250)
idtxt = Entry(top, bd=1)
idtxt.place(x=100,y=250)
l_msg=Label(top,text="İşlem Yaparken Bu Kısmı Boş Bırakınız... ").place(x=250,y=250)

l_urun_adi = Label(top, text="Ürün İsmi: ").place(x=10, y=270)
e_urun_adi = Entry(top, bd=1)
e_urun_adi.place(x=100,y=270)

l_giris_miktari = Label(top, text="Giriş Miktarı: ").place(x=10, y=290)
e_giris_miktari = Entry(top, bd=1)
e_giris_miktari.place(x=100,y=290)

l_depo_miktari = Label(top, text="Depo Miktarı: ").place(x=10, y=310)
e_depo_miktari = Entry(top, bd=1)
e_depo_miktari.place(x=100,y=310)

l_kalan_miktar = Label(top, text="Kalan Miktar: ").place(x=10, y=330)
e_kalan_miktar = Entry(top, bd=1)
e_kalan_miktar.place(x=100,y=330)

l_satis_miktari = Label(top, text="Satış Miktarı: ").place(x=10, y=350)
e_satis_miktari = Entry(top, bd=1)
e_satis_miktari.place(x=100,y=350)

b_ekle = Button(top, text="Ekle",command=ekle)
b_ekle.place(x=500,y=250,width=100,height=50)


b_guncelle = Button(top, text="Güncelle",command=guncelle)
b_guncelle.place(x=630,y=250,width=100,height=50)

b_sil = Button(top, text="Sil",command=sil)
b_sil.place(x=500,y=320,width=100,height=50)

b_temizle = Button(top, text="Temizle",command=temizle)
b_temizle.place(x=630,y=320,width=100,height=50)



liste = Treeview(top)
liste["columns"]=("sut1","sut2","sut3","sut4","sut5")
liste.place(x=0,y=0)
liste.heading("#0",text="Id")
liste.heading("sut1",text="Ürün Adı")
liste.heading("sut2",text="Giriş Miktarı")
liste.heading("sut3",text="Depo Miktarı")
liste.heading("sut4",text="Kalan Miktar")
liste.heading("sut5",text="Satış Miktarı")
liste.bind('<ButtonRelease-1>',datagetir)

listele()
top.mainloop()