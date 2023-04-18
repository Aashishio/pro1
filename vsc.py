from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()

root.title("Copyright Visual Studio Code")

root.configure(background="#C0C0C0")
root.minsize(700, 700)
root.maxsize(700, 700)

imgOpen = ImageTk.PhotoImage(Image.open("open_file.png"))
imgRun = ImageTk.PhotoImage(Image.open("run.png"))
imgSave = ImageTk.PhotoImage(Image.open("save_file.png"))

label_FileName = Label(root, text="File Name :")
label_FileName.place(relx=0.35, rely=0.03, anchor=CENTER)

input_FileName = Entry(root)
input_FileName.place(relx=0.50, rely=0.03, anchor=CENTER)
input_FileName.configure(bg="grey")

text = Text(root, width=80, height=35)
text.place(relx=0.5, rely=0.55, anchor=CENTER)
text.configure(bg="grey")

name = ""

def openFile():
    global name
    text.delete(1.0, END)
    input_FileName.delete(0, END)
    openFile = filedialog.askopenfilename(title="Open File", filetypes =(("html files", "*.html"),))
    print(openFile)
    name = os.path.basename(openFile)
    filename = name.split(".")[0]
    input_FileName.insert(END, filename)
    root.title(filename)
    fileInputs = open(name, 'rw')
    paragraph = fileInputs.read()
    text.insert(END, paragraph)
    fileInputs.close()

def save():
    namebyUser = input_FileName.get()
    file = open(namebyUser+".html", "w")
    data = text.get("1.0", END)
    file.write(data)
    text.delete(1.0, END)
    input_FileName.delete(0, END)
    messagebox.showinfo("Update", "Success!")

img_OpenBtn = Button(root, image=imgOpen, text="Open", command=openFile)
img_OpenBtn.place(relx=0.07, rely=0.03, anchor=CENTER)

img_SaveBtn = Button(root, image=imgSave, text="Save", command=save)
img_SaveBtn.place(relx=0.13, rely=0.03, anchor=CENTER)

img_RunBtn = Button(root, image=imgRun, text="Run")
img_RunBtn.place(relx=0.19, rely=0.03, anchor=CENTER)


root.mainloop()