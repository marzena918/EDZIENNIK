from student import cursor, sqliteConnection

class Parents:
    def get_all_parent(self):
        return cursor.execute("select * from parents").fetchall()

    # def delete(self, id):

    def dodaj(self, name, surname, pesel):
        cursor.execute(f"insert into parents(name, last_name, pesel) "
                       f"VALUES ('{name}','{surname}',{pesel})")
        sqliteConnection.commit()

    def delete(self, id):
        cursor.execute(f"DELETE from parents where id = '{id}'")
        sqliteConnection.commit()

    def update(self, id,name, surname, pesel):
        cursor.execute(
            f"UPDATE parents set name = '{name}',last_name ='{surname}', pesel = '{pesel}' where id = '{id}'")
        sqliteConnection.commit()

    def is_pesel_exist(self, pesel) -> bool:
        return bool(cursor.execute(f"select pesel from parents where pesel = '{pesel}'").fetchall())

    def get_parent(self,id):
        return cursor.execute(f"select name, last_name from parents where id= {id}").fetchall()[0]

parents = Parents()
#
# d = {"1":[{"g":"33"}, {"ff":'34'}]}
# for i in d: