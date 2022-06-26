from tkinter import Canvas
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle (self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

#class FindDist:
    def distance_from_points(self, point):
        return ((self.x - point.x) ** 2 + (self.y-point.y)**2 )**0.5


class GUIPoint(Point):
    def draw_point(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.dot(size = 10, color = "red")


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

class GUIRectangle(Rectangle):
    def __init__(self, lowleft, upright):
        super().__init__(lowleft, upright)
    
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)

        #canvas.pendown()
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)

        #turtle.done()



myturtle = turtle.Turtle()


point1 = Point(20,30)
point2 = Point(60,90)

rectangle = Rectangle(point1, point2)

pointx = Point(5,5)
a = pointx.falls_in_rectangle(rectangle)

area = rectangle.area()

gui = GUIRectangle(point1, point2)
guiPoint = GUIPoint(25,76)


gui.draw(myturtle)
guiPoint.draw_point(myturtle)

#a = point2.distance_from_points(point1)
print(a)
print(area)