import random

ans = True

def song_rec(num):
  if num == 1:
    print("Up - Kep1er") 
  if num == 2:
    print("Black Mamba - Aespa") 
  if num == 3:
    print("Stereotype - StayC")
  if num == 4:
    print("Kill This Love - BLACKPINK")
  if num == 5:
    print("Dance the Night Away - Twice") 
  if num == 6:
    print("We Go - fromis_9")
  if num == 7:
    print("Love Dive - Ive")


while True:
    q = input("want to continue y/n")
    num = random.randint(1,7)
    if q == "y":
        song_rec(num)
    elif q == "n":
        break
        