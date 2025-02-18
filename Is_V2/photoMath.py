import tkinter
from tkinter import *
from tkinter import messagebox


def ana():
    top = tkinter.Tk()
    top.title("Ana Ekran")
    top.geometry('360x140')

    def denklem():
        top.destroy()

        def soru():
            top_denklem = tkinter.Tk()
            top_denklem.title("Denklemler")
            top_denklem.geometry('300x150')

            Label(top_denklem, text="Örneğin: 3x+5=8").place(x=100, y=10)
            Label(top_denklem, text="Soru: ").place(x=65, y=40)
            e_soru = Entry(top_denklem, bd=1)
            e_soru.place(x=100, y=40)

            def hesapla():
                cozum_dizisi = list(e_soru.get())
                katsayi = list()
                for i in cozum_dizisi:
                    if i == 'x':
                        break
                    else:
                        katsayi.append(int(i))
                katsayi.reverse()

                a = 0
                kat = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
                for i in range(0, len(katsayi)):
                    a = a + katsayi[i] * kat[i]
                print("x'in katsayısı :", a)

                b = 0
                for i in range(0, len(cozum_dizisi)):
                    if cozum_dizisi[i] == '+':
                        b = int(cozum_dizisi[i + 1])
                        break
                    elif cozum_dizisi[i] == '-':
                        b = -int(cozum_dizisi[i + 1])
                        break
                print("Sabit sayı :", b)

                c = 0
                for i in range(0, len(cozum_dizisi)):
                    if cozum_dizisi[i] == '=':
                        if cozum_dizisi[i + 1] == '-':
                            c = -int(cozum_dizisi[i + 2])
                        else:
                            c = int(cozum_dizisi[i + 1])
                print("Eşitliğin sağı : ", c)

                try:
                    x = (c - b) / a
                    messagebox.showinfo("Sonuç", "x = {}".format(x))
                except ZeroDivisionError:
                    messagebox.showinfo("Hata", "Bir Soru Giriniz!!!")
                except ValueError:
                    messagebox.showinfo("Hata", "Değişken Mevcut Değil!!!")

            def geri():
                top_denklem.destroy()
                ana()

            b_hesapla = Button(top_denklem, text="Hesapla", command=hesapla)
            b_hesapla.place(x=35, y=75, width=100, height=50)

            b_geri = Button(top_denklem, text="Geri", command=geri)
            b_geri.place(x=155, y=75, width=100, height=50)

            top_denklem.mainloop()

        soru()

    def turev():
        top.destroy()

        def soru():
            top_turev = tkinter.Tk()
            top_turev.title("Türev")
            top_turev.geometry('300x150')

            Label(top_turev, text="Örneğin: 3x^2+5x+20").place(x=110, y=10)
            Label(top_turev, text="Soru: ").place(x=65, y=40)
            e_soru = Entry(top_turev, bd=1)
            e_soru.place(x=100, y=40)

            def hesapla():
                pass

            def geri():
                top_turev.destroy()
                ana()

            b_hesapla = Button(top_turev, text="Hesapla", command=hesapla)
            b_hesapla.place(x=35, y=75, width=100, height=50)

            b_geri = Button(top_turev, text="Geri", command=geri)
            b_geri.place(x=155, y=75, width=100, height=50)

            top_turev.mainloop()

        soru()

    b_denklem = Button(top, text="Birinci Dereceden Denklemler", command=denklem)
    b_denklem.place(x=150, y=45, width=180, height=50)

    b_turev = Button(top, text="Turev", command=turev)
    b_turev.place(x=30, y=45, width=100, height=50)

    top.mainloop()


ana()
