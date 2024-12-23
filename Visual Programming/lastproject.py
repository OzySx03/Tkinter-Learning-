import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.configure(bg="black")

primary_color = "#FFD700"
secondary_color = "White"
bg_color = "#1A1A1A"
font_main = ("Helvetica", 12)
font_title = ("Helvetica", 14, "bold")
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
surname TEXT NOT NULL,
gender TEXT NOT NULL,
age INTEGER NOT NULL
)
""")
connection.commit()

F1 = Frame(root, bg=bg_color, relief=RIDGE, bd=2)
F1.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

lname = Label(F1, text="Name:", bg=bg_color, fg=secondary_color, font=font_main)
lname.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e1 = Entry(F1, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
e1.grid(row=1, column=1, padx=10, pady=5)

lsname = Label(F1, text="Surname:", bg=bg_color, fg=secondary_color, font=font_main)
lsname.grid(row=2, column=0, padx=10, pady=5, sticky="w")
e2 = Entry(F1, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
e2.grid(row=2, column=1, padx=10, pady=5)

gendername = Label(F1, text="Gender:", bg=bg_color, fg=secondary_color, font=font_main)
gendername.grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender = ttk.Combobox(F1, width=27)
gender["values"] = ("Male", "Female")
gender.grid(row=3, column=1, padx=10, pady=5)

spinboxname = Label(F1, text="Age:", bg=bg_color, fg=secondary_color, font=font_main)
spinboxname.grid(row=4, column=0, padx=10, pady=5, sticky="w")
spinbox = Spinbox(F1, from_=0, to=120, width=10)
spinbox.grid(row=4, column=1, padx=10, pady=5)

def func():
    name = e1.get()
    surname = e2.get()
    student_gender = gender.get()
    age = spinbox.get()

    insert_query = """
    INSERT INTO Students (name, surname, gender, age)
    VALUES(?, ?, ?, ?)
    """
    cursor.execute(insert_query, (name, surname, student_gender, age))
    connection.commit()

def func1():
    student_name = e1.get()

    delete_query = """
    DELETE FROM Students 
    WHERE name = ?
    """
    cursor.execute(delete_query, (student_name,))
    connection.commit()


b = Button(F1, text="Enter", command=func)
b1 = Button(F1, text="Delete", command=func1)
b.grid(row=5, column=1, padx=10, pady=10)
b1.grid(row=5, column=2, padx=10, pady=10)

root.mainloop()
