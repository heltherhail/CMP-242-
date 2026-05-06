import pickle

def load_records(filename):
    try:
        with open(filename, "rb") as file:
            records = pickle.load(file)

        print("\nStored Records:")
        for record in records:
            print(f"Name: {record['name']}, Student ID: {record['student_id']}")

    except FileNotFoundError:
        print("File not found.")
    
    except Exception as e:
        print("Error:", e)
