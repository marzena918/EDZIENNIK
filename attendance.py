import datetime

from student import cursor, sqliteConnection
class Attendance:
    def get_sub_hour(self,day,classes):
        res = []
        is_full= cursor.execute(f"select hour_id, subject from lesson_plan where day='{day}' and "
                                f"classes_id = {classes}").fetchall()
        for i in is_full:
            if i['subject'] != '0':
                res.append(i)
        return res

    def get_all_hour(self):
        di = {}
        res = cursor.execute(f" select id, from_hour, until_hours from configurations_hours").fetchall()
        for i in res:
            di[i['id']]="-".join([i['from_hour'],i['until_hours']])
        return di

    def save(self,student, hour, subject, classes, date, inputPresent, inputLate):
        cursor.execute(f"delete from attendance where student= {student} and hour = {hour}")

        cursor.execute(f"insert into attendance (day, hour, class, student, lesson, present, late) VALUES ({'10-10-1999'}, {hour}, "
                       f"{classes}, {student}, '{subject}', {bool(inputPresent)}, {bool(inputLate)})")

        sqliteConnection.commit()

attendance = Attendance()