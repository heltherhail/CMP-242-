import pickle

def load_records(filename):

    try:
        with open(filename, "rb") as file:

            while True:

                try:
                    record = pickle.load(file)

                    print(record)

                except EOFError:
                    break

    except FileNotFoundError:
        print("File not found")


load_records("students.dat")