from student import cursor, sqliteConnection

class Parents:
    def get_all_parent(self):
        return cursor.execute("select * from parents").fetchall()

parents = Parents()