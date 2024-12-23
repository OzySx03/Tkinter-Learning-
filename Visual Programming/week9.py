from tkinter import *
root = Tk()
root.geometry("600x600")
def func():
    v=E.get()
    l["text"]=v


data=StringVar()
E=Entry(root, textvariable=data)
E.pack()

b=Button(root,text="Click", command=func)
b.pack()

l=Label(root, text="enter text")
l.pack()
root.mainloop()