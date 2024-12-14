class Course:
    def __init__(self, course_id, name, year, section):
        self.course_id = course_id
        self.name = name
        self.year = year
        self.section = section
        self.enrolled_students = []

    def enroll_student(self, student_name):
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
            print(f"Student {student_name} has been enrolled in {self.name}.")
        else:
            print(f"Student {student_name} is already enrolled in {self.name}.")

    def display_students(self):
        if self.enrolled_students:
            print(f"Students enrolled in {self.name}:")
            for student in self.enrolled_students:
                print(student)
        else:
            print(f"No students enrolled in {self.name}.")

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Year: {self.year}, Section: {self.section}"

class CourseEnrollmentSystem:
    def __init__(self):
        self.courses = []

    def add_course(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        year = int(input("Enter year level: "))
        section = input("Enter section (e.g., A, B, C): ")
        course = Course(course_id, name, year, section)
        self.courses.append(course)
        print(f"Course {name} has been added.")

    def enroll_student_in_course(self):
        course_id = input("Enter course ID to enroll in: ")
        student_name = input("Enter student name: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            course.enroll_student(student_name)
        else:
            print("Course not found.")

    def display_all_courses(self):
        if self.courses:
            print("All courses:")
            for course in self.courses:
                print(course)
        else:
            print("No courses available.")

    def display_students_in_course(self):
        course_id = input("Enter course ID to display enrolled students: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            course.display_students()
        else:
            print("Course not found.")

def main():
    system = CourseEnrollmentSystem()

    while True:
        print("\nCourse Enrollment System")
        print("1. Add a new course")
        print("2. Enroll a student in a course")
        print("3. Display all courses")
        print("4. Display students in a specific course")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            system.add_course()
        elif choice == '2':
            system.enroll_student_in_course()
        elif choice == '3':
            system.display_all_courses()
        elif choice == '4':
            system.display_students_in_course()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
