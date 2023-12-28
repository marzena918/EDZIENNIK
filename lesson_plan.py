from student import cursor, sqliteConnection


class LessonPlan:
    def save(self, clases_id, data):
        cursor.execute(f"delete  from lesson_plan where classes_id = {clases_id}")
        days = {'monday': 'poniedziałek', 'tuesday': 'wtorek', 'wednesday':'środa', 'thursday': 'czwartek', 'friday': 'piątek'}
        for day, v in data.items():
            for hour, sub_teach in v.items():
                cursor.execute(f"insert into lesson_plan (day, hour_id, subject, teacher, classes_id) VALUES "
                               f"('{days[day]}', {hour}, '{sub_teach.get('subject')}', {sub_teach.get('teacher')},"
                               f" {clases_id})")
        sqliteConnection.commit()

    def get_plan(self, class_id):
        return cursor.execute(f"select * from lesson_plan where classes_id = {class_id}").fetchall()


lesson_plan = LessonPlan()
