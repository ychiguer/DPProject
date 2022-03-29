from matplotlib import image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
import os

classes = ["TAT", "MOL", "PIG"];

data = {
    "x" : [],
    "y" : []
}

for c in classes:
    for pic in os.listdir(".//"+c):
        img = image.imread(".//"+c + "//" + pic)
        data["x"] += [img]
        data["y"] += [c]

x_train, x_test, y_train, y_test = train_test_split(data["x"], data["y"], test_size=0.1, random_state=1)
        
