from student import cursor

class Classes:
    def get_all(self):
        return cursor.execute("select * from subject").fetchall()

    def add(self, subject):
        cursor.execute(f"insert into subject VALUES ('{subject}')")
        cursor.connection.commit()

    def remove(self, subject):
        cursor.execute(f"delete FROM subject WHERE name = '{subject}'")
        cursor.connection.commit()

    def edit(self,old_subject, new_subject):
        cursor.execute(f" update subject SET name='{new_subject}' where name='{old_subject}'")
        cursor.connection.commit()

classes = Classes()