num1 : int # First number
num2 : int # Second number

num1 = int(input("Enter first number: ")) # Input first number
num2 = int(input("Enter second number: ")) # Input second number

print("\n")

print("Addition       :", num1 + num2)  
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", f"{num1 / num2:.4f}")
print("Floor Division :", num1 // num2)
print("Modulus        :", num1 % num2)
print("Exponentiation :", num1 ** num2)