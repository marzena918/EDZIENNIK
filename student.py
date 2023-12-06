import sqlite3

sqliteConnection = sqlite3.connect('identifier.sqlite', check_same_thread=False)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


sqliteConnection.row_factory = dict_factory
cursor = sqliteConnection.cursor()


class Student:

    def dodaj(self, name, surname, pesel, id_parents):
        cursor.execute(f"insert into student(name, last_name, pesel,parent_id) "
                       f"VALUES ('{name}','{surname}',{pesel}, {id_parents})")
        sqliteConnection.commit()

    def usun(self, id):
        cursor.execute(f"DELETE from student where id = '{id}'")
        sqliteConnection.commit()

    def update(self, id,name, surname, pesel):
        cursor.execute(
            f"UPDATE student set name = '{name}',last_name ='{surname}', pesel = '{pesel}' where id = '{id}'")
        sqliteConnection.commit()

    def get_all(self):
        return cursor.execute("select * from student").fetchall()

    def is_pesel_exist(self, pesel) -> bool:
        return bool(cursor.execute(f"select pesel from student where pesel = '{pesel}'").fetchall())

    # def add_grades(self):
    #     cursor.execute("insert into oceny(religia, angielski, polski, matematyka, id) VALUES (5,5,5,5,33)")
    #     sqliteConnection.commit()
    #
    # def get_all_grades(self,id):
    #     return cursor.execute(f"select * from oceny where id='{id}'").fetchall()

    def student_data(self,id):
        return cursor.execute(f"select name, last_name from student where id = '{id}'").fetchall()

student = Student()
