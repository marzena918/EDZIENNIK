import sqlite3

sqliteConnection = sqlite3.connect('identifier.sqlite', check_same_thread=False)
# todo: set foreign_keys	true

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


sqliteConnection.row_factory = dict_factory
cursor = sqliteConnection.cursor()


class Classs:
    def get_all(self):
        return cursor.execute("select class.name as name_class,class.id, teacher.name, teacher.last_name from class join teacher on class.tutor = teacher.id").fetchall()


    def get_all_teacher(self):
        return cursor.execute("select name, last_name, id from teacher").fetchall()

    def add_class(self, name, tutor, students):
        cursor.execute(f"insert into class (name, tutor) VALUES ('{name}', '{tutor}')")
        for i in students:
            cursor.execute(f"insert into class_student (class_id, student_id) VALUES ((select id from class where name = '{name}'), {i})")
        sqliteConnection.commit()

    def update(self, name, tutor, class_id, students):
        try:
            # start transaction
            cursor.execute(f"update class set name ='{name}', tutor= {tutor} where id = {class_id}")
            cursor.execute(f"delete from class_student where class_id={class_id}")
            for i in students:
                cursor.execute(f"insert into class_student(class_id, student_id) VALUES ({class_id}, {i})")
            sqliteConnection.commit()
        except Exception as e:
            sqliteConnection.rollback()
            raise e

    def list_of_students(self):
        return cursor.execute(f"select name, last_name, id from student").fetchall()


    def students_without_class(self):
        return cursor.execute(f"select name, last_name,id from student "
                              f"where id not in (select student_id from class_student)").fetchall()

    def list_of_student_for_class(self, id):
        return cursor.execute(f"select name, last_name,id from student "
                              f"where id in (select student_id from class_student where class_id = {id})").fetchall()




classs = Classs()
