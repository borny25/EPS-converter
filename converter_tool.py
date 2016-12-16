import os, sys, glob
import PIL.Image
from tkinter import *
from tkinter.filedialog import askdirectory
from shutil import copyfile


def browsefolder():
	fldr = askdirectory()
	imgpath.set(fldr)
	
	files = glob.glob("*.eps")
	print(files)
	
	entry1.delete(0, END)
	entry1.insert(0, fldr)



def batchconvert():
	imgpath = entry1.get()
	print(imgpath)
	os.chdir(imgpath)
	newpath = imgpath + "\\jpegs\\"
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	

	files = glob.glob("*.eps")								#identify all eps files in working directory
	print(files)

	jpegs = glob.glob("*.jpg")
	print(jpegs)

	for f in files:
		try:
			print(f)
			filename, extension = os.path.splitext(f)				#split filenames and extension
			print(filename)
			infile = PIL.Image.open(filename + ".eps")		
			infile.load(scale=8)							#open and load at double scale (important for quality)
			outfile = newpath + filename + ".jpg"					#define outfile as a jpg of infile in the 'jpegs' folder
			infile.save(outfile, quality = 95)					#attempt to convert and save into newpath, dpi set to same size as original, quality maxed at 95
		except IOError:
			print("Unable to convert")

	for j in jpegs:										#define new path to copy jpegs into the 'jpegs' folder, that way, everything is in the same place
		try:
			print(j)
			jpegpathold = os.path.abspath(j)
			jpegpathnew = os.path.abspath(newpath) + "\\" + j			#use os.abspath here otherwise end up with / rather than \ in pathnames. Using abspath is platform-agnostic.
			print(jpegpathold)
			print(jpegpathnew)
			copyfile(jpegpathold, jpegpathnew)
		except:
			print("Unable to move existing jpegs")

root = Tk()
root.title("EPS Image Converter")
root.minsize(20, 10)

imgpath=StringVar()

thelabel = Label(root, text = "This idenitifies the working directory")
thelabel.grid(row=0, columnspan=2, sticky=W)

button1=Button(root, text="Browse", fg="black", command=browsefolder)
button2=Button(root, text="Cancel", fg="black", command=root.destroy)
button3=Button(root, text="Convert", fg="black", command=batchconvert)

entry1=Entry(root, textvariable=imgpath)

button1.grid(row=1, column=1)
entry1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=2, column=1)

root.mainloop()
