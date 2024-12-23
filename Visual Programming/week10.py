from tkinter import *
root= Tk()
root.geometry("600x600")

l=Label(root,text="male", bg="yellow",fg="red", font=("Arial", 50))
l.pack()
def gender():
    x=data.get()
    if (x==1):
        l["text"]="female"
        l["bg"]="red"
        l["fg"]="yellow"
    else:
        l["text"]="male"
        l["bg"]="yellow"
        l["fg"]="red"
data=IntVar()
c=Checkbutton(root, text="change the info", variable=data, onvalue=1, offvalue=0, command=gender)
c.pack()


root.mainloop()