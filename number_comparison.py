num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is lesser than {num2}")
else:
    print(f"Both {num1} and {num2} are Equal!")