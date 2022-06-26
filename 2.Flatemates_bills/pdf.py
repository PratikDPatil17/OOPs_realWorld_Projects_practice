from fpdf import FPDF
import os
import webbrowser

class PDFreport:
    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style="B")
        
        # add image
        #pdf.image("name.png", w=30, h=30)

        # set font
        #pdf.set_font(family="Times", size = 18, style="B")

        # add  text 
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln = 1)
        pdf.cell(w=100, h=40, txt="Period:", border=1, align="C")
        pdf.cell(w=150, h=40, txt=bill.bill_date, border=1, ln = 1)

        # add details
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.calculate_pays(bill, flatmate2)), border=1, ln = 1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate2.calculate_pays(bill, flatmate1)), border=1 , ln = 1)

        os.chdir("files")
        pdf.output(self.filename)

        # open pdf after exectuion directly
        webbrowser.open(self.filename)
