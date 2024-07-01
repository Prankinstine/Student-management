class NoMatchingNameError(Exception):
    pass

class Student:
    def __init__(self, name, age, address, courses, marks):
        self.name = name
        self.age = age
        self.address = address
        self.courses = courses
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print("Courses and Marks:")
        for course, mark in zip(self.courses, self.marks):
            print(f"  {course}: {mark}")

    def accept():
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        courses = []
        marks = []
        print("Enter courses and marks (type 'done' to finish):")
        while True:
            course = input("Course: ")
            if course.lower() == 'done':
                break
            mark = int(input("Mark: "))
            courses.append(course)
            marks.append(mark)
        return Student(name, age, address, courses, marks)

    def display_all(students):
        for student in students:
            student.display()
            print()

    def search(students, name):
        for student in students:
            if student.name == name:
                student.display()
                return
        raise NoMatchingNameError("No student found with the given name.")

    def delete(students, name):
        for student in students:
            if student.name == name:
                students.remove(student)
                return
        raise NoMatchingNameError("No student found with the given name.")

    def pass_fail_determination(self):
        return all(mark >= 40 for mark in self.marks)

    def highest_and_lowest_scores(self):
        return max(self.marks), min(self.marks)

    def percentage(self):
       if self.pass_fail_determination():
            return sum(self.marks) / len(self.marks)
       else:
           return 0
        
    def rank_calculation(students):
        percentages = [(student.name, student.percentage(),student.pass_fail_determination()) for student in students]
        percentages.sort(key=lambda x: x[1], reverse=True)
        for rank, (name, percentage,pf) in enumerate(percentages, 1):
            if pf:
                passfail ="Pass"
                print(f"Rank {rank}: {name} with {percentage:.2f}%....which is {passfail}")
            else:
                passfail = "Fail"
                print(f"Rank NaN: {name} with {percentage:.2f}%....which is {passfail}")
        print(Student.highest_and_lowest_scores)
