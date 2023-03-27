from student import cursor, sqliteConnection


class Mark:
    def get_all_subjects(self):
        return cursor.execute("select * from subject").fetchall()

    def getAllClasses(self):
        return cursor.execute("select * from class").fetchall()
marks = Mark()
