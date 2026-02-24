class Student:
    def __init__(self, name,student_id):
        self.name = name
        self.student_id = student_id 
        self.__attendance_count = 0
        self.__total_classes = 0

    def mark_attendance(self, status):
        self.__total_classes += 1
        if status == 'present':
            self.__attendance_count += 1 

    def add_class_day(self):
        self.__total_classes += 1

    def calculate_attendance_percentage(self):
        if self.__total_classes == 0:
            return 0
        return (self.__attendance_count / self.__total_classes) * 100

    def is_allowed_exam(self):
        return (self.calculate_attendance_percentage() >=70)          

    def display_info(self):
        return f"{self.student_id} - {self.name}: {self.calculate_attendance_percentage():.2f}% attendance" and "Allowed to take exam" if self.is_allowed_exam() else "Not allowed to take exam"
       