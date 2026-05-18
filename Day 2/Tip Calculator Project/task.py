print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) #Total da conta
tip = int(input("What percentage tip would you like to give? 10% 12% 15% ")) #Gorjeta por cima do total
people = int(input("How many people to split the bill? ")) #Dividir o TotalG

percent_tip = round((bill * tip)/100)
Total = round(bill + percent_tip)
Total_Geral = Total/people
print(f"Each person should pay : ${Total_Geral}")