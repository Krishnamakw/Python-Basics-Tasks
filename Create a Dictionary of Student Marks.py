# Task 9: Create a Dictionary of Student Marks

# Step 1: Create the dictionary
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 75
}

# Step 2: Ask user to input a student’s name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the record.")
