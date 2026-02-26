class Counter:
    count = 100
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)

class CMP242:
    language = "This is English"
    def __init__(self, name):
        self.name = name
    def type(self):
        return "Please "+ self.name +" This is English"

Sudanez = CMP242("sud")
Emirkaya = CMP242("emir")

print(Sudanez.type())
print(Emirkaya.type())


class Student:
    school_name = "Near East University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

Student.change_school("Kyrenia University")
print(Student.school_name)