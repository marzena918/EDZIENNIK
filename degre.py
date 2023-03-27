from student import cursor, sqliteConnection

class Degre:
    def findDegreForStudentWithSubject(self,name,last_name,subject):
        cursor.execute(f"select mark from marks where subject = '{subject}' and student = (select id from student where name ='{name}' and last_name ='{last_name}')").fetchall()

    def add_degre(self,student_id,mark,notes, subject):
        cursor.execute(f"insert into marks(subject, mark, student, notes) values ('{subject}','{mark}', {student_id},'{notes}')")
        sqliteConnection.commit()

degre = Degre()