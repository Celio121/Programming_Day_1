exammark = int(input("Input result(1-100): "))
if exammark < 0 or exammark > 100:
    print("Error: marks must be between 1 and 100")
elif exammark < 50:
    print("Fail")
elif exammark >= 71:
    print("Distinction")
elif exammark >= 61:
    print("Merit")
elif exammark >= 50:
    print("Pass")