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

    def save(self, student, hour, subject, classes, date, inputPresent, inputLate, input_no_present):
        # no_present = False if input_no_present else None
        cursor.execute(f"delete from attendance where student= {student} and hour = {hour} and day= '{date}'")
        cursor.execute(
            f"insert into attendance (day, hour, class, student, lesson, present, late,excuse) VALUES ('{date}', {hour}, "
            f"{classes}, {student}, '{subject}', {inputPresent}, {inputLate},{input_no_present})")

        sqliteConnection.commit()

    def all_checkbox(self):
        return cursor.execute("select *  from attendance").fetchall()

    def get_attendance_with_date_and_student(self, year: int, month: int, student_id: int):
        last_day = calendar.monthrange(year, month)[1]
        month = '0' + str(month) if month <= 9 else month
        query = (
            "select CAST(strftime('%d', att.day) as integer) as day, att.student, ch.from_hour as hour, lesson as subject, "
            "case when att.late = 1 then 'SP' else case when att.present = 1 then 'OB' else case when att.excuse=1 then 'USP' else case when att.present = 0 then'NB' end end end end as attendance "
            "from attendance att "
            "join configurations_hours ch on ch.id = att.hour "
            f"where student = {student_id} "
            f"  and day >= '{year}-{month}-01' and day <= '{year}-{month}-{last_day}'"
            f"order by att.day, ch.lp "
        )
        db_result = cursor.execute(query).fetchall()
        result = defaultdict(lambda: [])
        for i in db_result:
            result[str(i["day"])].append(
                {"h": i["hour"], "att": i['attendance'], "sub": i['subject'], "student_id": i['student']})
        return result

    def update(self, all_data):
        data_to_base = {}
        for i in range(len(all_data)):
            data_to_base[i] = {"day": (all_data[i][0].split("+")[1]), "student_id": all_data[i][0].split("+")[0],"sub": all_data[i][0].split("+")[2],"hour":all_data[i][0].split("+")[3]}
        for k,v in data_to_base.items():

            cursor.execute(f"update attendance SET excuse=1 where student = {v['student_id']} and day='{v['day']}' "
                           f"and lesson = '{v['sub']}' and hour = (select id from configurations_hours "
                           f"join attendance on configurations_hours.id = attendance.hour "
                           f"where from_hour = {v['hour']} limit 1)")
        cursor.connection.commit()

    def summary(self, student_id):
        b = cursor.execute(f"select late,present,excuse from attendance where student = {student_id}").fetchall()
        return b


attendance = Attendance()
