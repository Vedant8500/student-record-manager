class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open("students.txt", "a") as f:
        f.write(f"{roll_no},{name},{marks}\n")
    print("Student added successfully!\n")

def view_students():
    print("\nStudent Records:")
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll_no, name, marks = line.strip().split(",")
                s = Student(roll_no, name, marks)
                s.display()
    except FileNotFoundError:
        print("No records found!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
