from student import Student
from attendance import Attendance

#Create attendance manager
attendance = Attendance()

#Create students
student1 = Student("Nancy", "001")
student2 = Student("Gide", "002")

#Mark attendance
attendance.mark_attendance(student1, "Present")
attendance.mark_attendance(student2, "Absent")

#Show records
attendance.show_attendance()