from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox


top = Tk()
top.title('Login')
top.geometry('1900x1000')


def show():
    if e2.cget('show') == "*":
        e2.config(show='')
    else:
        e2.config(show="*")

def login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mysql', db='batch4pm')
    cur = db.cursor()
    cur.execute("select * from customer where name=%s and password = %s", (e1.get(),e2.get()))
    row = cur.fetchone()

    if row == None:
       messagebox.showerror("Error","Invalid User Name And Password")

    else:
        top.destroy()
        import welcome





path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"
image=ImageTk.PhotoImage(Image.open(path))

l12=Label(top,image=image)
l12.pack()

l=Label(top,text='Login',bg='light coral',relief='sunken',fg='black',font=('Arial 24 bold'))
l.place(x=600,y=50)

l2=Label(top,text='Name',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=350,y=130)

e1=Entry (top,font=('Arial 20 bold'),bg='beige')
e1.place (x=510,y=130)

l3=Label(top,text='Password',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l3.place(x=350,y=200)

e2=Entry (top,font=('Arial 20 bold'),bg='beige',show="*")
e2.place (x=510,y=200)

b=Button(top,text='Login',bg='light coral',relief='sunken',fg='black',font=('Arial 18 bold'),command=login)
b.place(x=600,y=280)

ch=Checkbutton(top,command=show,bg='beige')
ch.place(x=785,y=205)


top.config(bg='pink')
top.mainloop()