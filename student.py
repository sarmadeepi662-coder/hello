from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox


top = Tk()
top.title('Welcome')
top.geometry('1300x750')


def update():
     k1 = int(e1.get())
     k2 = e2.get()
     k3 = e3.get()
     k4 = int(e4.get())
     k5 = int(e5.get())
     format = '%m/%d/%y'
     k6 = cal.get()
     date = datetime.datetime.strptime(k6, format)
     n = date.strftime('%m-%d-%y')
     k7 = c.get()
     k8 = c2.get()
     k9 = c3.get()
     k10 = int(e6.get())
     k11 = var.get()

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     if e2.get()=="" or e3.get() =="" or int(e4.get()) ==""or int(e5.get())==""or date.strftime('%m-%d-%y')=="" or c.get() ==""or c2.get() =="" or c3.get() =="" or int(e6.get()) =="" or var.get()=="":
      messagebox.showinfo("Result", "Please Update All Records")
     else:
         t = (k2,k3,k4,k5,n,k7,k8,k9,k10,k11,k1)
         s = "UPDATE StudentReg SET Name=%s,Lastname=%s,Contact=%s,Age=%s,RegDate=%s,Qualification=%s,City=%s,Course=%s,Fee=%s,Gender=%s WHERE RegistrationId=%s"
         result = cur.execute(s,t)
         if  (result >0):
              messagebox.showinfo("Result", "Record Update Successfully")
         else:
             messagebox.showinfo("Result","Record Not Update")
             db.commit()


def delete():
     k = e1.get()
     import pymysql as sql
     db = sql.connect(host='localhost', user='root',password='mysql',db='aca')
     cur = db.cursor()
     s="DELETE FROM StudentReg WHERE RegistrationId=%s"
     result=cur.execute(s,k)
     if(result>0):
          messagebox.showinfo("Result","Your Delete Successfully")
     else:
          messagebox.showerror("Result",'Record Not Found')
     db.commit()


def  insert():

     k1 = int(e1.get())
     k2 = e2.get()
     k3 = e3.get()
     k4 = int(e4.get())
     k5 =int(e5.get())
     format = '%m/%d/%y'
     k6 = cal.get()
     date = datetime.datetime.strptime(k6,format)
     n = date.strftime('%m-%d-%y')
     k7 = c.get()
     k8 = c2.get()
     k9 = c3.get()
     k10 =int(e6.get())
     k11 = var.get()

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     query = "INSERT INTO StudentReg VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
     result = cur.execute(query, (k1, k2, k3, k4,k5,n, k7, k8,k9,k10,k11))

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
     e5.delete(0, "end")
     e6.delete(0, "end")
     c.delete(0, "end")
     c2.delete(0, "end")
     c3.delete(0, "end")


def Back():
     top.destroy()
     import welcome

def Show():
     for i in tv.get_children():
          tv.delete(i)

     import pymysql as sql
     db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
     cur = db.cursor()
     s = "select * from  StudentReg"
     cur.execute(s)
     result = cur.fetchall()
     for col in result:
          RegistrationId = col[0]
          Name = col[1]
          Lastname = col[2]
          Contact = col[3]
          Age = col[4]
          RegDate = col[5]
          Qualification = col[6]
          City = col[7]
          Course = col[8]
          Fee = col [9]
          Gender=col[10]

          tv.insert("", 'end', values=(RegistrationId,Name, Lastname, Contact, Age, RegDate, Qualification, City,Course,Fee,Gender,))



var=StringVar()

path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"
image=ImageTk.PhotoImage(Image.open(path))

l12=Label(top,bg='black',image=image)
l12.pack()


tv = ttk.Treeview(top)
tv['columns']=('RegistrationId','Name', 'Lastname','Contact','Age','RegDate','Qualification','City','Course','Fee','Gender')
tv.column('#0', width=0, stretch=NO)
tv.column('RegistrationId', anchor=CENTER, width=90)
tv.column('Name', anchor=CENTER, width=60)
tv.column('Lastname', anchor=CENTER, width=70)
tv.column('Contact', anchor=CENTER, width=70)
tv.column('Age', anchor=CENTER, width=50)
tv.column('RegDate', anchor=CENTER, width=70)
tv.column('Qualification', anchor=CENTER, width=80)
tv.column('City', anchor=CENTER, width=60)
tv.column('Course', anchor=CENTER, width=70)
tv.column('Fee', anchor=CENTER, width=40)
tv.column('Gender', anchor=CENTER, width=70)

