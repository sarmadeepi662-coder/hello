from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter import messagebox
from tkinter import ttk


top = Tk()
top.title('Welcom')
top.geometry('1300x800')


def student():
    top.destroy()
    import student

def course():
    top.destroy()
    import course


def Search():
    for i in tv.get_children():
        tv.delete(i)

    s7=e12.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
    cur = db.cursor()
    s = "select * from TeacherData where name=%s"
    cur.execute(s,s7)
    result = cur.fetchall()
    for col in result:
        Name = col[0]
        Lastname = col[1]
        Contact = col[2]
        Age = col[3]
        Dob = col[4]
        Qualification = col[5]
        City = col[6]
        Subject = col[7]
        Experience = col[8]
        Gender = col[9]

        tv.insert("", 'end',values=(Name, Lastname, Contact, Age, Dob, Qualification, City, Subject, Experience, Gender))

def Search2():
    s7 = e12.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
    cur = db.cursor()
    s = "select * from Course where CourseName=%s"
    cur.execute(s,s7)
    result = cur.fetchall()
    for col in result:
        CourseName = col[0]
        Duration = col[1]
        Fee = col[2]
        Teacher = col[3]
        Time = col[4]
        Mode = col[5]
        tv.insert("", 'end', values=(CourseName, Duration, Fee, Teacher, Time, Mode))


def teacher():
    top.destroy()
    import Teacher

def ShowTeacher():
    global tv
    tv = ttk.Treeview(top, height=17)
    tv['columns'] = ('Name','Lastname','Contact','Age','Dob','Qualification','City','Subject','Experience','Gender')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=CENTER, width=120)
    tv.column('Lastname', anchor=CENTER, width=120)
    tv.column('Contact', anchor=CENTER, width=120)
    tv.column('Age', anchor=CENTER, width=120)
    tv.column('Dob', anchor=CENTER, width=120)
    tv.column('Qualification', anchor=CENTER, width=120)
    tv.column('City', anchor=CENTER, width=120)
    tv.column('Subject', anchor=CENTER, width=120)
    tv.column('Experience', anchor=CENTER, width=120)
    tv.column('Gender', anchor=CENTER, width=120)

    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Lastname', text='Lastname', anchor=CENTER)
    tv.heading('Contact', text='Contact', anchor=CENTER)
    tv.heading('Age', text='Age', anchor=CENTER)
    tv.heading('Dob', text='Dob', anchor=CENTER)
    tv.heading('Qualification', text='Qualification', anchor=CENTER)
    tv.heading('City', text='City', anchor=CENTER)
    tv.heading('Subject', text='Subject', anchor=CENTER)
    tv.heading('Experience', text='Experience', anchor=CENTER)
    tv.heading('Gender', text='Gender', anchor=CENTER)

    tv.place(x=30, y=250)

    for i in tv.get_children():
        tv.delete(i)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
    cur = db.cursor()
    s = "select * from TeacherData"
    cur.execute(s)
    result = cur.fetchall()
    for col in result:
        Name = col[0]
        Lastname = col[1]
        Contact = col[2]
        Age = col[3]
        Dob = col[4]
        Qualification = col[5]
        City = col[6]
        Subject = col[7]
        Experience = col[8]
        Gender = col[9]

        tv.insert("", 'end', values=(Name, Lastname, Contact, Age, Dob,Qualification,City,Subject,Experience,Gender))



def Show():
    global tv
    tv = ttk.Treeview(top, height=17)
    tv['columns'] = ('CourseName','Duration','CourseFee','TeacherName','Time','CourseMode')
    tv.column('#0', width=0, stretch=NO)
    tv.column('CourseName', anchor=CENTER, width=180)
    tv.column('Duration', anchor=CENTER, width=180)
    tv.column('CourseFee', anchor=CENTER, width=200)
    tv.column('TeacherName', anchor=CENTER, width=220)
    tv.column('Time', anchor=CENTER, width=200)
    tv.column('CourseMode', anchor=CENTER, width=220)


    tv.heading('CourseName',text='CourseName',anchor=CENTER)
    tv.heading('Duration',text='Duration',anchor=CENTER)
    tv.heading('CourseFee',text='CourseFee',anchor=CENTER)
    tv.heading('TeacherName',text='TeacherName',anchor=CENTER)
    tv.heading('Time', text='Time', anchor=CENTER)
    tv.heading('CourseMode',text='CourseMode',anchor=CENTER)


    tv.place(x=30, y=250)

    for i in tv.get_children():
        tv.delete(i)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mysql', db='aca')
    cur = db.cursor()
    s = "select * from Course"
    cur.execute(s)
    result = cur.fetchall()
    for col in result:
        coursename = col[0]
        duration = col[1]
        fee = col[2]
        teacher = col[3]
        time = col[4]
        mode = col[5]
        tv.insert("", 'end', values=(coursename, duration, fee, teacher, time,mode))


path=r"C:\Users\parba\Downloads\night-city-street-low-angle-d-rendering-night-city-panorama-view-hdri-d-rendering-environment-map-spherical-panorama-dark-sky-245761904.webp"

image=ImageTk.PhotoImage(Image.open(path))

l12=Label(top,image=image)
l12.pack()




l=Label(top,text='welcome',bg='light coral',font=('Arial 25 bold'))
l.place(x=600,y=20)

b7=Button(top,text='TeacherADD',bg='light coral',font=('Arial 14 bold'),command=teacher)
b7.place(x=110,y=110)

b8=Button(top,text='StudentRegistration',bg='light coral',font=('Arial 14 bold'),command=student)
b8.place(x=300,y=110)

b9=Button(top,text='ShowCourses',bg='light coral',font=('Arial 14 bold'),command=Show)
b9.place(x=550,y=110)

b10=Button(top,text='ADDCourse',bg='light coral',font=('Arial 14 bold'),command=course)
b10.place(x=740,y=110)

b10=Button(top,text='Exit',bg='light coral',font=('Arial 14 bold'),command=exit)
b10.place(x=910,y=110)

b10=Button(top,text='ShowTeacher',bg='light coral',font=('Arial 14 bold'),command=ShowTeacher)
b10.place(x=1005,y=110)

l=Label(top,text='SearchCourse',bg='light coral',font=('Arial 18 bold'))
l.place(x=300,y=190)

e12=Entry (top, font=('Arial 20 bold'), bg='beige')
e12.place (x=500,y=190,width=240)

b10=Button(top,text='Search',bg='light coral',font=('Arial 14 bold'),command=lambda:[Search(),Search2()])
b10.place(x=760,y=190,height=33)



top.config(bg='black')
top.mainloop()