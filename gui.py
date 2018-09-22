import tkinter
from tkinter import *
import glob
from edit import convert

def setvalues():
    h = int(sbh.get())
    m = int(sbm.get())
    s = int(sbs.get())
    sgn = sign.get()
    #print(h, " ", m, " ", s, " ", sgn)
    a = ""
    if(sgn == 1): a = "+"
    else: a = "-"
    for filename in glob.glob('*.jpg'): #assuming gif
        convert(filename, (h, m, s), a)
    

root = tkinter.Tk()
root.geometry("300x275")
root.title("Change the time!")
icon = PhotoImage(file = 'strawberry.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
#root.configure(background = 'white')

label0 = Label(root, text = "Enter the values")
label0.grid(row = 0, column = 1)
label1 = Label(root, text = "Hours:")

root.grid_rowconfigure(1, minsize=10)

label1.grid(row = 2, column = 0, sticky = W)
sbh = Spinbox(root, from_ = 0, to = 24)
sbh.grid(row = 2, column = 1)

root.grid_rowconfigure(3, minsize=20)  

label2 = Label(root, text = "Minutes:")
label2.grid(row = 4, column = 0,sticky = W)
sbm = Spinbox(root, from_ = 0, to = 60)
sbm.grid(row = 4, column = 1)

root.grid_rowconfigure(5, minsize=20) 

label3 = Label(root, text = "Seconds:")
label3.grid(row = 6, column = 0, sticky = W)
sbs = Spinbox(root, from_ = 0, to = 60)
sbs.grid(row = 6, column = 1)

root.grid_rowconfigure(7, minsize=20)

sign = IntVar()
radd = Radiobutton(root, text = "addition", variable = sign, value = 1)
radd.grid(row = 8, column = 0)

root.grid_rowconfigure(9, minsize=10)
rsub = Radiobutton(root, text = "subtract", variable = sign, value = -1)
rsub.grid(row = 10, column = 0)

root.grid_rowconfigure(11, minsize=20)
btn1 = tkinter.Button(root, text = "offset", command = setvalues)
btn1.grid(row = 12, column = 1)


root.mainloop()
