from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox


top = Tk()
top.title('Welcome')
top.geometry('1300x750')

def exit():
     top.destroy()


def show():
     if e5.cget('show') == "*":
          e5.config(show='')
     else:
          e5.config(show="*")


def show2():
     for i in tv.get_children():
         tv.delete(i)

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='batch4pm')
     cur = db.cursor()
     s="select * from customer"
     cur.execute(s)
     result=cur.fetchall()
     for col in result :
          name=col[0]
          lastname=col[1]
          contact=col[2]
          age=col[3]
          Dob=col[4]
          password=col[5]
          city=col[6]
          gender=col[7]
          tv.insert("",'end',values=(name,lastname,contact,age,Dob,password,city,gender,))

def search():
     k = e1.get()

     for i in tv.get_children():
         tv.delete(i)

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='batch4pm')
     cur = db.cursor()
     s="select * from customer where name=%s "
     cur.execute(s,k)
     result=cur.fetchall()
     for col in result :
          name=col[0]
          lastname=col[1]
          contact=col[2]
          age=col[3]
          Dob=col[4]
          password=col[5]
          city=col[6]
          gender=col[7]
          tv.insert("",'end',values=(name,lastname,contact,age,Dob,password,city,gender))

def update():
     k1 = e1.get()
     k2 = e2.get()
     k3 = int(e3.get())
     k4 = int(e4.get())
     format = '%m/%d/%y'
     k5 = cal.get()
     date = datetime.datetime.strptime(k5, format)
     n = date.strftime('%m-%d-%y')
     k6 = e5.get()
     k7 = c.get()
     k8 = var.get()

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='batch4pm')
     cur = db.cursor()
     if e2.get()=="" or int(e3.get()) =="" or int(e4.get()) =="" or date.strftime('%m-%d-%y')==""or e5.get()=="" or c.get() =="" or var.get()=="":
      messagebox.showinfo("Result", "Please Update All Records")
     else:
         t = (k1,k2,k3,k4,n,k6,k7,k8)
         s = "UPDATE CUSTOMER SET lastname=%s,contact=%s,age=%s,Dob=%s,password=%s,city=%s,gender=%s WHERE name=%s"
         result = cur.execute(s,t)
         if  (result >0):
              messagebox.showinfo("Result", "Record Update Successfully")
         else:
             messagebox.showinfo("Result","Record Not Update")
             db.commit()


def delete():
     k = e1.get()
     import pymysql as sql
     db = sql.connect(host='localhost', user='root',password='mysql',db='batch4pm')
     cur = db.cursor()
     s="delete from customer where name=%s"
     result=cur.execute(s,k)
     if(result>0):
          messagebox.showinfo("Result","Your Delete Successfully")
     else:
          messagebox.showerror("Result",'Record Not Found')
     db.commit()

def  insert():

     k1 = e1.get()
     k2 = e2.get()
     k3 = int(e3.get())
     k4 = int(e4.get())
     format = '%m/%d/%y'
     k5 = cal.get()
     date = datetime.datetime.strptime(k5,format)
     n = date.strftime('%m-%d-%y')
     k6 = e5.get()
     k7 = c.get()
     k8 = var.get()

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='batch4pm')
     cur = db.cursor()
     query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
     result = cur.execute(query, (k1, k2, k3, k4, n, k6, k7, k8))

     if result > 0:
          messagebox.showinfo("Result", "Your Record Inserted Successfully")
     else:
          messagebox.showwarning("Result", "Record Not Inserted")

     db.commit()
     db.close()

     e1.delete(0,"end")
     e2.delete(0, "end")
     e3.delete(0, "end")
     e4.delete(0, "end")
     c.delete(0, "end")

def login():
     top.destroy()
     import lala


var=StringVar()

path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"
image=ImageTk.PhotoImage(Image.open(path))
l12=Label(top,image=image)
l12.pack()


tv = ttk.Treeview(top)
tv['columns']=('Name', 'Lastname','Contact','Age','DOB','Password','Gender','City')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=70)
tv.column('Lastname', anchor=CENTER, width=70)
tv.column('Contact', anchor=CENTER, width=70)
tv.column('Age', anchor=CENTER, width=60)
tv.column('DOB', anchor=CENTER, width=70)
tv.column('Password', anchor=CENTER, width=70)
tv.column('Gender', anchor=CENTER, width=60)
tv.column('City', anchor=CENTER, width=70)


tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('DOB', text='DOB', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.heading('City', text='City', anchor=CENTER)

tv.place(x=720,y=390)


l=Label(top,text='Registration',bg='light coral',relief='sunken',fg='black',font=('Arial 20 bold'))
l.place(x=470,y=20)

l2=Label(top,text='Name',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=230,y=90)

e1=Entry (top,font=('Arial 20 bold'),bg='beige')
e1.place (x=400,y=90)

l3=Label(top,text='Lastname',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l3.place(x=230,y=138)

e2=Entry (top,font=('Arial 20 bold'),bg='beige',)
e2.place (x=400,y=138)

l4=Label(top,text='Contact',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l4.place(x=230,y=185)

e3=Entry (top, font=('Arial 20 bold'), bg='beige')
e3.place (x=400,y=185)

l5=Label(top,text='Age',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l5.place(x=230,y=232)

e4=Entry (top,font=('Arial 20 bold'),bg='beige')
e4.place (x=400,y=232)

l6=Label(top,text='DOB',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l6.place(x=230,y=279)

cal=DateEntry(top,width=19,big="darkblue",fg="white",font=('Arial 20 bold'))
cal.place(x=400,y=279)


l7=Label(top,text='Password',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l7.place(x=230,y=329)

e5=Entry (top,font=('Arial 20 bold'),bg='beige',show='*')
e5.place (x=400,y=329)


l8=Label(top,text='City',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=230,y=376)

k=['Select City','Meerut','Jaipur','Delhi','Noida','Kanpur']

c=ttk.Combobox(top,values=k,font=('Arial 19 bold'))

c.place(x=400,y=376)
c.current(0)


l9=Label(top,text='Gender',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l9.place(x=230,y=425,)

r=Radiobutton(top,text='Male',value='Male',variable=var,font=('Arial 16 bold'),bg='beige')
r.place(x=400,y=425)

r2=Radiobutton(top,text='Female',value='Female',variable=var,font=('Arial 16 bold'),bg='beige')
r2.place(x=492,y=425)

r3=Radiobutton(top,text='Other',value='Other',variable=var,font=('Arial 16 bold'),bg='beige')
r3.place(x=610,y=425)

r.select()

b=Button(top,text='Submit',bg='light coral',font=('Arial 14 bold'),command =insert)
b.place(x=430,y=480)

b2=Button(top,text='Delete',bg='light coral',font=('Arial 14 bold'),command =delete)
b2.place(x=520,y=480)

b3=Button(top,text='Show',bg='light coral',font=('Arial 14 bold'),command =show2)
b3.place(x=605,y=480)

b4=Button(top,text='search',bg='light coral',font=('Arial 14 bold'),command =search)
b4.place(x=430,y=535)

b5=Button(top,text='update',bg='light coral',font=('Arial 14 bold'),command =update)
b5.place(x=520,y=535)

b6=Button(top,text='Login',bg='light coral',font=('Arial 14 bold'),command =login)
b6.place(x=610,y=535)

b7=Button(top,text='Exit',bg='light coral',font=('Arial 14 bold'),command =exit)
b7.place(x=535,y=585)

ch=Checkbutton(top,command=show,bg='beige')
ch.place(x=670,y=335)





top.config(bg='pink')
top.mainloop()