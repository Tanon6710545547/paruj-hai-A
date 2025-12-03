
class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self._name = name
        self.__major = major
        self.credits = 0

    def get_info(self):
        return f"ID: {self.student_id}, Name: {self._name}, Major: {self.__major}, Credits: {self.credits}"

student_id = input("Enter student ID: ")
name = input("Enter name: ")
major = input("Enter major:")
stu = Student(student_id,name,major)
print(stu.get_info())