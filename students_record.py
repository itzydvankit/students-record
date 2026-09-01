import os

HEADER = "ROLL|NAME|MARKS|CLASS\n"
LINE = "-" * 30 + "\n"


def choose_level():
    while True:
        level = input("Enter student level (UG /PG): ").strip().upper()
        if level in ("UG", "PG"):
            return level.lower() + ".txt"
        print("Invalid input. Enter UG or PG.")


def initialize_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write(HEADER)
            f.write(LINE)


def roll_exists(file_name, roll):
    if not os.path.exists(file_name):
        return False

    with open(file_name, "r") as f:
        for line in f.readlines()[2:]:
            if line.startswith(str(roll) + "|"):
                return True
    return False


def add_student(file_name):
    initialize_file(file_name)

    while True:

        try:
            roll = int(input("Enter Roll Number: "))
        except ValueError:
            print("Invalid Roll Number!")
            continue

        if roll_exists(file_name, roll):
            print("Student data already available")
        else:
            name = input("Enter Name: ").strip().upper()
            marks = input("Enter Marks: ").strip()
            student_class = input("Enter Class: ").strip().upper()

            with open(file_name, "a") as f:
                f.write(f"{roll}|{name}|{marks}|{student_class}\n")

            print("Student added successfully.")

        print("\n1. Add Another Student")
        print("0. Exit to Main Menu")

        choice = input("Enter choice: ").strip()
        if choice == "0":
            break


def view_students(file_name):
    if not os.path.exists(file_name):
        print("No records found.")
        return

    with open(file_name, "r") as f:
        print("\n" + f.read())


def search_student(file_name):
    if not os.path.exists(file_name):
        print("File not found.")
        return

    search_roll = input("Enter Roll Number to Search: ").strip()

    with open(file_name, "r") as f:
        for line in f.readlines()[2:]:
            if line.startswith(search_roll + "|"):
                print("\nStudent Found\n")
                print(HEADER.strip())
                print(LINE.strip())
                print(line.strip())
                return

    print("Student not found.")


def delete_student(file_name):
    if not os.path.exists(file_name):
        print("File not found.")
        return

    delete_roll = input("Enter Roll Number to Delete: ").strip()

    with open(file_name, "r") as f:
        lines = f.readlines()

    updated = []
    deleted = False

    for line in lines:
        if line.startswith(delete_roll + "|"):
            deleted = True
        else:
            updated.append(line)

    with open(file_name, "w") as f:
        f.writelines(updated)

    if deleted:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    file_name = choose_level()
    initialize_file(file_name)

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Change UG/PG")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(file_name)
        elif choice == "2":
            view_students(file_name)
        elif choice == "3":
            search_student(file_name)
        elif choice == "4":
            delete_student(file_name)
        elif choice == "5":
            file_name = choose_level()
            initialize_file(file_name)
        elif choice == "6":
            print("Program exited successfully.")
            print("Thank You !")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()