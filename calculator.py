num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operator = input("Enter operator(+,-,*,/)")

if operator == '+':
    result = num1 + num2 
    print(f"Result of {num1} + {num2} is {result}.")
elif operator == '-':
    result = num1 - num2
    print(f"Result of {num1} - {num2} is {result}.")
elif operator == '*':
     result = num1*num2
     print(f"Result of {num1} * {num2} is {result}.")
elif operator == '/':
    if num2 !=0:
        result = num1/num2
        print(f"Result of {num1} / {num2} is {result}.")
else:
    print("Error! Cannot be Divided by Zero.")
         