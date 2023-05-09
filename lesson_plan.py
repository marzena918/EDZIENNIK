from student import cursor, sqliteConnection


class LessonPlan:
    def get_all(self):
        return cursor.execute(
            "select class.name as name_class,class.id, teacher.name, teacher.last_name from class join teacher on class.tutor = teacher.id").fetchall()

    def get_all_hours(self):
        return cursor.execute("select * from configurations_hours").fetchall()


lesson_plan = LessonPlan()
