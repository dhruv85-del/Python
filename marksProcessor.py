name : str
python : int
database : int
programming : int

name = input("Enter your name: ") # Input name
python = int(input("Enter your Python marks: ")) # Input Python marks   
database = int(input("Enter your Database marks: ")) # Input Database marks
programming = int(input("Enter your Programming marks: ")) # Input Programming marks

total_marks = python + database + programming # Calculate total marks
average_marks = total_marks / 3 # Calculate average marks

print("======= MARKS REPORT =======")
print(f"Student Name: {name}")
print(f"Python      : {python}")
print(f"Database    : {database}")
print(f"Programming : {programming}\n")
print(f"Total Marks : {total_marks}")
print(f"Average     : {average_marks:.2f}")
print("============================")