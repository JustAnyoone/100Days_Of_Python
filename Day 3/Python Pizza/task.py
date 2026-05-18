import sys

print("Welcome to Python Pizza Deliveries!")
Pizza_Total_Value = 0
size = input("What size pizza do you want? S, M or L: ").upper()

if size == "S":
    Pizza_Total_Value += 15
elif size == "M":
    Pizza_Total_Value += 20
elif size == "L":
    Pizza_Total_Value += 25
else:
    print("Invalid pizza size")
    sys.exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if  pepperoni == "Y":
    if size == "S":
        Pizza_Total_Value += 2
    else:
            Pizza_Total_Value += 3
else:
    print("ok")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    Pizza_Total_Value += 1
else:
    print("ok")

print(f"Your final bill is: ${Pizza_Total_Value}.")



