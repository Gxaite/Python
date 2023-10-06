print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))

percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
percentage/=100

split = int(input("How many people to split the bill? "))

result = round(total_bill/split*(1+percentage),2)
print(f"Each person should pay ${result}")
