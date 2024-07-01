import re

class NoMatchingNameError(Exception):
    pass

class Teacher:
    def __init__(self, name, id, email, phone_number, subject, address):
        self.name = name
        self.id = id
        self.email = email
        self.phone_number = phone_number
        self.subject = subject
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Subject: {self.subject}")
        print(f"Address: {self.address}")

    def accept(teachers):
        name = input("Enter name: ")
        id = int(input("Enter ID: "))
        email = input("Enter email: ")
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email) and email in teachers:
            email = input("Invalid email. Enter email again: ")
        phone_number = int(input("Enter phone number: "))
        while len(str(phone_number)) != 10 and phone_number in teachers:
            phone_number = int(input("Invalid phone number. Enter 10 digit phone number: "))
        subject = input("Enter subject: ")
        address = input("Enter address: ")
        return Teacher(name, id, email, phone_number, subject, address)

    def display_all(teachers):
        for teacher in teachers:
            teacher.display()
            print()

    
    def search(teachers, name):
        for teacher in teachers:
            if teacher.name == name:
                teacher.display()
                return
        raise NoMatchingNameError("No teacher found with the given name.")


def delete(teachers, name):
        for teacher in teachers:
            if teacher.name == name:
                teachers.remove(teacher)
                return
        raise NoMatchingNameError("No teacher found with the given name.")