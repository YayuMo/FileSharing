import matplotlib.pyplot as plt
from PIL import Image
import os

if __name__ == '__main__':

    imagefiles = os.listdir('image')
    i = 1
    for img in range(0,len(imagefiles),3):
        print(img)
        file = os.path.join('image',imagefiles[img])
        image = Image.open(file)
        plt.subplot(4,4,i)
        i += 1
        plt.imshow(image)
    plt.show()