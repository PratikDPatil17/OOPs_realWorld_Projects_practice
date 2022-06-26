from flat import Bill, Flatmates
from pdf import PDFreport



# Build Command line interface -> CLI
print()
print("Welcome to Flatmates bill app!! ")
print()

bill = float(input("Enter a bill amount ="))
bill_date = input("Enter date (format - Month Year - Dec 2022) =")
bill_month = Bill(bill, bill_date)

print()
print("Flatmates Details")
print()
print("Enter Flatmate 1 Details")
name = input("Enter name = ")
days = int(input("Enter number of days spend in house = "))
f1 = Flatmates(name, days)

print()
print("Enter Flatmate 2 Details")
name = input("Enter name = ")
days = int(input("Enter number of days spend in house = "))
f2 = Flatmates(name, days)

print()
# Individual bills
f1_pays = f1.calculate_pays(bill_month, f2)
print("Amount need to be Paid by ",f1.name," is = ",f1_pays)

f2_pays = f2.calculate_pays(bill_month, f1)
print("Amount need to be Paid by ",f2.name," is = ",f2_pays)

print()
# Want to generate pdf?
p = input("Want to generate pdf? y/n = ")
if p.lower() == "y":
    filename = input("Enter Filename :")
    pdf = PDFreport(filename)
    pdf.generate(f1, f2, bill_month)
else:
    print("Thank you!!!!")





