from tkinter import *
from tkinter import messagebox 

root = Tk()
root.geometry("700x600")
root.configure(bg="black")

primary_color = "#FFD700" 
secondary_color = "White"
bg_color = "#1A1A1A" 
font_main = ("Helvetica", 12)
font_title = ("Helvetica", 14, "bold")

cnvs = Canvas(root, width=600, height=500, bg=primary_color)
cnvs.pack(anchor=CENTER, pady=20)

cnvs.create_rectangle((0, 0), (600, 100), fill=bg_color)
cnvs.create_text(300, 50, text="Temperature Converter", fill="white", font=font_title)

def func():
    try:
        fahrenheit = float(e1.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result_label.config(text=f"{celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

e1 = Entry(root, font=font_main, width=25, bg="#333333", fg=secondary_color, insertbackground=secondary_color)
e1.pack()
cnvs.create_text(50, 150, text="Fahrenheit:", fill="white", font=font_main)
cnvs.create_window(250, 150, window=e1)

b = Button(root, text="Click", command=func)
b.pack()
cnvs.create_window(500, 150, window=b)

cnvs.create_text(400, 300, text="Fahrenheit:", fill="white", font=font_main)
cnvs.create_text(550, 300, text="Celsius:", fill="white", font=font_main)

result_label = Label(root, text=" ", font=font_main, bg=primary_color, fg=secondary_color)
result_label.pack()
cnvs.create_window(475, 300, window=result_label)

root.mainloop()