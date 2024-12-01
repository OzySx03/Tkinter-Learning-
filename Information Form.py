from tkinter import *

root = Tk()
root.title("Information Form")
root.geometry("700x600")
root.configure(bg="black")

primary_color = "#FFD700" 
secondary_color = "White"
bg_color = "#1A1A1A" 
font_main = ("Helvetica", 12)
font_title = ("Helvetica", 14, "bold")

F1 = Frame(root, bg=bg_color, relief=RIDGE, bd=2)
F1.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

Label(F1, text="User Information", bg=bg_color, fg=primary_color, font=font_title).grid(row=0, column=0, columnspan=2, pady=10)

lname = Label(F1, text="Name:", bg=bg_color, fg=secondary_color, font=font_main)
lname.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e1 = Entry(F1, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
e1.grid(row=1, column=1, padx=10, pady=5)

lsname = Label(F1, text="Surname:", bg=bg_color, fg=secondary_color, font=font_main)
lsname.grid(row=2, column=0, padx=10, pady=5, sticky="w")
e2 = Entry(F1, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
e2.grid(row=2, column=1, padx=10, pady=5)

l1 = Label(F1, text="Additional Info:", bg=bg_color, fg=secondary_color, font=font_main)
l1.grid(row=3, column=0, padx=10, pady=5, sticky="w")

t = Text(F1, width=35, height=10, font=font_main, wrap=WORD, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
t.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

F2 = Frame(root, bg=bg_color, relief=RIDGE, bd=2)
F2.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

Label(F2, text="Output", bg=bg_color, fg=primary_color, font=font_title).grid(row=0, column=0, columnspan=2, pady=10)

L21 = Label(F2, text="Email:", bg=bg_color, fg=secondary_color, font=font_main)
L21.grid(row=1, column=0, padx=10, pady=5, sticky="w")
L22 = Label(F2, text=" ", bg=bg_color, fg=primary_color, font=font_main)
L22.grid(row=1, column=1, padx=10, pady=5, sticky="w")

L23 = Label(F2, text="Submitted Info:", bg=bg_color, fg=secondary_color, font=font_main)
L23.grid(row=2, column=0, padx=10, pady=5, sticky="nw")
L24 = Label(F2, text=" ", bg="#333333", fg=secondary_color, wraplength=200, justify="left", anchor="nw", relief=SOLID, width=30, height=10)
L24.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def delete():
    t.delete(1.0, END)

def selection():
    data= e1.get()+"."+e2.get()+"@fbu.edu.tr"
    L22["text"]=data

    text=t.get(1.0, END)
    L24["text"]=text

    delete()

b = Button(root, text="Generate", bg=primary_color, fg="#000000", font=font_main, command=selection, relief=FLAT)
b.grid(row=1, column=0, columnspan=2, pady=15)

root.mainloop()
