from tkinter import *

#---------------------------saving Values------------------------------------------------------------------
def getval():
    print("Form submitted")
    print (f"{nameval.get(), genderval.get(), phoneval.get(), emailval.get(), passsval.get(), tncval.get()}")

    with open ("Travel_records.txt", "a") as f:
        f.write (f"{nameval.get(), genderval.get(), phoneval.get(), emailval.get(), passsval.get(), tncval.get()}\n")

def Next():

    r = Tk()
    # GUI logic here
    r.geometry('400x400')  # (widthxhieght)
    r.minsize(200, 250)  # (width, hieght)
    r.maxsize(750,600)     # (width, hieght)



    frame = Frame(r, borderwidth=5, bg="black", relief=SUNKEN)
    frame.pack(side=TOP, anchor="nw")
    label = Label(frame, text="Welcome to learning of GUI in Pycharm")
    label.grid(row=0, column=0)
    b1 = Button(frame, fg="red", text="print 1", padx=5, pady=5, borderwidth=5, relief=RAISED)
    b1.grid()
    b2 = Button(frame, fg="red", text="print 2", padx=5, pady=5, borderwidth=5, relief=RAISED)
    b2.grid()



#-------------------------------Window geometry---------------------------------------------------------------
root = Tk ()
#GUI logic here

#can_wd=680
#can_ht=670

#root.geometry(f'{can_wd}x{can_ht}')  # (widthxhieght)
root.geometry('680x670')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(700,700)     # (width, hieght)
root.title ("Akash's GUI")

#can_widget = Canvas (root, width= can_wd, height= can_ht)
#can_widget.grid()
#can_widget.create_rectangle(0,0,480,470, fill="sky blue")

#-------------------Inserting Photo----------------------------------------------

photo = PhotoImage(file="kismat.png")
akash = Label (image = photo)
akash.grid(row=0, column=1)

#--------------------------displaying Information----------------------------

Label(root, text ="Akash Travels", font="Arial 20 bold", bg="red", fg= "white",padx=70, borderwidth=8, relief=SUNKEN).grid(row=1, column=1, padx=30, pady=5)

Label(root, text ="Welcome to Akash Travels", font="Arial 13 underline", bg="orange", fg= "white",padx=100, borderwidth=3, relief=RAISED).grid(row=2, column=1, padx=30, pady=2)

Label(root, text ="please Reagister first ->", font="Arial 11 italic", bg="light grey", fg= "black",padx=100, borderwidth=2, relief=RAISED).grid(row=3, column=1, padx=30, pady=4)


name= Label (root, text= "Name -> ", font="comicsansms 12", padx=38, pady=3, borderwidth=3, relief=RAISED, fg="blue", bg= "sky blue")
gender = Label (root, text= "Gender -> ", font="comicsansms 12", padx=32, pady=3, borderwidth=3, relief=RAISED, fg="blue", bg= "sky blue")
phone= Label (root, text= "Phone no -> ", font="comicsansms 12", padx=26, pady=3, borderwidth=3, relief=RAISED, fg="blue", bg= "sky blue")
email= Label (root, text= "Email id -> ", font="comicsansms 12", padx=30, pady=3, borderwidth=3, relief=RAISED, fg="blue", bg= "sky blue")
passs = Label (root, text= "Set Password -> ", font="comicsansms 12", padx=10, pady=3, borderwidth=3, relief=RAISED, fg="blue", bg= "sky blue")


name.grid(row=5, column=0)
gender.grid(row=6, column=0)
phone.grid(row=7, column=0)
email.grid(row=8, column=0)
passs.grid(row=9, column=0)

nameval = StringVar()
genderval = StringVar()
phoneval = StringVar()
emailval = StringVar()
passsval = StringVar()
tncval = IntVar()

nameentry= Entry (root, textvariable = nameval)
genderentry= Entry (root, textvariable = genderval)
phoneentry= Entry (root, textvariable = phoneval)
emailentry= Entry (root, textvariable = emailval)
passsentry= Entry (root, textvariable = passsval)

nameentry.grid(row=5, column= 1, )
genderentry.grid(row=6, column=1 )
phoneentry.grid(row=7 , column=1 )
emailentry.grid(row= 8, column=1 )
passsentry.grid(row= 9, column=1 )

#---------------------Check Button--------------------------------------------------------

tnc = Checkbutton (text="I have read all Terms and conditions.",font="comicsansms 12", padx=26, pady=3, borderwidth=3, relief=RAISED, fg="black", bg= "light grey", variable = tncval)
tnc.grid(row=10, column= 1, pady=13)

#----------------------------Submit Button---------------------------------------------------------------

Button(root, text="Submit", font="elephant 12 bold", padx=5, pady=5, borderwidth=5, relief=RAISED, command=getval).grid(row= 11, column=1, pady=5)

Button(root, text="Next", font="elephant 12 bold", padx=5, pady=5, borderwidth=5, relief=RAISED, command=Next).grid(row= 11, column=2, pady=5)

#---------------------------Exit Button------------------------------------------------------------------

#widget = Button(root, text="Exit", font="elephant 12 bold",fg="red", bg="pink", padx=5, pady=5, borderwidth=5, relief=RAISED, command=getval).grid(row= 11, column=1, pady=5)
#widget.bind('<Button-1>', quit)

Label(text="Contact Us -> 9359109196",font="comicsansms 12", padx=20, borderwidth=3, relief=RAISED, fg="black", bg= "light grey").grid(row=12, column=1, pady=8)

#---------------------------Code for Submenu-------------------------------------------------------------


def profile():
    print("There is No profile created to choose")
def project():
    print("There is No project created to choose")
def save():
    print("There is No entry to be saved")
def preview():
    print("There is No parameter project to preview")

def font():
    print("select font Style")
def size():
    print("select font Size")
def appearance():
    print("There is only one Theme available")
def help():
    print("Help yourself with Google :)")

mainmenu = Menu(root)
m1 = Menu (mainmenu, tearoff=0)
m1.add_command(label="Profile", command=profile)
m1.add_command(label="Project", command=project)
m1.add_separator()
m1.add_command(label="Save as", command=save)
m1.add_command(label="Preview", command=preview)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Open", menu=m1)


m2 = Menu (mainmenu, tearoff=0)
m2.add_command(label="Font", command=font)
m2.add_command(label="Size", command=size)
m2.add_command(label="Appearance", command=appearance)
m2.add_separator()
m2.add_command(label="Help", command=help)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Setting",menu=m2)


root.mainloop()