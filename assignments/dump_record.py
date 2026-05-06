import pickle

def dump_records(filename):
    records = []
    
    n = int(input("Enter number of records: "))
    
    for i in range(n):
        print(f"\nRecord {i+1}")
        name = input("Enter name: ")
        student_id = int(input("Enter student ID: "))
        
        record = {"name": name, "student_id": student_id}
        records.append(record)

