import pytest
from main import Shapes, Square, Rectangle


class TestClass:
    def test_objects(self):
        
        a = Shapes(3,5,"square", "red")
        d = Shapes(6,9,"Rectangle", "Blue")
        b = Square(a.x,a.y, a.shape, a.color, 40)
        c = Rectangle(d.x, d.y, d.shape, d.color, 45, 70)