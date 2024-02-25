from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
import webbrowser

# Creating the main Tkinter window
window = tk.Tk()

# Set the window size to full screen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Stegowriting - Hide a Msg In An Image!")
window.resizable(YES, YES)
window.configure(bg="#000000")

# Load the background image
bakgroundimage = PhotoImage(file="A:\Coding\python\College_project/bgimage.png")
Label(window, image=bakgroundimage, bg="#0000FF").place(x=0, y=0)

# Resize the background image
smaller_image = bakgroundimage.subsample(2, 2)

# Function to show the selected image
def showimage():
    global filename  # Declare filename as a global variable
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image',
                                          filetypes=(("Png File", "*.png"),
                                                     ("JPG File", "*.jpg"), ("All file", "*txt")))
    img = Image.open(filename)
    img.thumbnail((500, 300))  # Resize the image to fit within a 250x250 box

    img = ImageTk.PhotoImage(img)

    # Use a Label widget to display the image within a specific area
    lbl_image.configure(image=img)
    lbl_image.image = img

    # Use a Canvas widget to display the image
    #canvas.config(width=250, height=250)
    #canvas.delete("all")
   # canvas.create_image(0, 0, anchor=NW, image=img)
    #canvas.image = img

# Function to hide data in the image
def hide():
    global filename, secret  # Declare filename and secret as global variables
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

# Function to reveal data from the image
def show():
    global filename  # Declare filename as a global variable
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

# Function to save the hidden image
def save():
    global secret  # Declare secret as a global variable
    secret.save("hidden.png")

#Function for About Me!
def aboutme():
    global aboutdev
    messagebox.showinfo('About Me!','I am a program developed by Ajay Kumar Chaudhary. I can hide text into the images and can also show the text hidden into the images. I am a college project on StegnoGraphy!')

#Links to the Social Media
def sociallinks():
    url = "https://www.instagram.com/ajay_01.xx/"
    webbrowser.open_new_tab(url)

#Link Displayed

# ... rest of the code ...

# Create the label for the background image
Label(window, text="Stegowriting", bg="#000000", fg="white", font="courier 25 bold").place(x=565, y=40)     #Main Header
Label(window, text="Image Here!", bg="#000000", fg="white", font="courier 14").place(x=250, y=100)           #Second Text
Label(window, text="Msg Here!", bg="#000000", fg="white", font="courier 14").place(x=1000,y=100)             #Third Text

# The left box frame first
f = Frame(window, bd=3, width=500,height=300, relief=GROOVE)
f.place(x=70, y=140)

# Use a Canvas widget to display the image
#canvas = Canvas(f, bg="white")#, width=500, height=500)
#canvas.pack()
# Use a Label widget to display the image within a specific area
lbl_image = Label(f, bg="white",width=400)
lbl_image.place(x=40, y=10)

#The right box frame second

f2=Frame(window,bd=3,width=500,height=300,relief=GROOVE,bg="white")
f2.place(x=800,y=140)

lbl=Label(f,bg="black")
lbl.place(x=210,y=420)

text1=Text(f2,font="courier 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=800,height=280)

#creating scrollbar

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=800,y=0,height=280)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#creating third frame
f3=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f3.place(x=70,y=570)

Button(f3,text="Open Image",width=10,height=2,font="Courier 14 bold",command=showimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="Courier 14 bold",command=save).place(x=360,y=30)
Label(f3,text="Any Image Format!",font="courier",bg="#2f4155",fg="yellow").place(x=165,y=20)

#creating Fourth frame
f4=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f4.place(x=800,y=570)

Button(f4,text="Hide Data",width=10,height=2,font="Courier 14 bold",command=hide).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="Courier 14 bold",command=show).place(x=360,y=30)
Label(f4,text="Any Image Format!",font="courier",bg="#2f4155",fg="yellow").place(x=165,y=20)

#THIS IS FOR DETECTING THE eXIF dATA! ( PROJECT UNDER DEVELOPMENT )

def detect_exif_data():
    image_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                            filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
   
    if image_path:
        try:
            with Image.open(image_path) as img:
                exif_data = img.getexif()
                if exif_data:
                    messagebox.showinfo('Exif Data Full Exif Data :', exif_data)
                    

                else:
                    messagebox.showwarning('Exif Data','Exif Data Not Found!')
                    
        except Exception as e:
            print(f"Error:{e}")




#def detect_exif_button_click():
 #   detect_exif_data()

#detect_exif_button = Button(window,text="Detect Exif Data",command=detect_exif_button_click)
#detect_exif_button.pack()

#Creating menubar

menubar = Menu(window)

#Adding file menu and commands.

file = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File Menu', menu = file )
file.add_command(label = 'Open Image', command = showimage )
file.add_command(label='Save Image', command= save)
file.add_separator()
file.add_command(label='Exit',command=window.destroy)

#Adding Detect Exif Option

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Detect Exif Data',menu = file )
file.add_command(label='Detect Exif', command= detect_exif_data)
#file.add_command(label='')


#Adding About me section

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label='About',menu = file )
file.add_command(label= ' About Me',command=aboutme)
file.add_command(label='Instagram',command=sociallinks)

window.config(menu = menubar)
window.mainloop()



