# Student Grading System

name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculate total
total = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate average
average = total / 5

# Calculate grade
if average < 50:
    grade = "F"
elif average >= 50 and average < 60:
    grade = "D"
elif average >= 60 and average < 70:
    grade = "C"
elif average >= 70 and average < 80:
    grade = "B"
elif average >= 80 and average < 90:
    grade = "A"
else:
    grade = "A+"

# Display result
print("\n--- Student Grade Report ---")
print("Student Name:", name)
print("Student ID:", student_id)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)






# Student Grading System for 4 Students

students = []

for i in range(4):
    print("\nEnter details for Student", i + 1)

    name = input("Student Name: ")
    student_id = input("Student ID: ")

    marks = []
    for j in range(5):
        mark = float(input(f"Enter marks for Subject {j + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average < 50:
        grade = "F"
    elif average < 60:
        grade = "D"
    elif average < 70:
        grade = "C"
    elif average < 80:
        grade = "B"
    elif average < 90:
        grade = "A"
    else:
        grade = "A+"

    students.append([name, student_id, marks, total, average, grade])


# Display all students
print("\n========== STUDENT GRADING REPORT ==========")

for student in students:
    print("\nStudent Name:", student[0])
    print("Student ID:", student[1])
    print("Marks:", student[2])
    print("Total:", student[3])
    print("Average:", student[4])
    print("Grade:", student[5])
    
    
    