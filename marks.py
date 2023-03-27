from student import cursor, sqliteConnection


class Mark:
    def get_all_subjects(self):
        return cursor.execute("select * from subject").fetchall()

    def getAllClasses(self):
        return cursor.execute("select * from class").fetchall()

    def listStudentOfClass(self, id):
        return cursor.execute(f"select student.* from student join class_student cs on student.id = cs.student_id where cs.class_id = {id}").fetchall()
marks = Mark()
