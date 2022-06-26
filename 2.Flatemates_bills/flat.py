class Bill:
    def __init__(self, amount:float, period:str):
        self.bill_amount = amount
        self.bill_date = period


# class TotalDays:
#     def __init__(self,o1,o2) -> None:
#         self.o1 = o1
#         self.o2 = o2
#         #self.total_days = self.o1.days_in_house + self.o2.days_in_house
#     def return_days(self):
#         total_days = self.o1.days_in_house + self.o2.days_in_house
#         return total_days

class Flatmates:
    def __init__(self, name:str, days:int):
        self.name = name
        self.days_in_house = days
    def calculate_pays(self, bill:Bill, flatmate2):
        total_days = self.days_in_house + flatmate2.days_in_house
        ans = bill.bill_amount*(self.days_in_house / total_days)
        return round(ans, 2)