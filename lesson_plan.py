from student import cursor, sqliteConnection


class LessonPlan:
    def save(self, clases_id, data):
        cursor.execute(f"delete  from lesson_plan where classes_id = {clases_id}")


        days = {'monday': 'poniedziałek', 'tuesday': 'wtorek', 'wednesday':'środa', 'thursday': 'czwartek', 'friday': 'piątek'}
        for day, v in data.items():
            for hour, sub_teach in v.items():

                # cursor.execute(f"insert into lesson_plan (day, classes_id, hour_id) VALUES ('{day}', {clases_id}, '{hour}'")
                # # if hour:
                # #     cursor.execute(f"insert into lesson_plan (hour_id) VALUES ({hour}")
                # if sub_teach['subject']:
                #     cursor.execute(f"insert into lesson_plan (subject) VALUES ('{sub_teach['subject']}'")
                # if sub_teach['teacher']:
                #     cursor.execute(f"insert into lesson_plan (teacher) VALUES ({sub_teach['teacher']}")
                cursor.execute(f"insert into lesson_plan (day, hour_id, subject, teacher, classes_id) VALUES "
                               f"('{days[day]}', {hour}, '{sub_teach['subject'] if sub_teach['subject'] else '0'}', "
                               f"{sub_teach['teacher'] if sub_teach['teacher'] else 0}, {clases_id})")
        sqliteConnection.commit()

    def get_plan(self, class_id):
        return cursor.execute(f"select * from lesson_plan where classes_id = {class_id}").fetchall()


lesson_plan = LessonPlan()
