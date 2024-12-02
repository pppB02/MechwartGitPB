import random

def get_random_num(a: int,b: int):
    try:
        print(random.randint(a,b))
        print("A -B:",a - b)
    except:
        print("Elbasztad teso!")

numA = int(input("A szam:"))
numB = int(input("B szam:"))

get_random_num(numA,numB)	
