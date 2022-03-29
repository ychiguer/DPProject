import PIL
from matplotlib import image
import os

classes = ["TAT", "MOL", "PIG"];

for c in classes:
    file = 1
    for pic in os.listdir(".//"+c):
        img = PIL.Image.open(".//"+c + "//" + pic)
        img = img.resize((600,600))
        img.save(".//"+c + "//" + str(file) +".png")
        if (pic != str(file) +".png" ):
            os.remove(".//"+c + "//" + pic)
        file += 1
