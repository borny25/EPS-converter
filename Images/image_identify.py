
import os, sys, glob
from PIL import Image

directory = "C:\\Users\\adam.born\\Desktop"
print(os.getcwd())

files = glob.glob("*.eps")
print(files)


for f in files:
	filename, extension = os.path.splitext(f)
	infile = Image.open(filename + ".eps")
	print(filename, infile.format, infile.size, infile.mode)

os.chdir(directory)
print(os.getcwd())
files = glob.glob("*.eps")
print(files)
