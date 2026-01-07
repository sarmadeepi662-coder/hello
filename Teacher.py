from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox


top = Tk()
top.title('Welcome')
top.geometry('1300x750')


def  insert():

     k1 = e1.get()
     k2 = e2.get()
     k3 = int(e3.get())
     k4 = int(e4.get())
     format = '%m/%d/%y'
     k5 = cal.get()
     date = datetime.datetime.strptime(k5,format)
     n = date.strftime('%m-%d-%y')
     k6 = c2.get()
     k7 = c3.get()
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

     e1.delete(0, "end")
     e2.delete(0, "end")
     e3.delete(0, "end")
     e4.delete(0, "end")
     c.delete(0, "end")
     c2.delete(0, "end")
     c3.delete(0, "end")


def Back():
     top.destroy()
     import welcome


def show2():
     for i in tv.get_children():
          tv.delete(i)

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     s = "select * from TeacherData"
     cur.execute(s)
     result = cur.fetchall()
     for col in result:
          name = col[0]
          lastname = col[1]
          contact = col[2]
          age = col[3]
          Dob = col[4]
          qualification = col[5]
          city = col[6]
          subject = col[7]
          experience = col = [9]
          gender=col=[9]

          tv.insert("", 'end', values=(name, lastname, contact, age, Dob, qualification, city,subject,experience, gender,))


def TeacherInsurt():
     k1 = e1.get()
     k2 = e2.get()
     k3 = int(e3.get())
     k4 = int(e4.get())
     format = '%m/%d/%y'
     k5 = cal.get()
     date = datetime.datetime.strptime(k5, format)
     n  = date.strftime('%m-%d-%y')
     k6 = c.get()
     k7 = c2.get()
     k8 = c3.get()
     k9 = e9.get()
     k10 = var.get()


     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     query = "INSERT INTO TeacherData VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
     result = cur.execute(query, (k1, k2, k3, k4, n, k6, k7, k8,k9,k10))

     if result > 0:
          messagebox.showinfo("Result", "Your Record Inserted Successfully")
     else:
          messagebox.showwarning("Result", "Record Not Inserted")

     db.commit()
     db.close()

     e1.delete(0, "end")
     e2.delete(0, "end")
     e3.delete(0, "end")
     e4.delete(0, "end")
     e9.delete(0, "end")



var=StringVar()

path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"
image=ImageTk.PhotoImage(Image.open(path))
l12=Label(top,bg='black',image=image)
l12.pack()

tv = ttk.Treeview(top)
tv['columns']=('Name', 'Lastname','Contact','Age','DOB','Qualification','City','Subject','Experience','Gender')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=60)
tv.column('Lastname', anchor=CENTER, width=60)
tv.column('Contact', anchor=CENTER, width=80)
tv.column('Age', anchor=CENTER, width=60)
tv.column('DOB', anchor=CENTER, width=60)
tv.column('Qualification', anchor=CENTER, width=60)
tv.column('City', anchor=CENTER, width=60)
tv.column('Subject', anchor=CENTER, width=60)
tv.column('Experience', anchor=CENTER, width=80)
tv.column('Gender', anchor=CENTER, width=60)

tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('DOB', text='DOB', anchor=CENTER)
tv.heading('Qualification', text='Qualification', anchor=CENTER)
tv.heading('City', text='City', anchor=CENTER)
tv.heading('Subject', text='Subject', anchor=CENTER)
tv.heading('Experience', text='Experience', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)

tv.place(x=610,y=350)



l=Label(top,text='TeacherRegistration',bg='light coral',relief='sunken',fg='black',font=('Arial 20 bold'))
l.place(x=320,y=25)

l2=Label(top,text='Name',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=90,y=100)

e1=Entry (top,font=('Arial 20 bold'),bg='beige')
e1.place (x=300,y=100)

l3=Label(top,text='Lastname',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l3.place(x=90,y=148)

e2=Entry (top,font=('Arial 20 bold'),bg='beige',)
e2.place (x=300,y=148)

l4=Label(top,text='Contact',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l4.place(x=90,y=198)

e3=Entry (top, font=('Arial 20 bold'), bg='beige')
e3.place (x=300,y=198)

l5=Label(top,text='Age',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l5.place(x=90,y=246)

e4=Entry (top,font=('Arial 20 bold'),bg='beige')
e4.place (x=300,y=246)

l6=Label(top,text='Dob',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l6.place(x=90,y=295)

cal=DateEntry(top,width=19,big="darkblue",fg="white",font=('Arial 20 bold'))
cal.place(x=300,y=295)


l7=Label(top,text='Qualification',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l7.place(x=90,y=344)

k=['Select','BA','Btech','Mtech','Bsc','Msc','MBA']

c=ttk.Combobox(top,values=k,font=('Arial 19 bold'))
c.place(x=300,y=344)
c.current(0)


l8=Label(top,text='City',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=90,y=390)

k=['Select City','Meerut','Jaipur','Delhi','Noida','Kanpur']

c2=ttk.Combobox(top,values=k,font=('Arial 19 bold'))

c2.place(x=300,y=390)
c2.current(0)

l8=Label(top,text='Subject',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=90,y=437)

k=['Select subject','PYTHON','JAVA','ML','DSA','EXCEL','REACT','HTML','CSS']

c3=ttk.Combobox(top,values=k,font=('Arial 19 bold'))

c3.place(x=300,y=437)
c3.current(0)

l8=Label(top,text='EXPERIENCE',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=90,y=484)

e9=Entry (top,font=('Arial 20 bold'),bg='beige')
e9.place (x=300,y=484)


l9=Label(top,text='Gender',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l9.place(x=90,y=530,)

r=Radiobutton(top,text='Male',value='Male',variable=var,font=('Arial 16 bold'),bg='beige')
r.place(x=300,y=530)

r2=Radiobutton(top,text='Female',value='Female',variable=var,font=('Arial 16 bold'),bg='beige')
r2.place(x=395,y=530)

r3=Radiobutton(top,text='Other',value='Other',variable=var,font=('Arial 16 bold'),bg='beige')
r3.place(x=515,y=530)

r.select()

b=Button(top,text='Submit',bg='light coral',font=('Arial 14 bold'),command =TeacherInsurt)
b.place(x=300,y=585)


b6=Button(top,text='Exit',bg='light coral',font=('Arial 14 bold'),command =exit)
b6.place(x=393,y=585)

b7=Button(top,text='Back',bg='light coral',font=('Arial 14 bold'),command =Back)
b7.place(x=457,y=585)

b3=Button(top,text='Show',bg='light coral',font=('Arial 14 bold'),command =show2)
b3.place(x=530,y=585)




top.config(bg='grey')
top.mainloop()