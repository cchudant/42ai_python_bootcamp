import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import tkinter
matplotlib.use('TkAgg')

class ImageProcessor():
    def load(path):
        img = mpimg.imread(path)
        print('Loading array of dimensions {} x {}'.format(*img.shape))
        return img / 255

    def display(img):
        plt.imshow(img)
        plt.show()
