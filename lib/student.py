from user import User


class Student(User):

    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade
    
    def log_in(self):
        super().log_in()
        self.in_class = True



oneil = Student("O'neil", 10)
# Student.__init__ called.
# User.__init__ called.
oneil.__dict__
# {'name': "O'neil", 'grade': 10}