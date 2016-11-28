import os, sys
from PIL import Image

filename = "test"
infile = Image.open(filename + ".eps")
outfile = filename + ".jpg"
infile.save(outfile)

