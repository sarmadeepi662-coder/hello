from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox


top = Tk()
top.title('Welcome')
top.geometry('1300x650')

def Back():
     top.destroy()
     import welcome




def exit():
     top.destroy()




def insert():
     k1 = e1.get()
     k2 = e2.get()
     k3 = int(e3.get())
     k4 = e4.get()
     k5 = e5.get()
     k6 = e6.get()


     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     query = "INSERT INTO course VALUES (%s, %s, %s, %s, %s, %s)"
     result = cur.execute(query, (k1, k2, k3, k4, k5, k6,))

     if result > 0:
          messagebox.showinfo("Result", "Your Course Add Successfully")
     else:
          messagebox.showwarning("Result", " Not Inserted")

     db.commit()
     db.close()

     e1.delete(0, "end")
     e2.delete(0, "end")
     e3.delete(0, "end")
     e4.delete(0, "end")
     e5.delete(0, "end")
     e6.delete(0,"end")



var=StringVar()

path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"
image=ImageTk.PhotoImage(Image.open(path))

l12=Label(top,bg='black',image=image)
l12.pack()




l=Label(top,text='CourseADD',bg='light coral',relief='sunken',fg='black',font=('Arial 20 bold'))
l.place(x=650,y=25)

l2=Label(top,text='CourseName',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=380,y=100)

e1=Entry (top,font=('Arial 20 bold'),bg='beige')
e1.place (x=590,y=100)

l3=Label(top,text='Duration',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l3.place(x=380,y=148)

e2=Entry (top,font=('Arial 20 bold'),bg='beige',)
e2.place (x=590,y=148)

l4=Label(top,text='CourseFee',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l4.place(x=380,y=198)

e3=Entry (top, font=('Arial 20 bold'), bg='beige')
e3.place (x=590,y=198)

l5=Label(top,text='TeacherName',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l5.place(x=380,y=246)

e4=Entry (top,font=('Arial 20 bold'),bg='beige')
e4.place (x=590,y=246)

l6=Label(top,text='Time',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l6.place(x=380,y=295)

e5=Entry (top,font=('Arial 20 bold'),bg='beige')
e5.place (x=590,y=295)

l7=Label(top,text='CourseMode',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l7.place(x=380,y=345)

e6=Entry (top,font=('Arial 20 bold'),bg='beige')
e6.place (x=590,y=345)

b=Button(top,text='Submit',bg='light coral',font=('Arial 14 bold'),command=insert)
b.place(x=620,y=400)

b6=Button(top,text='Exit',bg='light coral',font=('Arial 14 bold'),command =exit)
b6.place(x=720,y=400)

b7=Button(top,text='Back',bg='light coral',font=('Arial 14 bold'),command =Back)
b7.place(x=790,y=400)







top.config(bg='grey')
top.mainloop()