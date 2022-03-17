def getPath():
	from tkinter import filedialog, Tk
	root = Tk()
	root.withdraw()
	folder_selected = filedialog.askdirectory(title="aoiclient.txt Open Commands Directory")
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

from tkinter import *
import os


win = Tk()
win.geometry("800x600")
win.title("aoiclient.txt by Ethy")
win.resizable(False, False)

font = ("Sans Serif Pro", "16")

mainFrame = Frame(win, height=100, width=800)
mainFrame.pack(side="top")

title = Label(mainFrame, text="aoiclient.txt by Ethy", font=font)
title.pack(side="left")

file = None
filename = ""

nameFrame = Frame(win, height=100, width=600)
nameFrame.pack(side="top")

nameLBL = Label(nameFrame, text="Name:", font=font)
nameLBL.pack(side="top")

nameText = Text(nameFrame, height=1, font=font)
nameText.pack(side="bottom")

codeFrame = Frame(win, height=100, width=600)
codeFrame.pack(side="top")

codeLBL = Label(codeFrame, text="Code:", font=font)
codeLBL.pack(side="top")

codeText = Text(codeFrame, height=10, font=font)
codeText.pack(side="bottom")

btnFrame = Frame(win, height=100, width=600)
btnFrame.pack()

def clearValues():
	global codeText, nameText, file
	file = None
	if nameText.get(1.0, END) != "":
		nameText.delete(1.0, END)
	if codeText.get(1.0, END) != "":
		codeText.delete(1.0, END)

def openThis():
	global codeText, nameText, file, path, win
	from tkinter import filedialog, Tk
	win.withdraw()
	check = filedialog.askopenfilename(title="aoiclient.txt Open Text Command").split("/")
	check = check[len(check)-1]
	if (not os.path.exists(os.path.join(path, check))):
		return
	win.deiconify()
	lines = check
	if nameText.get(1.0, END) != "":
		nameText.delete(1.0, END)
	nameText.insert(END, file.split(".")[0])
	if file:
		file.close()
	file = open(os.path.join(path, file))
	if codeText.get(1.0, END) != "":
		codeText.delete(1.0, END)
	codeText.insert(END, "\n".join(file.readlines()))
	
def saveThis():
	global codeText, nameText, path, file, filename
	if filename != nameText.get(1.0, END):
		os.rename(os.path.join(path, filename))
	line = str.encode(codeText.get(1.0, END))
	tru = open(filepath, "w+")
	tru.truncate(0)
	tru.close()
	fd = os.open(filepath, os.O_RDWR)
	numBytes = os.write(fd, line)
	os.close(fd)
	if file and nameText.get(1.0, END) != file:
		os.rename(filepath, path+nameText.get(1.0,END)+".txt")
	file = nameText.get(1.0,END)
	clearValues()

saveButton = Button(btnFrame, text="Save", command=saveThis)
saveButton.pack(side="left")
openButton = Button(btnFrame, text="Open", command=openThis)
openButton.pack(side="left")

win.mainloop()
# open, save, delete, new