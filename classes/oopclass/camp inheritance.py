
# inheritance - using common codes in a separate class -called code reusability

# we inherit -data members or var,member functions(methods),constructor
# private members are not inherited

class User:

    def login(self):
        print('login')

    def register(self):
        print('reg')

class Student(User):
    def enroll(self):
        print('enroll')

    def review(self):
        print('revw')

class Teacher(User):
    def course(self):
        print('subject')
    def account(self):
        print('transactions')

stu1 = Student()
stu1.enroll()
stu1.login()
stu1.register()
stu1.review()











