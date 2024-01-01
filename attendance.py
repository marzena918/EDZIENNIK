from collections import defaultdict

from student import cursor, sqliteConnection
import calendar


class Attendance:
    def get_sub_hour(self, day, classes):
        return cursor.execute(f"select hour_id, subject from lesson_plan "
                              f"join configurations_hours h on h.id = lesson_plan.hour_id "
                              f"where day='{day}' and classes_id = {classes} and subject is not null "
                              f"order by CAST(h.from_hour as integer) ").fetchall()

    def get_all_hour(self):
        di = {}
        res = cursor.execute(f" select id, from_hour, until_hours from configurations_hours").fetchall()
        for i in res:
            di[i['id']] = "-".join([i['from_hour'], i['until_hours']])
        return di

    def save(self, student, hour, subject, classes, date, inputPresent, inputLate):
        cursor.execute(f"delete from attendance where student= {student} and hour = {hour} and day= '{date}'")
        cursor.execute(
            f"insert into attendance (day, hour, class, student, lesson, present, late) VALUES ('{date}', {hour}, "
            f"{classes}, {student}, '{subject}', {inputPresent}, {inputLate})")

        sqliteConnection.commit()

    def all_checkbox(self):
        return cursor.execute("select *  from attendance").fetchall()

    def get_attendance_with_date_and_student(self, year: int, month: int, student_id: int):
        last_day = calendar.monthrange(year, month)[1]
        month = '0' + str(month) if month <= 9 else month
        query = (
            "select CAST(strftime('%d', att.day) as integer) as day, ch.from_hour as hour, lesson as subject, "
            "case when att.late = 1 then 'SP' else case when att.present = 1 then 'OB' else 'NB' end end as attendance "
            "from attendance att "
            "join configurations_hours ch on ch.id = att.hour "
            f"where student = {student_id} "
            f"  and day >= '{year}-{month}-01' and day <= '{year}-{month}-{last_day}'"
            f"order by att.day, ch.lp "
        )
        db_result = cursor.execute(query).fetchall()
        print(db_result)
        result = defaultdict(lambda: [])
        for i in db_result:
            result[str(i["day"])].append({"h": i["hour"], "att": i['attendance'], "sub": i['subject']})
        print(result, year, month)
        return result


attendance = Attendance()
