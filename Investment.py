initial = int(input("Initial Investment: "))
target = int(input("Target Value: "))
interest = int(input("Interest Rate: "))

interest_inc = int((initial) * (interest / 100))
peryear = int(initial + interest_inc)
for years in range (peryear, target, interest_inc):
    print(f"Amount of money per year: {years}") 
    if years == 100:
        break
