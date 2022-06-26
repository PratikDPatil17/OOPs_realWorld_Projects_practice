import pytest
#from fpdf import FPDF
#import webbrowser
from flat import Flatmates, Bill 
#from pdf import PDFreport

f1 = Flatmates("Pratik", 30)
f2 = Flatmates("Virat", 30)
b = Bill(6000, "Dec 2022")
#c = PDFreport
class TestApp:
    def test_objects(self):
        pass
        #a = Flatmates()
        #b = Bill(1200)

    def test_bill_payment(self):
        res = f1.calculate_pays(b, f2)
        print("Result _------", res)
        assert  res == 3000

    #def test_generate_pdf(self):
    #   res = c.generate(f1,f2,b)
