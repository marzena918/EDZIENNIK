from student import cursor, sqliteConnection
class Attendance:
    def get_sub_hour(self,day,classes):
        res = []
        is_full= cursor.execute(f"select hour_id, subject from lesson_plan where day='{day}' and "
                                f"classes_id = {classes}").fetchall()
        for i in is_full:
            if i['subject'] != '0':
                res.append(i)
                print(i['subject'])
        return res

    def get_all_hour(self):
        di = {}
        res = cursor.execute(f" select id, from_hour, until_hours from configurations_hours").fetchall()
        for i in res:
            di[i['id']]="-".join([i['from_hour'],i['until_hours']])
        print(di)
        return di
attendance = Attendance()