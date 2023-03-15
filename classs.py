import sqlite3

sqliteConnection = sqlite3.connect('identifier.sqlite', check_same_thread=False)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


sqliteConnection.row_factory = dict_factory
cursor = sqliteConnection.cursor()


class Classs:
    def get_all(self):
        return cursor.execute("select * from class").fetchall()

    def get_all_teacher(self):
        return cursor.execute("select name, last_name from teacher").fetchall()

    def add_class(self, name, tutor, students):
        cursor.execute(f"insert into class (name, tutor) VALUES ('{name}', '{tutor}')")
        for i in students:
            cursor.execute(f"insert into class_student (class_id, student_id) VALUES ((select id from class where name = '{name}'), {i})")
        sqliteConnection.commit()

    def update(self, name, tutor, id):
        cursor.execute(f"update class set name ='{name}', tutor= '{tutor}' where id = {id}")
        sqliteConnection.commit()

    def list_of_students(self):
        return cursor.execute(f"select name, last_name, id from student").fetchall()
        # do zmian - nie umiem

    def students_without_class(self):
        return cursor.execute(f"select name, last_name,id from student "
                              f"where id not in (select student_id from class_student)").fetchall()
    #zle


classs = Classs()
