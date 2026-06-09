#Your Name 
#CIS261
#WK10 VIBE Coding

#Your Name 
#CIS261
#WK10 VIBE Coding- Student Grade Calculator

import os

FILE_NAME = "student_grades.txt"


class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.student_id = student_id
        self.test1 = float(test1)
        self.test2 = float(test2)
        self.test3 = float(test3)
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return (self.test1 + self.test2 + self.test3) / 3

    def calculate_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def to_file_string(self):
        return (
            f"{self.name}|{self.student_id}|"
            f"{self.test1}|{self.test2}|{self.test3}|"
            f"{self.average:.2f}|{self.grade}"
        )


def load_students():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) >= 7:
                    student = Student(
                        parts[0],
                        parts[1],
                        float(parts[2]),
                        float(parts[3]),
                        float(parts[4])
                    )
                    students.append(student)

    except Exception as e:
        print(f"Error loading file: {e}")

    return students


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            for student in students:
                file.write(student.to_file_string() + "\n")

        print("\nRecords saved successfully.")

    except Exception as e:
        print(f"Error saving file: {e}")


def add_student(students):
    try:
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        test1 = float(input("Enter Test 1 score: "))
        test2 = float(input("Enter Test 2 score: "))
        test3 = float(input("Enter Test 3 score: "))

        student = Student(name, student_id, test1, test2, test3)
        students.append(student)

        print("Student added successfully.\n")

    except ValueError:
        print("Invalid score entered. Please enter numeric values.\n")


def display_students(students):
    if not students:
        print("No student records found.\n")
        return

    print("\n{:<20} {:<10} {:>8} {:>8} {:>8} {:>10} {:>8}".format(
        "Name", "ID", "Test1", "Test2", "Test3", "Average", "Grade"
    ))

    print("-" * 80)

    for student in students:
        print("{:<20} {:<10} {:>8.2f} {:>8.2f} {:>8.2f} {:>10.2f} {:>8}".format(
            student.name,
            student.student_id,
            student.test1,
            student.test2,
            student.test3,
            student.average,
            student.grade
        ))

    print()


def search_student(students):
    search_name = input("Enter student name to search: ").lower()

    found = False

    for student in students:
        if search_name in student.name.lower():
            print("\nStudent Found:")
            print(f"Name: {student.name}")
            print(f"ID: {student.student_id}")
            print(f"Average: {student.average:.2f}")
            print(f"Grade: {student.grade}\n")
            found = True

    if not found:
        print("Student not found.\n")


def class_statistics(students):
    if not students:
        print("No student records available.\n")
        return

    averages = [student.average for student in students]

    highest = max(averages)
    lowest = min(averages)
    class_avg = sum(averages) / len(averages)

    print("\nClass Statistics")
    print("-" * 20)
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average:  {lowest:.2f}")
    print(f"Class Average:   {class_avg:.2f}\n")


def main():
    students = load_students()

    while True:
        print("===== Student Grade Calculator =====")
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student By Name")
        print("4. View Class Statistics")
        print("5. Save and Exit")
        print("ESC. Exit and Save")

        choice = input("\nEnter choice: ").strip().upper()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            class_statistics(students)

        elif choice == "5":
            save_students(students)
            print("Goodbye!")
            break

        elif choice == "ESC":
            save_students(students)
            print("Program exited and data saved.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()