from tkinter import *

# Create window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
e = Entry(root, width=25, borderwidth=5, font=('Arial', 16))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to click number
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

# Clear screen
def clear():
    e.delete(0, END)

# Operation functions
def add():
    global f_num
    global op
    f_num = int(e.get())
    op = "+"
    e.delete(0, END)

def subtract():
    global f_num
    global op
    f_num = int(e.get())
    op = "-"
    e.delete(0, END)

def multiply():
    global f_num
    global op
    f_num = int(e.get())
    op = "*"
    e.delete(0, END)

def divide():
    global f_num
    global op
    f_num = int(e.get())
    op = "/"
    e.delete(0, END)

# Equal function
def equal():
    s_num = int(e.get())
    e.delete(0, END)

    if op == "+":
        e.insert(0, f_num + s_num)
    elif op == "-":
        e.insert(0, f_num - s_num)
    elif op == "*":
        e.insert(0, f_num * s_num)
    elif op == "/":
        if s_num != 0:
            e.insert(0, f_num / s_num)
        else:
            e.insert(0, "Error")

# Buttons
Button(root, text="1", command=lambda: click(1)).grid(row=1, column=0)
Button(root, text="2", command=lambda: click(2)).grid(row=1, column=1)
Button(root, text="3", command=lambda: click(3)).grid(row=1, column=2)

Button(root, text="4", command=lambda: click(4)).grid(row=2, column=0)
Button(root, text="5", command=lambda: click(5)).grid(row=2, column=1)
Button(root, text="6", command=lambda: click(6)).grid(row=2, column=2)

Button(root, text="7", command=lambda: click(7)).grid(row=3, column=0)
Button(root, text="8", command=lambda: click(8)).grid(row=3, column=1)
Button(root, text="9", command=lambda: click(9)).grid(row=3, column=2)

Button(root, text="0", command=lambda: click(0)).grid(row=4, column=1)

Button(root, text="+", command=add).grid(row=1, column=3)
Button(root, text="-", command=subtract).grid(row=2, column=3)
Button(root, text="*", command=multiply).grid(row=3, column=3)
Button(root, text="/", command=divide).grid(row=4, column=3)

Button(root, text="=", command=equal).grid(row=4, column=2)
Button(root, text="Clear", command=clear).grid(row=4, column=0)

root.mainloop()