from student import cursor, sqliteConnection

class Configuration_hours:

    def save_hours(self, i_from, i_until, lp):
        lp_bool = cursor.execute(f"select lp from configurations_hours where lp = {lp}").fetchall()
        if lp_bool:
            cursor.execute(f" DELETE from configurations_hours where lp ={lp} ")
        cursor.execute(
            f"insert into configurations_hours(lp,from_hour, until_hours) VALUES ({lp},'{i_from}', '{i_until}')")
        sqliteConnection.commit()

    def get_all(self):
        return cursor.execute("select * from configurations_hours order by lp asc ").fetchall()


configuration_of_hours = Configuration_hours()
