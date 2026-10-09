name: str # Student name
age: int # Student age
email: str # Student email
course_name: str # Course name
course_fee: float # Course fee


name = input("Enter student name: ")
age = int(input("Enter student age: "))
email = input("Enter student email: ")
course_name = input("Enter course name: ")
course_fee = float(input("Enter course fee: "))

print("============== STUDENT PROFILE ==============")
print("Student Name     :", name)
print("Age              :", age)
print("Email            :", email)
print("Course           :", course_name)
print("Course Fee       :", course_fee)
print("=============================================")

