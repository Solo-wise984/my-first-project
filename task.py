# Student Grade Management System

# Dictionary to store student names and grades
students = {}

# Function to add students and their grades
def add_student():
    name = input("Enter the student's name: ").capitalize()
    try:
        grade = float(input(f"Enter the grade for {name}: "))
        students[name] = grade
        print(f"Student {name} with grade {grade} added successfully! 🎉\n")
    except ValueError:
        print("Invalid grade. Please enter a number. ❌\n")

# Function to display statistics
def display_statistics():
    if not students:
        print("No student data available. Please add students first. 🤷‍♂️\n")
        return

    average = sum(students.values()) / len(students)
    highest = max(students, key=students.get)
    lowest = min(students, key=students.get)

    print("\n--- Grade Statistics ---")
    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest} ({students[highest]})")
    print(f"Lowest Grade: {lowest} ({students[lowest]})\n")

# Function to search for a student's grade
def search_student():
    name = input("Enter the student's name to search: ").capitalize()
    grade = students.get(name)
    if grade is not None:
        print(f"{name} has a grade of {grade}. 🎓\n")
    else:
        print(f"Student {name} not found. ❌\n")

# Function to update a student's grade
def update_grade():
    name = input("Enter the student's name to update: ").capitalize()
    if name in students:
        try:
            new_grade = float(input(f"Enter the new grade for {name}: "))
            students[name] = new_grade
            print(f"Updated {name}'s grade to {new_grade}. ✅\n")
        except ValueError:
            print("Invalid grade. Please enter a number. ❌\n")
    else:
        print(f"Student {name} not found. ❌\n")

# Main menu
def menu():
    while True:
        print("--- Student Grade Management System ---")
        print("1. Add a Student")
        print("2. Display Statistics")
        print("3. Search for a Student")
        print("4. Update a Grade")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_statistics()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_grade()
        elif choice == "5":
            print("Exiting the system. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again. ❌\n")

# Run the program
menu()
