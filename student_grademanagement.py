students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

def show_results():
    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"
        print(name, "Marks:", marks, "Grade:", grade)

while True:
    print("1.Add Student 2.Show Results 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_results()
    else:
        break