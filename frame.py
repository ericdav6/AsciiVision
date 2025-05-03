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
        self.aspect_ratio = self.width/self.height
        self.resize()



        self.image_matrix = numpy.array(self.image)
        self.gray_matrix = self.to_gray_scale()

        self.matrix_to_ascii()

        pyplot.imshow(self.gray_matrix, cmap="grey")
        pyplot.show()





    def to_gray_scale(self):
        r, g, b = self.image_matrix[:,:,0], self.image_matrix[:,:,1], self.image_matrix[:,:,2]
        gray = r*0.299 + g*0.587 + b*0.114
        return gray
    
    def resize(self):
        self.new_size = (50*int(self.aspect_ratio),50)
        self.image = self.image.resize(self.new_size)

    def matrix_to_ascii(self):
        self.ascii_matrix = [[0 for _ in range(self.new_size[1])] for _ in range(self.new_size[1])]
        for row in range(len(self.gray_matrix)):
            for element in range(len(self.gray_matrix[row])):
                if self.gray_matrix[row][element] == 255.0:
                    self.ascii_matrix[row][element] = " "
                if self.gray_matrix[row][element] == 0.0 or self.gray_matrix[row][element] == 0:
                    self.ascii_matrix[row][element] = "@"
                else:
                    if self.gray_matrix[row][element] < 255.0 and self.gray_matrix[row][element] > 225.0:
                        self.ascii_matrix[row][element] = "."
                    if self.gray_matrix[row][element] < 225.0 and self.gray_matrix[row][element] > 195.0:
                        self.ascii_matrix[row][element] = ":"
                    if self.gray_matrix[row][element] < 195.0 and self.gray_matrix[row][element] > 165.0:
                        self.ascii_matrix[row][element] = "-"
                    if self.gray_matrix[row][element] < 165.0 and self.gray_matrix[row][element] > 135.0:
                        self.ascii_matrix[row][element] = "="
                    if self.gray_matrix[row][element] < 105.0 and self.gray_matrix[row][element] > 75.0:
                        self.ascii_matrix[row][element] = "+"
                    if self.gray_matrix[row][element] < 75.0 and self.gray_matrix[row][element] > 45.0:
                        self.ascii_matrix[row][element] = "*"
                    if self.gray_matrix[row][element] < 45.0 and self.gray_matrix[row][element] > 15.0:
                        self.ascii_matrix[row][element] = "#"
                    if self.gray_matrix[row][element] < 15.0 and self.gray_matrix[row][element] > 0.0:
                        self.ascii_matrix[row][element] = "%"
    
                    
    
   








        



    

    

