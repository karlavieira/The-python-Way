print("Welcome to tip calculator.")
bill = int(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip wold you like to give? 10, 12, or 15? "))
total = int((bill / people) * (1 +(tip / 100)))
total_pago = total * people
print(f"Each person should pay: ${total}")
print(f"O total pago foi: ${total_pago}")