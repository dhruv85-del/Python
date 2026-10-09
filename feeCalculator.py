student_name = input("Enter student name: ")
course_fee = float(input("Enter course fee: "))
registration_fee = float(input("Enter registration fee: "))

total_amount = course_fee + registration_fee

print(f"Course Fee      : ₹{course_fee:.0f}")
print(f"Registration Fee: ₹{registration_fee:.0f}")
print("-------------------------")
print(f"Total Payable   : ₹{total_amount:.0f}")
