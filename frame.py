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
        self.print()

        pyplot.imshow(self.gray_matrix, cmap="grey")
        pyplot.show()


    def to_gray_scale(self):
        r, g, b = self.image_matrix[:,:,0], self.image_matrix[:,:,1], self.image_matrix[:,:,2]
        gray = r*0.299 + g*0.587 + b*0.114
        return gray
    
    def resize(self):
        self.size_tuple = (self.width, self.height)
        if self.height > 600:
            factor = 600/self.height
            self.height = int(self.height*factor)
            self.width = int(self.width*factor)
            self.size_tuple = (self.width, self.height)
        
        self.image = self.image.resize(self.size_tuple)

    def matrix_to_ascii(self):
        self.ascii_matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for row in range(len(self.gray_matrix)):
            for element in range(len(self.gray_matrix[row])):
                if self.gray_matrix[row][element] == 255.0:
                    self.ascii_matrix[row][element] = " "
                if self.gray_matrix[row][element] == 0.0:
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
    
    def print(self):
        for row in self.ascii_matrix:
            print(" ".join(map(str,row)))

                    
    
   





        



    

    

