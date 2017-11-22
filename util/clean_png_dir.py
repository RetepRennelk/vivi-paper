import os
import sys

png_dir = sys.argv[1]
pngs = sys.argv[2:]

for file in os.listdir(png_dir):
    if file not in pngs:
        os.remove(os.path.join(png_dir, file))