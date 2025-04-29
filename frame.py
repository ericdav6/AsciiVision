from PIL import Image
import numpy
from matplotlib import pyplot

class Frame():
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        
        self.size_of_image = self.image.size
        self.width = self.size_of_image[0]
        self.height = self.size_of_image[1]

        self.image_matrix = numpy.array(self.image)
        self.gray_matrix = self.to_gray_scale()

        pyplot.imshow(self.gray_matrix, cmap="grey")
        pyplot.show()

        

    def to_gray_scale(self):
        r, g, b = self.image_matrix[:,:,0], self.image_matrix[:,:,1], self.image_matrix[:,:,2]
        gray = r*0.299 + g*0.587 + b*0.114
        return gray







        



    

    

