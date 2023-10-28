from tkinter import *
import random
from datetime import *
import re

i=0
gender=""
Student= open("StudentInfo.txt","a+")
Data =open("Data.txt","a+")

def save_info():
    global i
    datetime1=datetime.now()
    Student = open("StudentInfo.txt", "a+")
    Name = e1.get()
    Roll_no = e2.get()
    Division= e3.get()
    Mobile_no= e4.get()
    Address= e5.get()
    Student.write("DateTime :"+ str(datetime1))
    Student.write("\nStudent no: " +str(i+1))
    Student.write("\nName :"+Name)
    Student.write("\nRoll No : :"+Roll_no)
    Student.write("\nDivision :"+Division)
    Student.write("\nMobile No  :"+Mobile_no)
    Student.write("\nAddress  :"+Address)
    Student.write("\nDivision :"+Division)
    Student.write("\nGender :"+v.get())
    Student.write("\n")
    i+=1
def search(pattern):
    res1=re.search(pattern, data)


def close(root):
    global i
    Data.write("Total Entries :"+str(i+1))
    root.destroy()

def display():
    pass
def color_changer():
    fg = random.choice(colors)
    l7.config(fg=fg,bg="deep sky blue",borderwidth=5, relief ="raised")
    l7.after(200, color_changer)


    labels = ["Student info Genrator", "Student info Genrator"]

    text = random.choice(labels)
    l7.config(text=text)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)







colors = ["black", "red" , "green" , "blue","yellow","white"]
root = Tk()
root.title("Form submission")
root.geometry('1366x768')
bg =PhotoImage(file=r"E:\Vedant\Projects\Student Register(txt)\Background.png")
b1 = Label(root,image=bg)
b1.place(x=0,y=0)
v =StringVar(root,"1")


e1 = Entry(root,border=1, width=60,font=('Helvetica',10,'bold','italic'),borderwidth=3,relief ="ridge")
e2 = Entry(root, border=1, width=60,font=('Helvetica',10,'bold','italic'),borderwidth=3,relief ="ridge")
e3 = Entry(root, border=1, width=60,font=('Helvetica',10,'bold','italic'),borderwidth=3,relief ="ridge")
e4 = Entry(root, border=1, width=60,font=('Helvetica',10,'bold','italic'),borderwidth=3,relief ="ridge")
e5 = Entry(root, border=1, width=60,font=('Helvetica',10,'bold','italic'),borderwidth=3,relief ="ridge")
e1.place(relx=0.35, rely=0.15)
e2.place(relx=0.35, rely=0.20)
e3.place(relx=0.35, rely=0.25)
e4.place(relx=0.35, rely=0.30)
e5.place(relx=0.35, rely=0.35)

l1=Label(root,text="Name :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l2=Label(root,text="Roll no :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l3=Label(root,text="Division :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l4=Label(root,text="Mobile No :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l5=Label(root,text="Address :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l6=Label(root,text="Gender :",fg="white",bg="#4052AB",font=('Helvetica',15,'bold','italic'),borderwidth=2, relief ="raised")
l7=Label(root,bg="#4052AB",font=('Helvetica',30,'bold','italic'))
l1.place(relx=0.25,rely=0.15)
l2.place(relx=0.25,rely=0.20)
l3.place(relx=0.25,rely=0.25)
l4.place(relx=0.25,rely=0.30)
l5.place(relx=0.25,rely=0.35)
l6.place(relx=0.25,rely=0.4)
l7.place(relx=0.35,rely=0.0)



c1=Radiobutton(root,text ="Male",value="Male",variable=v,bg="#4052AB",font=('Helvetica',10,'bold','italic'))
c2=Radiobutton(root,text ="Female",value="Female",variable=v,bg="#4052AB",font=('Helvetica',10,'bold','italic'))
c3=Radiobutton(root,text ="Other",value="Other",variable=v,bg="#4052AB",font=('Helvetica',10,'bold','italic'))

c1.place(relx=0.35,rely=0.4)
c2.place(relx=0.35,rely=0.45)
c3.place(relx=0.35,rely=0.5)


submit1= Button(root ,text ="Submit",bg="Green",font = ('Comic Sas MS',20,'bold'),padx=10,pady=5,borderwidth=3,command=lambda:save_info())
submit1.place(relx=0.6,rely=0.6)

exit =Button(root,text ="Exit",command=lambda:close(root),bg="Red",padx=10,pady=5,font = ('Comic Sas MS',20,'bold'),borderwidth=3)
exit.place(relx=0.48,rely=0.6)

clear1 =Button(root,text="Clear",command=lambda:clear(),bg="White",font = ('Comic Sas MS',20,'bold'),padx=10,pady=5,borderwidth=3)
clear1.place(relx=0.35,rely=0.6)



color_changer()
root.mainloop()
