from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("700x600")
root.configure(bg="black")

primary_color = "#FFD700" 
secondary_color = "White"
bg_color = "#1A1A1A" 
font_main = ("Helvetica", 12)
font_title = ("Helvetica", 14, "bold")

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
gender=ttk.Combobox(F1, width = 27)
gender["values"]=("Male","Female")
gender.grid(row=3, column=1, padx=10, pady=5)
spinboxname = Label(F1, text="Age:", bg=bg_color, fg=secondary_color, font=font_main)
spinboxname.grid(row=4, column=0, padx=10, pady=5, sticky="w")
spinbox=Spinbox(F1,from_=0, to=120,width=10)
spinbox.grid(row=4, column=1, padx=10, pady=5)

F2 = Frame(root, bg=bg_color, relief=RIDGE, bd=2)
F2.grid(row=0, column=0, padx=15, pady=200, sticky="nsew")
T=ttk.Treeview(F2,columns=("Name","Surname","Gender","Age"),show="headings")
T.column("Name", width=55)
T.column("Surname", width=55)
T.column("Gender", width=55)
T.column("Age", width=55)

T.heading("Name",text="Name")
T.heading("Surname",text="Surname")
T.heading("Gender",text="Gender")
T.heading("Age",text="Age")
T.pack()

def func():
    T.insert("","end",values=(e1.get(),e2.get(),gender.get(),spinbox.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    gender.delete(0,END)
    spinbox.delete(0,END)

b=Button(F1,text="Enter",command=func)
b.grid(row=5, column=1, padx=10, pady=10)
root.mainloop()