def getPath():
	from tkinter import filedialog, Tk
	root = Tk()
	root.withdraw()
	folder_selected = filedialog.askdirectory()
	return folder_selected

def getFiles(path):
	from os import walk
	filenames = next(walk(path), (None, None, []))[2]
	return filenames or []

print("Launching folder dialog...")
path = getPath()
print("Got " + path)
print("Fetching Files...")
files = getFiles(path)
print("Fetched")
file = None
from tkinter import *
import os

win = Tk()
win.geometry("800x400")
win.title("aoiclient.txt by Ethy")
win.resizable(False, False)
win.grid_rowconfigure(2, minsize=400)

mainFont = ("Sans Serif Pro", "20")
secondFont = ("Sans Serif Pro", "15")

listPanel = Frame(win, width=800, height=100)
listPanel.configure(background="#222222")
listPanel.grid(row=0)

editPanel = Frame(win, width=800, height=400)
editPanel.configure(background="#333333")
editPanel.grid(row=1)
editPanel.grid_rowconfigure(4, minsize=100)

title = Label(listPanel, text="aoiclient.txt", font=mainFont)
title.configure(background="#222222",foreground="#ffffff")
title.pack(side="left")

var_file = StringVar()
var_file.set("Select an Option")

nameLabel = None
nameText = None
codeLabel = None
codeText = None

def fileCallback(var, index, mode):
	global editPanel, var_file, file, nameText, codeText, nameLabel, codeLabel
	if file and not file.closed:
		file.close()
	file = open(os.path.join(path,var_file.get()))

	if nameText.get(1.0, END) != "":
		nameText.delete(1.0, END)
	nameText.insert(END, var_file.get().split(".")[0])
	if codeText.get(1.0, END) != "":
		codeText.delete(1.0, END)
	codeText.insert(END, "\n".join(file.readlines()))


var_file.trace_add('write', fileCallback)

filemenu = OptionMenu(listPanel, var_file, *files)
filemenu.configure(background="#222222",foreground="#ffffff")
filemenu.pack()

nameText = Text(editPanel, font=secondFont)
nameText.configure(background="#333333",foreground="#ffffff")
nameText.grid()
nameLabel = Label(editPanel, text="Name:", font=secondFont)
nameLabel.configure(background="#333333",foreground="#ffffff")
nameLabel.grid()

codeLabel = Label(editPanel, text="Code:", font=secondFont)
codeLabel.configure(background="#333333",foreground="#ffffff")
codeLabel.grid()
codeText = Text(editPanel, font=secondFont)
codeText.configure(background="#333333",foreground="#ffffff")
codeText.grid()

win.mainloop()
#new command button, save command button, close command button