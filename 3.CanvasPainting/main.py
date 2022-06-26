from abc import ABC, abstractmethod
from PIL import Image
import numpy as np

class Shapes(ABC):
    def __init__(self,x,y,shape,color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
    
    @abstractmethod
    def draw(self, canvas):
        pass

class Square(Shapes):
    def __init__(self, x, y, shape, color, width):
        super().__init__(x, y, shape, color)
        self.width = width

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.width, self.y:self.y + self.width] = self.color

class Rectangle(Shapes):
    def __init__(self, x, y, shape, color, width, height):
        super().__init__(x, y, shape, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color



class Canvas:
    def __init__(self, a, b, color) -> None:
        self.a = a
        self.b = b
        self.color = color

        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        self.data[:] = self.color
    
    def make(self, imagepath):
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)
        

    


canvas = Canvas(500, 500, (255, 255, 255))
rect = Rectangle(1,6,"rectangle", (100,200,125), 20,17)
rect.draw(canvas)

sq = Square(10,50,"square", (0,100,222), 70)
sq.draw(canvas)


rect = Rectangle(40, 70, "rectangle",(35,76,45), 70, 60)
rect.draw(canvas)
canvas.make("canvas.png")


# build CLI 

# print()
# print("Welcome to Canvas Painting")

# print("Step 1 = Build your canvas")
# h = int(input("Enter Canvas Height = "))
# w = int(input("Enter Canvas Width = "))
# c = input("Canvas Color - Black/white")

# if c.lower() == "white":
#     col = (255, 255, 255)
# elif c.lower() == "black":
#     col = (0,0,0)
# else:
#     print("Wrong out put - You are out")

# canvas = Canvas(h,w,col)

# print()
# print("Lets add shapes to canvas now")

# ans = True
# cnt = 0
# sq = "sq"
# while ans:
#     cnt += 1
#     obj = "sq"+str(cnt)
#     shape = input("Add shape (square/rectangle/exit):")
#     if shape.lower() == "square":
#         obj = "sq"+str(cnt)
#         x = int(input("WHat is the x co-ordinate? : "))
#         y = int(input("What is the y co-ordinate? : "))
#         c = tuple(input("Color in tuple format :"))
#         width = int(input("Enter Square side : "))

#         obj = Square(x,y,shape,c,width)
#         obj.draw(canvas)

#     elif shape.lower() == "rectangle":
#         obj = "rect"+str(cnt)
#         x = int(input("WHat is the x co-ordinate? : "))
#         y = int(input("What is the y co-ordinate? : "))
#         c = tuple(input("Color in tuple format :"))
#         width = int(input("Enter rectangle width : "))
#         height = int(input("Enter rectangle height : "))

#         obj = Rectangle(x,y,shape,c,width, height)
#         obj.draw(canvas)

#     elif shape.lower() == "done":
#         ans = False


# canvas.make("canvas.png")






