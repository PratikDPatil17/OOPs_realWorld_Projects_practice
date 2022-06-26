from typing import List
class Game_inputs:
    def __init__(self):
        self.x1 = int(input("Enter x1 : "))
        self.x2 = int(input("Enter x2 : "))
        self.y1 = int(input("Enter y1 : "))
        self.y2 = int(input("Enter y2 : "))
        self.c1 = int(input("Enter c1 : "))
        self.c2 = int(input("Enter c2 : "))

    
class Game_process():
    def  __init__(self, obj:Game_inputs):
        self.obj = obj

     
    def check_co_ordinate(self):
        if self.obj.c1 > self.obj.x1  and self.obj.c2 < self.obj.x2 :
            if self.obj.c2 > self.obj.y1  and self.obj.c2 < self.obj.y2:
                return True

        return False

class Ans():
    def __init__(self, obj:Game_process):
        self.obj = obj
    def ans(self):
        if self.obj.check_co_ordinate():
            print("Inside Rectangle")
        else:
            print("Outside rectangle")

gi = Game_inputs()

gp = Game_process(gi)
# ans = gp.check_co_ordinate()

an = Ans(gp)
an.ans()