import os, sys
from PIL import Image

infile = "2016-06-07717B-Extended_Data_Figure_1.eps"
f, e = os.path.splitext(infile)
print(f)
outfile = f + ".png"
print(infile, outfile)
if infile != outfile:
	try:
		Image.open(infile).save(outfile)
	except IOError:
		print("cannot convert", infile)
