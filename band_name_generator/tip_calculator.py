print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")

bill1 = float(bill)
tip1 = int(tip)
people_split1 = int(people_split)

tip2 = tip1 * bill1 / 100
bill2 = tip2 + bill1
people_split2 =  bill2 / people_split1
people_split3 = round(people_split2,2)
print(f"Each person should pay: {people_split3}$")