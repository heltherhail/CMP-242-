class Student:
    def __init__(self, name,student_id):
        self.name = name
        self.student_id = student_id 

    def display_info(self):
        return f"{self.student_id} - {self.name}"
       