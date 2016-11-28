import os, sys, glob
from PIL import Image

#imgpath = "C:\\Users\\adam.born\\Desktop\\Python stuff\\Images" 						#set path variable
#os.chdir(path)																		#set current working directory to 'path' variable as defined above		
#print(os.getcwd())

imgpath = "U:\\Subbing\\Brennecke 20162\\ED"

os.chdir(imgpath)	

newpath = imgpath + "\\jpegs\\"
if not os.path.exists(newpath):
	os.makedirs(newpath)

files = glob.glob("*.eps")															#identify all eps files in working directory
print(files)

for f in files:
	try:
		print(f)
		filename, extension = os.path.splitext(f)									#split filenames and extension
		print(filename)
		infile = Image.open(filename + ".eps")		
		infile.load(scale=2)														#open and load at double scale (important for quality)
		outfile = newpath + filename + ".jpg"										#define outfile as a jpg of infile in the jpegs folder
		infile.save(outfile, dpi=infile.size, quality = 95)							#attempt to convert and save into newpath, dpi set to same size as original, quality maxed at 95
	except IOError:
		print("Unable to convert")