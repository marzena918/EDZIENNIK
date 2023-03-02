from student import cursor

class Teacher:
    def get_all(self):
        return cursor.execute("select * from subject").fetchall()

teachers = Teacher()