from student import Student

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
            print("student added successfully")
        else:
            print(f"Student with ID {student_id} already exists.")   

    def mark_attendance(self, student_id):
        if student_id in self.students:
            self.students[student_id].mark_attendance()
            print("Attendance marked successfully")
        else:
            print("Student not found.")
       
        def add_class_day(self):
            for student in self.students.values():
                student.add_class_day()

    def generate_report(self):
        for student in self.students.values():
            sid, name, att, total = student.get_details()
            percentage = student.calculate_percentage()
            status = "Allowed to take exam" if student.is_allowed_exam() else "Not allowed to take exam"
            print(f"{sid} - {name}: {percentage:.2f}% attendance - {status}")