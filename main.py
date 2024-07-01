import json
from Students import Student, NoMatchingNameError
from Teachers import Teacher, NoMatchingNameError
class NotMatchingEmail(Exception):
    pass
class NoMatchingIdError(Exception):
    pass

class AuthenticationError(Exception):
    pass

def read_data_from_json(file_path, cls):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return [cls(**item) for item in data]
    except FileNotFoundError:
        return []

def save_data(data, file_path):
    data_list = [vars(item) for item in data]
    with open(file_path, 'w') as file:
        json.dump(data_list, file, indent=4)

def main():
    students_file_path = 'students.json'
    teachers_file_path = 'teachers.json'
    students = read_data_from_json(students_file_path, Student)
    teachers = read_data_from_json(teachers_file_path, Teacher)

    user_type = input("Are you a teacher or a student? ").lower()

    if user_type == 'teacher':
        name = input("Enter your name: ")
        id = int(input("Enter your ID number: "))
        authenticate= False
        for teacher in teachers:
            if teacher.name == name and teacher.id == id:
                authenticate = True
                break
        if not authenticate:
            raise AuthenticationError("Invalid teacher name or ID.")

    while True:
        print("\nManagement System")
        print("1. Display all students")
        print("2. Display all teachers")
        if user_type == 'teacher':
            print("3. Add a new student")
            print("4. Add a new teacher")
            print("5. Update a student's address")
            print("6. Update a teacher's address")
            print("7. Update a student's marks")
            print("8. Delete a student")
            print("9. Delete a teacher")
        print("10. Search a student")
        print("11. Search a teacher")
        if user_type == 'teacher':
            print("12. Calculate percentage and rank for students")
        print("13. Save and exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                Student.display_all(students)
            elif choice == '2':
                Teacher.display_all(teachers)
            elif choice == '3':
                student = Student.accept()
                for existing_student in students:
                    if existing_student.name == student.name:
                        raise ValueError("Name must be unique.")
                students.append(student)
            elif user_type == 'teacher' and choice == '4':
                teacher = Teacher.accept(teachers)
                for existing_teacher in teachers:
                    if existing_teacher.id == teacher.id:
                        raise ValueError("ID must be unique.")
                    if existing_teacher.email == teacher.email:
                        raise NotMatchingEmail("Email is replicated")
                teachers.append(teacher)
            elif user_type == 'teacher' and choice == '5':
                name = input("Enter the name of the student to update address: ")
                new_address = input("Enter new address: ")
                for student in students:
                    if student.name == name:
                        student.address = new_address
                        break
                else:
                    raise NoMatchingNameError("No student found with the given name.")
            elif user_type == 'teacher' and choice == '6':
                name = input("Enter the name of the teacher to update address: ")
                new_address = input("Enter new address: ")
                for teacher in teachers:
                    if teacher.name == name:
                        teacher.address = new_address
                        break
                else:
                    raise NoMatchingNameError("No teacher found with the given name.")
            elif user_type == 'teacher' and choice == '7':
                name = input("Enter the name of the student to update marks: ")
                course = input("Enter the course: ")
                new_mark = int(input("Enter new mark: "))
                for student in students:
                    if student.name == name:
                        if course in student.courses:
                            index = student.courses.index(course)
                            student.marks[index] = new_mark
                        else:
                            raise ValueError("Course not found.")
                        break
                else:
                    raise NoMatchingNameError("No student found with the given name.")
            elif user_type == 'teacher' and choice == '8':
                name = input("Enter the name of the student to delete: ")
                Student.delete(students, name)
            elif user_type == 'teacher' and choice == '9':
                name = input("Enter the name of the teacher to delete: ")
                Teacher.delete(teachers, name)
            elif choice == '10':
                name = input("Enter the name of the student to search: ")
                Student.search(students, name)
            elif choice == '11':
                name = input("Enter the name of the teacher to search: ")
                Teacher.search(teachers, name)
            elif user_type == 'teacher' and choice == '12':
                Student.rank_calculation(students)
            elif choice == '13':
                save_data(students, students_file_path)
                save_data(teachers, teachers_file_path)
                print("Data saved successfully. Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()