tv.heading('RegistrationId', text='RegistrationId', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('RegDate', text='RegDate', anchor=CENTER)
tv.heading('Qualification', text='Qualification', anchor=CENTER)
tv.heading('City', text='City', anchor=CENTER)
tv.heading('Course', text='Course', anchor=CENTER)
tv.heading('Fee', text='Fee', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)


tv.place(x=530,y=340)



l=Label(top,text='Student Registration',bg='light coral',relief='sunken',fg='black',font=('Arial 20 bold'))
l.place(x=230,y=10)

l2=Label(top,text='Registration ID',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=0,y=55)

e1=Entry (top,font=('Arial 20 bold'),bg='beige')
e1.place (x=220,y=55)

l2=Label(top,text='Name',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l2.place(x=0,y=100)

e2=Entry (top,font=('Arial 20 bold'),bg='beige')
e2.place (x=220,y=100)

l3=Label(top,text='Lastname',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l3.place(x=0,y=148)

e3=Entry (top,font=('Arial 20 bold'),bg='beige',)
e3.place (x=220,y=148)

l4=Label(top,text='Contact',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l4.place(x=0,y=198)

e4=Entry (top, font=('Arial 20 bold'), bg='beige')
e4.place (x=220,y=198)

l5=Label(top,text='Age',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l5.place(x=0,y=246)

e5=Entry (top,font=('Arial 20 bold'),bg='beige')
e5.place (x=220,y=246)

l6=Label(top,text='RegDate',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l6.place(x=0,y=295)

cal=DateEntry(top,width=19,big="darkblue",fg="white",font=('Arial 20 bold'))
cal.place(x=220,y=295)


l7=Label(top,text='Qualification',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l7.place(x=0,y=344)

k=['Select','BA','Btech','Mtech','Bsc','Msc','MBA','12th','10th']

c=ttk.Combobox(top,values=k,font=('Arial 19 bold'))
c.place(x=220,y=344)
c.current(0)


l8=Label(top,text='City',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=0,y=390)

k=['Select City','Meerut','Jaipur','Delhi','Noida','Kanpur']

c2=ttk.Combobox(top,values=k,font=('Arial 19 bold'))

c2.place(x=220,y=390)
c2.current(0)

l8=Label(top,text='Course',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l8.place(x=0,y=437)

k=['Select subject','PYTHON','JAVA','ML','DSA','EXCEL','REACT','HTML','CSS']

c3=ttk.Combobox(top,values=k,font=('Arial 19 bold'))

c3.place(x=220,y=437)
c3.current(0)

l9=Label(top,text='Fee',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l9.place(x=0,y=484)

e6=Entry (top,font=('Arial 20 bold'),bg='beige')
e6.place (x=220,y=484)


l10=Label(top,text='Gender',bg='beige',relief='sunken',fg='black',font=('Arial 20 bold'))
l10.place(x=0,y=530,)

r=Radiobutton(top,text='Male',value='Male',variable=var,font=('Arial 16 bold'),bg='beige')
r.place(x=220,y=530)

r2=Radiobutton(top,text='Female',value='Female',variable=var,font=('Arial 16 bold'),bg='beige')
r2.place(x=312,y=530)

r3=Radiobutton(top,text='Other',value='Other',variable=var,font=('Arial 16 bold'),bg='beige')
r3.place(x=430,y=530)

r.select()

b=Button(top,text='Submit',bg='light coral',font=('Arial 14 bold'),command =insert)
b.place(x=220,y=585)



b6=Button(top,text='Exit',bg='light coral',font=('Arial 14 bold'),command =exit)
b6.place(x=310,y=585)

b7=Button(top,text='Back',bg='light coral',font=('Arial 14 bold'),command =Back)
b7.place(x=370,y=585)

b7=Button(top,text='Show',bg='light coral',font=('Arial 14 bold'),command =Show)
b7.place(x=440,y=585)

b2=Button(top,text='Delete',bg='light coral',font=('Arial 14 bold'),command =delete)
b2.place(x=518,y=585)

b5=Button(top,text='update',bg='light coral',font=('Arial 14 bold'),command =update)
b5.place(x=610,y=585)
top.config(bg='grey')
top.mainloop()