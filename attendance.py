from student import cursor, sqliteConnection
class Attendance:
    def get_sub_hour(self,day,classes):
        res = []
        is_full= cursor.execute(f"select hour_id, subject from lesson_plan where day='{day}' and "
                                f"classes_id = {classes}").fetchall()
        for i in is_full:
            if i['hour_id'] != 0:
                res.append(i)
        print(res)
        return res
attendance = Attendance()