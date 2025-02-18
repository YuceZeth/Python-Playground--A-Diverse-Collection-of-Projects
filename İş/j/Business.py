import tkinter
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

con = sqlite3.connect("Users.db")
cur = con.cursor()

if cur:
    print("Connection Successful...")


def Message():
    messagebox.showinfo("Result", "Process Completed.")


def Create_Table():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Users (Id INTEGER AUTO_INCREMENT PRIMARY KEY  NOT NULL,Name TEXT, "
        "Last_name TEXT, Age INT, Address TEXT)")
    con.commit()


def Show():
    listt.delete(*listt.get_children())
    conn = sqlite3.connect("Users.db")
    sql = "SELECT * FROM Users"
    cur.execute(sql)
    results = cur.fetchall()
    for rs in results:
        listt.insert("", tk.END, text=rs[0], values=(
            rs[1], rs[2], rs[3], rs[4]))
    conn.close()


def Get_Data(event):
    idno = listt.item(listt.selection()[0])['text']
    sql = "SELECT * FROM Users WHERE Id=%s" % idno
    cur.execute(sql)
    results = cur.fetchone()
    idtxt.delete(0, END)
    idtxt.insert(0, results[0])
    e_Name.delete(0, END)
    e_Name.insert(0, results[1])
    e_Last_Name.delete(0, END)
    e_Last_Name.insert(0, results[2])
    e_Age.delete(0, END)
    e_Age.insert(0, results[3])
    e_Address.delete(0, END)
    e_Address.insert(0, results[4])


def Add():
    try:
        cur.execute("INSERT INTO Users VALUES (?,?,?,?,?)", (
            idtxt.get(), e_Name.get(), e_Last_Name.get(), e_Age.get(), e_Address.get()))
        con.commit()
        Show()
        Message()
    except sqlite3.IntegrityError:
        messagebox.showinfo("Result", "ID Value Should Not Be Repeated...")


def Delete():
    sql = "DELETE FROM Users WHERE Id=%s" % (idtxt.get())
    cur.execute(sql)
    con.commit()
    Show()
    Message()


def Update():
    sql = "UPDATE Users SET Name='%s' ,Last_Name='%s' ,Age='%s' ,Address='%s'  Where Id=%s " % (e_Name.get(),
                                                                                                e_Last_Name.get(),
                                                                                                e_Age.get(),
                                                                                                e_Address.get(),
                                                                                                idtxt.get())
    cur.execute(sql)
    con.commit()
    Show()
    Message()


def Clean():
    idtxt.delete(0, END)
    e_Name.delete(0, END)
    e_Last_Name.delete(0, END)
    e_Age.delete(0, END)
    e_Address.delete(0, END)


top = tkinter.Tk()
top.title("Add User")
top.geometry('1210x400')

l_id = Label(top, text="ID: ").place(x=10, y=250)
idtxt = Entry(top, bd=1)
idtxt.place(x=100, y=250)
l_msg = Label(top, text="Use This Part Without Repetition While Transacting...").place(x=240, y=250)

l_Name = Label(top, text="Name: ").place(x=10, y=275)
e_Name = Entry(top, bd=1)
e_Name.place(x=100, y=275)

l_Last_Name = Label(top, text="Last Name: ").place(x=10, y=300)
e_Last_Name = Entry(top, bd=1)
e_Last_Name.place(x=100, y=300)

l_Age = Label(top, text="Age: ").place(x=10, y=325)
e_Age = Entry(top, bd=1)
e_Age.place(x=100, y=325)

l_Address = Label(top, text="Address: ").place(x=10, y=350)
e_Address = Entry(top, bd=1)
e_Address.place(x=100, y=350)

b_Add = Button(top, text="Add", command=Add)
b_Add.place(x=600, y=250, width=100, height=50)

b_Delete = Button(top, text="Delete", command=Delete)
b_Delete.place(x=600, y=320, width=100, height=50)

b_Update = Button(top, text="Update", command=Update)
b_Update.place(x=730, y=250, width=100, height=50)

b_Clean = Button(top, text="Clean", command=Clean)
b_Clean.place(x=730, y=320, width=100, height=50)

listt = ttk.Treeview(top, column=("column1", "column2", "column3", "column4", "column5"))
listt.place(x=0, y=0)
listt.heading("#0", text="Id")
listt.heading("column1", text="Name")
listt.heading("column2", text="Last Name")
listt.heading("column3", text="Age")
listt.heading("column4", text="Address")
listt.pack()
listt.bind('<ButtonRelease-1>', Get_Data)

Create_Table()
Show()
top.mainloop()
