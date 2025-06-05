# Student Result Calculator
print("Please input student information mentioned order. " \
"Name, Phone, 1st Term result, 2nd term result, 3rd term result")

student_list = []

while len(student_list) < 5:
    student_info = input(f"Enter information for student {len(student_list) + 1}: ").split(", ")
    if len(student_info) != 5:
        print("Invalid input. Please enter exactly 5 values.")
        continue
    
    name, phone, term1, term2, term3 = student_info
    try:
        term1 = float(term1)
        term2 = float(term2)
        term3 = float(term3)
    except ValueError:
        print("Invalid term results. Please enter numeric values.")
        continue
    
    average = (term1 + term2 + term3) / 3
    student_list.append({
        "Name": name,
        "Phone": phone,
        "Term 1": term1,
        "Term 2": term2,
        "Term 3": term3,
        "Average": average
    })

student_list.sort(
    key=lambda student: student["Average"],
    reverse=True
)

# Displaying the results
print("\nStudent Results:")
for student in student_list:
    print(f"Name: {student['Name']}")
    print(f"Phone: {student['Phone']}")
    print(f"Term 1: {student['Term 1']}")
    print(f"Term 2: {student['Term 2']}")
    print(f"Term 3: {student['Term 3']}")
    print(f"Average: {student['Average']:.2f}\n")