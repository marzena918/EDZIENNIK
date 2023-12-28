from datetime import datetime

from student import cursor, sqliteConnection

class LessonPlanForParents:

    def lesson_plan_with_attendance(self, student_id,month):
        attendance= cursor.execute(f"select * from attendance where student = {student_id}").fetchall()
        attendance_by_month = []
        for i in attendance:
            for k, v in i.items():
                if k == 'day':
                    mon = datetime.strptime(v, '%Y-%m-%d')
                    if mon.month ==int(month):
                        attendance_by_month.append(i)
        print(attendance_by_month)
        return attendance_by_month

lesson_plan_for_parents = LessonPlanForParents()