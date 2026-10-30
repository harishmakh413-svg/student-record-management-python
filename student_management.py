def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    try:
        mark = int(input("Enter student mark: "))

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100")
            return

        with open("students.txt", "a") as file:
            file.write(name + " - " + str(mark) + "\n")

        print("Student record saved successfully!")

    except ValueError:
        print("Please enter a valid whole number")
def display_students():
    try:
        with open("students.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("No student records found!")
def search_student():
    name = input("Enter student name: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(" - ")
                student_name = data[0]

                if student_name.lower() == name.lower():
                    print(line.strip())
                    found = True

        if not found:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")
def delete_student():
    name = input("Enter student name to delete: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                data = line.strip().split(" - ")
                student_name = data[0]

                if student_name.lower() == name.lower():
                    found = True
                else:
                    file.write(line)

        if found:
            print("Student record deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")
def update_student():
    name = input("Enter student name to update: ").strip()

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            data = line.strip().split(" - ")
            student_name = data[0]

            if student_name.lower() == name.lower():
                try:
                    new_mark = int(input("Enter new mark: "))

                    if not 0 <= new_mark <= 100:
                        print("Mark must be between 0 and 100")
                        return

                except ValueError:
                    print("Please enter a valid whole number")
                    return

                lines[i] = student_name + " - " + str(new_mark) + "\n"

                with open("students.txt", "w") as file:
                    file.writelines(lines)

                print("Student mark updated successfully!")
                return

        print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")    
while True:
    print("\n--- Student Record Management ---")
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Exit")
    choice = input("Enter the choice: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        display_students()
    elif choice=="3":
       search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        update_student()
    elif choice=="6":
         break
    else:
        print("invalid choice")