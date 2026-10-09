num1 : int # First number
num2 : int # Second number
operator : str # Operator

num1 = int(input("Enter first number: ")) # Input first number
operator = input("Enter operator: ") # Input operator
num2 = int(input("Enter second number: ")) # Input second number

print("\n")
if operator == "/" and num2 == 0:
    print("Error: Division by zero is not allowed.")
    exit()
    
if operator == "+":
    print("Result: ", num1 + num2)
elif operator == "-":
    print("Result: ", num1 - num2)
elif operator == "*":
    print("Result: ", num1 * num2)
elif operator == "/":
    print("Result: ", f"{num1 / num2:.4f}")
else:
    print("Invalid operator!")