class Attendance:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, student, status):
        self.records[student.student_id] = {
            'name': student.name,
            'status': status
        }

    def show_attendance(self):
        for student_id, info in self.records.items():
            print(f"{student_id} - {info['name']}: {info['status']}")