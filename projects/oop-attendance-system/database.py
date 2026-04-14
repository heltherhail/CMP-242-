import sqlite3

class Database:
    def _init_(self):
        self.conn = sqlite3.connect("attendance.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT,
            attendance INTEGER,
            total_classes INTEGER
        )
        """)
        self.conn.commit()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                            (student.id, student.name, 0, 0))
        self.conn.commit()

    def update_student(self, student):
        self.cursor.execute("""
        UPDATE students
        SET attendance=?, total_classes=?
        WHERE id=?
        """, (student.attendance, student.total_classes, student.id))
        self.conn.commit()

    def get_all_students(self):
        return self.cursor.execute("SELECT * FROM students").fetchall()