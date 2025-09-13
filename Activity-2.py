import math
variablex1 = float(input("Enter the value of x1: "))
variabley1 = float(input("Enter the value of y1: "))
variablex2 = float(input("Enter the value of x2: "))
variabley2 = float(input("Enter the value of y2: "))

distance = math.sqrt(pow(variablex2 - variablex1, 2) + pow(variabley2 - variabley1, 2))

print("The distance between the two points is:", round(distance, 2))