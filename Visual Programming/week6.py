from tkinter import *
root = Tk()
root.geometry("400x400")
def engin():
    root.configure(bg="red")
l=Label(root, text="enter your GSM number", bg="red", font=("arial",25)).place(x=50 , y=100)
e=Entry(root, font=("arial",25) ).place(x=400, y=100)
root.mainloop()