from student import cursor, sqliteConnection


class Teacher:
    def get_all(self):
        return cursor.execute("select * from subject").fetchall()

    def is_pesel_exist(self, pesel):
        return bool(cursor.execute(f"select pesel from teacher where pesel = '{pesel}'").fetchall())

    def add_teacher(self, name, last_name, pesel, sub):
        cursor.execute(
            f"insert into teacher (name,last_name,pesel) VALUES('{name}', '{last_name}', '{pesel}')")
        teacher_id = cursor.lastrowid

        for i in sub:
            cursor.execute(f"insert into teacher_subject(teacher_id, subject) VALUES ({teacher_id}, '{i}')")
        sqliteConnection.commit()

    def get_all_teacher(self):
        return cursor.execute("select * from teacher").fetchall()

    def subjects_of_teacher(self, id):
        return cursor.execute(f"select subject from teacher_subject where teacher_id = {id}").fetchall()
        # res2 = result[:]
        # if not result:
        #     return ''
        # else:
        #     print(res2)
        #     return res2
    def delete_subject_for_teacher(self, id,subject):
        cursor.execute(f"DELETE from teacher_subject where teacher_id = '{id}' and subject = '{subject}'")
        sqliteConnection.commit()
teachers = Teacher()
