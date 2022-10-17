number = 1
while number < 100:
    square = number ** 2
    number += 1
    if square >= 2000:
        break
    print(f"{number} ^2 = {square}")