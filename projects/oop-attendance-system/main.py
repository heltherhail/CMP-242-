from logging import root

from attendance_system import AttendanceSystem
from qr_manager import QRManager

system = AttendanceSystem()
qr = QRManager()

while True:
    print("\n1. Add Student")
    print("2. Generate QR Code for Attendance")
    print("3. Mark Attendance")
    print("4. Add Class Day")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        system.add_student(student_id, name)
        
    elif choice == '2':
        student_id = input("Enter student ID: ")
        qr.generate_qr_code(student_id)
        
    elif choice == '3':
        sid = input("Scan QR code or enter student ID: ")
        system.mark_attendance(sid)
        
    elif choice == '4':
        system.add_class_day()
        print("New class day added successfully.")

    elif choice == '5':
        system.generate_report()
        
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.") 

import tkinter as tk
from attendance_system import AttendanceSystem

system = AttendanceSystem()

def add_Student():
        sid = entry_id.get()
        name = entry_name.get()
        system.add_student(sid, name)

root = tk.Tk()
root.title("Attendance System")

tk.Label(root, text="Student ID:").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Button(root, text="Add Student", command=add_student).pack()
root.mainloop()
   