from asyncore import loop


num1 = int(input("Select your First number: "))
num2 = int(input("Select your Second number: "))


print("1. Add     + ")
print("2. Subtract - ")
print("3. Multiply * ")
print("4. Divide   / ")
print("5. Square   s ")
symbol = input("Please select one of the following operations by selecting the symbol: ")


if symbol == "+":
    value = num1 + num2
    print(value)
elif symbol == "-":
    value = num1 - num2
    print(value)
elif symbol == "*":
    value = num1 * num2
    print(value)
elif symbol == "/":
    value = num1 / num2
    print(value)
elif symbol == "s":
    print("Number 1 Squared: " + str(num1**2))
    print("Number 2 Squared: " + str(num2**2))
    