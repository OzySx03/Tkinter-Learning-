#from tkinter import *
#root= Tk()
#root.geometry("600x600")
#l=Label(root,text="Select the menu", bg= "yellow", fg="blue", font=("Arial", 50))
#l.pack(pady=20)
#data=StringVar()
#cmbx=ttk.Combobox(root, values=["pizza", "burger", "vegan"], textvariable=data)
#cmbx.pack
#def selection():
#    slct=f"you selected {data.get()}"
#    l["text"]=slct
#b=Button(root, text="Click", command=selection, bg="blue")
#b.pack(fill="x")
#root.mainloop()

#from tkinter import *
#root= Tk()
#root.geometry("600x600")
#l=Label(root,text="Select the menu", bg= "yellow", fg="blue", font=("Arial", 50))
#l.pack(pady=20)
#data=StringVar()
#def selection():
#    slct=f"you selected {data.get()}"
#    l["text"]=slct
#r=Radiobutton(root, text="pizza", value="pizza", variable=data, command=selection, indicatoron=0)
#r.pack()
#r1=Radiobutton(root, text="burger", value="burger", variable=data, command=selection, indicatoron=0)
#r1.pack()
#r2=Radiobutton(root, text="vegan", value="vegan", variable=data, command=selection, indicatoron=0)
#r2.pack()
#root.mainloop()

from tkinter import *
root= Tk()
root.geometry("600x600")
l=Label(root,text="Select the menu", bg= "yellow", fg="blue", font=("Arial", 50))
l.pack(pady=20)
data=StringVar()
def selection():
    slct=f"you selected {data.get(ANCHOR)}"
    l["text"]=slct

lb=Listbox(root)
lb.insert(1,"pizza")
lb.insert(2,"burger")
lb.insert(3,"vegan")
lb.pack()
b=Button(root, text="Click", bg="blue", command=selection)
b.pack(fill=BOTH, pady=10)
root.mainloop()