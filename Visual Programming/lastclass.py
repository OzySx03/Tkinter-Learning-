import sqlite3

connection=sqlite3.connect("my_database.db")
cursor=connection.cursor()

create_table_query= """
CREATE TABLE IF NOT EXISTS Students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
email TEXT
)
"""
cursor.execute(create_table_query)

insert_query="""
INSERT INTO Students (id,name,age,email)
VALUES(?,?,?,?)
"""
student_data=(1,"Ozan",21,"ozan.yildiz2@stu.fbu.edu.tr")

cursor.execute(insert_query, student_data)

connection.commit()
connection.close()