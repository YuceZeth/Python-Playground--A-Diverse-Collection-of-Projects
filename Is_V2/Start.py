import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import math
import random


def ana():
    top = tkinter.Tk()
    top.title("Ana Ekran")
    top.geometry('350x150')

    def Matematik():
        top2 = tkinter.Tk()
        top2.title("Matematik")
        top2.geometry('350x150')
        top.destroy()

        def karekok():
            top2.destroy()

            def karekok_soru():
                top_karekok = tkinter.Tk()
                top_karekok.title("Karekök")
                top_karekok.geometry('330x400')

                l_cevap = Label(top_karekok, text="Cevap: ").place(x=50, y=280)
                e_cevap = Entry(top_karekok, bd=1)
                e_cevap.place(x=100, y=280)

                photo = PhotoImage(file="asasd.PNG")
                w = Label(top_karekok, image=photo)
                w.place(x=50, y=50)

                rs = random.randint(0, 8)
                rk = [1, 9, 16, 25, 36, 49, 64, 81, 100]
                soru = Label(top_karekok, text='Kök {} kaçtır ?'.format(rk[rs])).place(x=50, y=250)

                def hesap():
                    try:
                        if int(e_cevap.get()) >= 0:
                            cevap = rk[rs] ** (1/2)
                            if int(e_cevap.get()) == cevap:
                                msg = messagebox.showinfo("Sonuç", "Doğru!!!")
                                top_karekok.destroy()
                                karekok_soru()
                            else:
                                msg = messagebox.showinfo("Sonuç", "Yanlış!!!")
                        else:
                            msg = messagebox.showinfo("Sonuç", "Cevap 0'dan Büyük olmalıdır!!!")
                    except ValueError:
                        msg = messagebox.showinfo("Sonuç", "Cevap Giriniz!!!")

                def geri():
                    top_karekok.destroy()
                    ana()

                b_hesapla = Button(top_karekok, text="Hesapla", command=hesap)
                b_hesapla.place(x=35, y=320, width=100, height=50)

                b_geri = Button(top_karekok, text="Geri", command=geri)
                b_geri.place(x=155, y=320, width=100, height=50)

                top_karekok.mainloop()

            karekok_soru()

        def uslu():
            top2.destroy()

            def uslu_soru():
                top_uslu = tkinter.Tk()
                top_uslu.title("Üslü")
                top_uslu.geometry('330x400')

                l_cevap = Label(top_uslu, text="Cevap: ").place(x=50, y=280)
                e_cevap = Entry(top_uslu, bd=1)
                e_cevap.place(x=100, y=280)

                photo = PhotoImage(file="aasdasd.PNG")
                w = Label(top_uslu, image=photo)
                w.place(x=50, y=50)

                rs = random.randint(0, 8)
                rk = random.randint(1, 4)
                soru = Label(top_uslu, text='{} üzeri {} kaçtır ?'.format(rs, rk)).place(x=50, y=250)

                def hesap():
                    try:
                        if int(e_cevap.get()) >= 0:
                            cevap = rs ** rk
                            if int(e_cevap.get()) == cevap:
                                msg = messagebox.showinfo("Sonuç", "Doğru!!!")
                                top_uslu.destroy()
                                uslu_soru()
                            else:
                                msg = messagebox.showinfo("Sonuç", "Yanlış!!!")
                        else:
                            msg = messagebox.showinfo("Sonuç", "Cevap 0'dan Büyük olmalıdır!!!")
                    except ValueError:
                        msg = messagebox.showinfo("Sonuç", "Cevap Giriniz!!!")

                def geri():
                    top_uslu.destroy()
                    ana()

                b_hesapla = Button(top_uslu, text="Hesapla", command=hesap)
                b_hesapla.place(x=35, y=320, width=100, height=50)

                b_geri = Button(top_uslu, text="Geri", command=geri)
                b_geri.place(x=155, y=320, width=100, height=50)

                top_uslu.mainloop()

            uslu_soru()

        uslu = Button(top2, text="Üslü", command=uslu)
        uslu.place(x=200, y=50, width=100, height=50)

        karekok = Button(top2, text="Karekök", command=karekok)
        karekok.place(x=50, y=50, width=100, height=50)

        top2.mainloop()

    def Geometri():
        top2 = tkinter.Tk()
        top2.title("Geometri")
        top2.geometry('350x150')
        top.destroy()

        def ucgen():
            top2.destroy()

            def ucgen_soru():
                top_ucgen = tkinter.Tk()
                top_ucgen.title("Üçgen")
                top_ucgen.geometry('330x400')

                l_cevap = Label(top_ucgen, text="Cevap: ").place(x=50, y=280)
                e_cevap = Entry(top_ucgen, bd=1)
                e_cevap.place(x=100, y=280)

                photo = PhotoImage(file='a.PNG')
                w = Label(top_ucgen, image=photo)
                w.place(x=50, y=50)

                ry = random.randint(1, 10)
                rt = random.randint(1, 10)
                soru = Label(top_ucgen, text='Yüksekliği {} ve tabanı {} olan üçgenin alanı kaçtır ?'
                             .format(ry, 2 * rt)).place(x=50, y=250)

                def hesap():
                    try:
                        if int(e_cevap.get()) >= 0:
                            cevap = (ry * 2 * rt) / 2
                            if int(e_cevap.get()) == cevap:
                                msg = messagebox.showinfo("Sonuç", "Doğru!!!")
                                top_ucgen.destroy()
                                ucgen_soru()
                            else:
                                msg = messagebox.showinfo("Sonuç", "Yanlış!!!")
                        else:
                            msg = messagebox.showinfo("Sonuç", "Alan 0'dan Büyük olmalıdır!!!")
                    except ValueError:
                        msg = messagebox.showinfo("Sonuç", "Cevap Giriniz!!!")

                def geri():
                    top_ucgen.destroy()
                    ana()

                b_hesapla = Button(top_ucgen, text="Hesapla", command=hesap)
                b_hesapla.place(x=35, y=320, width=100, height=50)

                b_geri = Button(top_ucgen, text="Geri", command=geri)
                b_geri.place(x=155, y=320, width=100, height=50)

                top_ucgen.mainloop()

            ucgen_soru()

        def cember():
            top2.destroy()

            def cember_soru():
                top_cember = tkinter.Tk()
                top_cember.title("Çember")
                top_cember.geometry('330x400')

                l_yaricap = Label(top_cember, text="Cevap: ").place(x=50, y=280)
                e_yaricap = Entry(top_cember, bd=1)
                e_yaricap.place(x=100, y=280)

                photo = PhotoImage(file='dairenin-alan-formulu.png')
                w = Label(top_cember, image=photo)
                w.place(x=50, y=50)

                ryr = random.randint(1, 10)
                soru = Label(top_cember, text='Yarıçapı {} olan çemberin alanı kaçtır ?'.format(ryr)).place(x=50, y=250)

                def hesap():
                    try:
                        if int(e_yaricap.get()) >= 0:
                            cevap = 3 * ryr ** 2
                            if int(e_yaricap.get()) == cevap:
                                msg = messagebox.showinfo("Sonuç", "Doğru!!!")
                                top_cember.destroy()
                                cember_soru()
                            else:
                                msg = messagebox.showinfo("Sonuç", "Yanlış!!!")
                        else:
                            msg = messagebox.showinfo("Sonuç", "Alan 0'dan Büyük olmalıdır!!!")
                    except ValueError:
                        msg = messagebox.showinfo("Sonuç", "Cevap Giriniz!!!")

                def geri():
                    top_cember.destroy()
                    ana()

                b_hesapla = Button(top_cember, text="Hesapla", command=hesap)
                b_hesapla.place(x=35, y=320, width=100, height=50)

                b_geri = Button(top_cember, text="Geri", command=geri)
                b_geri.place(x=155, y=320, width=100, height=50)

                top_cember.mainloop()

            cember_soru()

        uslu = Button(top2, text="Çember Alan", command=cember)
        uslu.place(x=200, y=50, width=100, height=50)

        karekok = Button(top2, text="Üçgen Alan", command=ucgen)
        karekok.place(x=50, y=50, width=100, height=50)

        top2.mainloop()

    Matematik = Button(top, text="Matematik", command=Matematik)
    Matematik.place(x=200, y=50, width=100, height=50)

    Geometri = Button(top, text="Geometri", command=Geometri)
    Geometri.place(x=50, y=50, width=100, height=50)

    top.mainloop()


ana()
