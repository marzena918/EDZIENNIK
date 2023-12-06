from student import cursor, sqliteConnection


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
        cursor.execute(f"delete from attendance where student= {student} and hour = {hour}")
        cursor.execute(
            f"insert into attendance (day, hour, class, student, lesson, present, late) VALUES ('{date}', {hour}, "
            f"{classes}, {student}, '{subject}', {inputPresent}, {inputLate})")

        sqliteConnection.commit()

    def all_checkbox(self):
        return cursor.execute("select *  from attendance").fetchall()


attendance = Attendance()
