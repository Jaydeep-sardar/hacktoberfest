import json
import os

class Student:
    def __init__(self, student_id: int, name: str, marks: float):
        self.id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {"id": self.id, "name": self.name, "marks": self.marks}

    @staticmethod
    def from_dict(data):
        return Student(data["id"], data["name"], data["marks"])

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_from_file()

    def add_student(self, student_id, name, marks):
        student = Student(student_id, name, marks)
        self.students.append(student)
        print("Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No students to display.")
            return
        print("\nID\tName\t\tMarks")
        print("-----------------------------")
        for s in self.students:
            print(f"{s.id}\t{s.name}\t{s.marks:.2f}")

    def delete_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                print("Student deleted.")
                return
        print("Student not found.")

    def update_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                s.name = input("Enter new name: ")
                s.marks = float(input("Enter new marks: "))
                print("Student updated.")
                return
        print("Student not found.")

    def search_student(self, name):
        found = False
        for s in self.students:
            if name.lower() in s.name.lower():
                print(f"Found -> ID: {s.id}, Name: {s.name}, Marks: {s.marks:.2f}")
                found = True
        if not found:
            print(f"No student found with name containing '{name}'")

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.students], f)
        print("Data saved to file.")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Student.from_dict(d) for d in data]

def main():
    sms = StudentManagementSystem()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            sms.add_student(student_id, name, marks)
        elif choice == "2":
            sms.display_students()
        elif choice == "3":
            student_id = int(input("Enter ID to delete: "))
            sms.delete_student(student_id)
        elif choice == "4":
            student_id = int(input("Enter ID to update: "))
            sms.update_student(student_id)
        elif choice == "5":
            name = input("Enter Name to search: ")
            sms.search_student(name)
        elif choice == "6":
            sms.save_to_file()
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
