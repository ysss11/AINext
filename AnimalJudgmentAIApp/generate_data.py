import glob
import numpy as np
from PIL import Image
from sklearn import model_selection
from const import CLASSES, IMAGE_SIZE


X = []
Y = []

for index, classlabel in enumerate(CLASSES):
    photos_dir = "./animal_images/" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./imagefiles.npy", xy)
