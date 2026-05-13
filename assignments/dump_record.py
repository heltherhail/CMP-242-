import pickle

def dump_records(filename):

    with open(filename, "wb") as file:

        n = int(input("How many records? "))

        for i in range(n):

            print(f"\nRecord {i+1}")

            name = input("Enter name: ")
            student_id = int(input("Enter student ID: "))

            record = {
                "name": name,
                "student_id": student_id}

            records = []
            records.append(record)

            pickle.dump(record, file)

    print("Records saved successfully!")

dump_records("students.dat")