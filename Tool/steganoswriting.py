from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

#creating object
window=tk.Tk()

#let's see automatic detection

width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("Stegowriting - Hide a Msg In An Image!")


window.resizable(YES,YES)
window.configure(bg="#000000")

#I changed the root with window variable class and the other configuration are same.

#I like the default icon.

#Background image
bakgroundimage=PhotoImage(file="A:\Coding\python\logo.png")
Label(window,image=bakgroundimage,bg="#0000FF").place(x=10,y=0)

#smaller_image = logo.subsample(2,2)

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image',
                                        filetypes=(("Png File","*.png"),
                                                   ("JPG File","*.jpg"),("All file","*txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

    
    print("")


def Hide():
    print("")

def Show():
    print("")

def Save():
    print("")



Label(window,text="Stegowriting",bg="#000000",fg="white",font="arial 25 bold").place(x=50,y=40)

#The left box frame first

f=Frame(window,bd=3,bg="white",width=500,height=300,relief=GROOVE)
f.place(x=70,y=140)

lbl=Label(f,bg="white")
lbl.place(x=40,y=10)

#The right box frame second

f2=Frame(window,bd=3,width=500,height=300,relief=GROOVE,bg="white")
f2.place(x=800,y=140)

lbl=Label(f,bg="black")
lbl.place(x=210,y=420)

text1=Text(f2,font="arial 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=800,height=280)

#creating scrollbar

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=800,y=0,height=280)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#creating third frame
f3=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f3.place(x=70,y=570)

Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=Save).place(x=360,y=30)
Label(f3,text="Any Image Format!",bg="#2f4155",fg="yellow").place(x=200,y=20)

#creating Fourth frame
f4=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f4.place(x=800,y=570)

Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=360,y=30)
Label(f4,text="Any Image Format!",bg="#2f4155",fg="yellow").place(x=200,y=20)

window.mainloop()



