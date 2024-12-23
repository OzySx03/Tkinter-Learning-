from tkinter import *
from tkinter import messagebox
from tkinter import ttk


login_window = Tk()
login_window.geometry("700x600")
login_window.configure(bg="black")

primary_color = "#FFD700" 
secondary_color = "White"
bg_color = "#1A1A1A" 
font_main = ("Helvetica", 12)
font_title = ("Helvetica", 14, "bold")


def validate_login():
    admin_username="Ozzy"
    admin_password="1234"
    username=username_entry.get()
    password=password_entry.get()
    if username==admin_username and password==admin_password:
        login_window.destroy()
        new_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def new_screen():
    root = Tk()
    root.title("Register System")
    name = Label(root, text="Book Name:", bg=bg_color, fg=secondary_color, font=font_main)
    name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    e1 = Entry(root, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
    e1.grid(row=1, column=1, padx=10, pady=5)

    authorname = Label(root, text="Author Name:", bg=bg_color, fg=secondary_color, font=font_main)
    authorname.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    e2 = Entry(root, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
    e2.grid(row=2, column=1, padx=10, pady=5)

    publishyear = Label(root, text="Author Name:", bg=bg_color, fg=secondary_color, font=font_main)
    publishyear.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    e3 = Entry(root, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
    e3.grid(row=3, column=1, padx=10, pady=5)

    T=ttk.Treeview(root,columns=("Book Name","Author name","Publish Year"),show="headings")
    T.column("Book Name", width=55)
    T.column("Author Name", width=55)
    T.column("Publish Year", width=55)

    T.heading("Book Name",text="Book Name")
    T.heading("Author Name",text="Author Name")
    T.heading("Publish Year",text="Publish Year")
    T.pack()

    def func():
        T.insert("","end",values=(e1.get(),e2.get(),e3.get))
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    
    b=Button(root,text="Enter",command=func)
    b.grid(row=5, column=1, padx=10, pady=10)
    root.mainloop()

L1=Label(login_window, text="Username:", font=(font_main)).grid(row=0, column=0, pady=5, padx=5)
username_entry= Entry(login_window, font=font_title)
username_entry.grid(row=0,column=1,pady=5,padx=5)

L2=Label(login_window, text="Password:", font=(font_main)).grid(row=1, column=0, pady=5, padx=5)
password_entry= Entry(login_window, font=font_title, show="*")
password_entry.grid(row=1,column=1,pady=5,padx=5)

B=Button(login_window,text="Login",command=validate_login).grid(row=2,column=0,columnspan=2,padx=5,pady=5)

login_window.mainloop()
