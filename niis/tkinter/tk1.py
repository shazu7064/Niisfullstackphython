from tkinter import *

root = Tk()
root.title("Addition of Three Numbers")
root.geometry("300x250")

Label(root, text="Enter First Number").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Enter Second Number").pack()
e2 = Entry(root)
e2.pack()

Label(root, text="Enter Third Number").pack()
e3 = Entry(root)
e3.pack()

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = int(e3.get())
    result = n1 + n2 + n3
    Label(root, text="Sum = " + str(result)).pack()

Button(root, text="Add", command=add).pack()

root.mainloop()