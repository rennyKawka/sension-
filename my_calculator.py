
num1 = int(input("Enter First number: "))
op = input("Enter operator: ")
num2 = int(input("Enter Second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid operator!!!")
