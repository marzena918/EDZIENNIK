from student import cursor, sqliteConnection


class Degre:
    def findDegreForStudentWithSubject2(self, name, last_name, subject):
        cursor.execute(
            f"select mark from marks where subject = '{subject}' and student = (select id from student where name ='{name}' and last_name ='{last_name}')").fetchall()

    def findDegreForStudentWithSubject(self, subject, student_id):
        return cursor.execute(
            f"select mark, id,notes from marks where subject = '{subject}' and student = {student_id}").fetchall()

    def add_degre(self, student_id, mark, notes, subject):
        cursor.execute(
            f"insert into marks(subject, mark, student, notes) values ('{subject}','{mark}', {student_id},'{notes}')")
        sqliteConnection.commit()


    def grades_id(self, student_id,mark, notes, subject):
        return cursor.execute(
            f"select id from marks where subject = '{subject}' and notes ='{notes}' and mark ='{mark}' and student ={student_id}").fetchall()

    def remove_degre(self, degre_id: int):
        cursor.execute(f"DELETE from marks where id ={degre_id}")
        sqliteConnection.commit()

    def get_all_degre(self,student_id):
        return cursor.execute(f"select * from marks where student = {student_id}").fetchall()

degre = Degre()
