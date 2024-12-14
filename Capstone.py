class Student:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = [grade1, grade2, grade3, grade4]

    def update_grades(self, grade1=None, grade2=None, grade3=None, grade4=None):
        if grade1 is not None:
            self.grades[0] = grade1
        if grade2 is not None:
            self.grades[1] = grade2
        if grade3 is not None:
            self.grades[2] = grade3
        if grade4 is not None:
            self.grades[3] = grade4

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_student(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Grades: {self.grades}, Average Grade: {self.average_grade():.2f}")


class StudentGradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, course, grade1, grade2, grade3, grade4):
        student = Student(student_id, name, course, grade1, grade2, grade3, grade4)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def update_student_grades(self, student_id, grade1=None, grade2=None, grade3=None, grade4=None):
        student = self.find_student_by_id(student_id)
        if student:
            student.update_grades(grade1, grade2, grade3, grade4)
            print(f"Grades updated for {student.name}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display_student()

    def calculate_class_average(self):
        if not self.students:
            print("No students in the system to calculate the average.")
        else:
            total_average = sum(student.average_grade() for student in self.students)
            class_average = total_average / len(self.students)
            print(f"Class Average Grade: {class_average:.2f}")


def main():
    manager = StudentGradeManager()

    while True:
        print("\nStudent Grade Management System")
        print("1. Add New Student")
        print("2. Update Student Grades")
        print("3. View All Students")
        print("4. Calculate Class Average")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course = input("Enter Course : ")
            grade1 = float(input("Enter Math Grade: "))
            grade2 = float(input("Enter Science Grade: "))
            grade3 = float(input("Enter English Grade: "))
            grade4 = float(input("Enter Filipino Grade : "))
            manager.add_student(student_id, name, course, grade1, grade2, grade3, grade4)
        
        elif choice == "2":
            student_id = input("Enter Student ID to update: ")
            print("Enter grades to update (leave blank for no change):")
            grade1 = input("Math: ")
            grade2 = input("Science: ")
            grade3 = input("English: ")
            grade4 = input("Filipino: ")
            
            grade1 = float(grade1) if grade1 else None
            grade2 = float(grade2) if grade2 else None
            grade3 = float(grade3) if grade3 else None
            grade4 = float(grade4) if grade4 else None

            manager.update_student_grades(student_id, grade1, grade2, grade3, grade4)
        
        elif choice == "3":
            manager.display_all_students()
        
        elif choice == "4":
            manager.calculate_class_average()
        
        elif choice == "5":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
