def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "FAIL"

def add_student():
    name = input("Enter student name: ")
    math = float(input("Enter Math marks (out of 100): "))
    science = float(input("Enter Science marks (out of 100): "))
    english = float(input("Enter English marks (out of 100): "))
    computer = float(input("Enter Computer marks (out of 100): "))
    
    total = math + science + english + computer
    percentage = total / 4
    grade = calculate_grade(percentage)
    
    with open("students.txt", "a") as f:
        f.write(f"{name},{math},{science},{english},{computer},{percentage:.2f},{grade}\n")
    
    print(f"\nStudent Added Successfully!")
    print(f"Name: {name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def view_students():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No students found!")
                return
            print("\n--- ALL STUDENTS ---")
            for line in lines:
                data = line.strip().split(",")
                print(f"Name: {data[0]} | Percentage: {data[5]}% | Grade: {data[6]}")
    except FileNotFoundError:
        print("No students found!")

def search_student():
    name = input("Enter student name to search: ").lower()
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            found = False
            for line in lines:
                data = line.strip().split(",")
                if data[0].lower() == name:
                    print(f"\n--- STUDENT FOUND ---")
                    print(f"Name: {data[0]}")
                    print(f"Math: {data[1]} | Science: {data[2]}")
                    print(f"English: {data[3]} | Computer: {data[4]}")
                    print(f"Percentage: {data[5]}%")
                    print(f"Grade: {data[6]}")
                    found = True
            if not found:
                print("Student not found!")
    except FileNotFoundError:
        print("No records found!")

def delete_student():
    name = input("Enter student name to delete: ").lower()
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
        with open("students.txt", "w") as f:
            deleted = False
            for line in lines:
                data = line.strip().split(",")
                if data[0].lower() != name:
                    f.write(line)
                else:
                    deleted = True
            if deleted:
                print("Student deleted successfully!")
            else:
                print("Student not found!")
    except FileNotFoundError:
        print("No records found!")
def class_report():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No students found!")
                return
            
            total_students = len(lines)
            total_percentage = 0
            highest = 0
            highest_name = ""
            passed = 0
            failed = 0
            
            for line in lines:
                data = line.strip().split(",")
                percentage = float(data[5])
                total_percentage += percentage
                
                if percentage > highest:
                    highest = percentage
                    highest_name = data[0]
                
                if data[6] == "FAIL":
                    failed += 1
                else:
                    passed += 1
            
            class_average = total_percentage / total_students
            
            print("\n===== CLASS REPORT =====")
            print(f"Total Students: {total_students}")
            print(f"Class Average: {class_average:.2f}%")
            print(f"Top Student: {highest_name} ({highest:.2f}%)")
            print(f"Passed: {passed} | Failed: {failed}")
            
    except FileNotFoundError:
        print("No records found!")

def menu():
    while True:
        print("\n=== STUDENT RESULT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            class_report()
        elif choice == "6":
            print("goodbye")
            break
        else:
            print("Invalid choice!")

menu()
