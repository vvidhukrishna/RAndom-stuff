from tkinter import *
from tkinter import messagebox
import math

root = Tk(className="calculator")
root.geometry("607x340")
root.configure(bg='black')
root.title("Calculator")

# making input/output bar
frame = LabelFrame(root, bg="black")
frame.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
d = Entry(frame, width=40, border=8)
d.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# defining functions

global math1
global f_num


def calculations(num):
    c = d.get()
    d.delete(0, END)
    d.insert(0, str(c) + str(num))


def decimal():
    F_n = d.get()
    global f_num
    global math1
    math1 = "dec"
    f_num = float(F_n)
    d.delete(0, END)


def pi():
    d.insert(0, math.pi)


def e():
    F_n = d.get()
    global f_num
    f_num = float(F_n)
    d.delete(0, END)
    e_x = math.e ** float(f_num)
    d.insert(0, e_x)


def iox():
    F_n = d.get()
    global f_num
    f_num = float(F_n)
    d.delete(0, END)
    ten_to_x = 10 ** float(f_num)
    d.insert(0, ten_to_x)


def natural_log():
    F_n = d.get()
    global f_num
    f_num = float(F_n)
    d.delete(0, END)
    n_log = math.log(f_num, math.e)
    d.insert(0, n_log)


def log_ten():
    F_n = d.get()
    global f_num
    f_num = float(F_n)
    d.delete(0, END)
    log__ten = math.log10(f_num)
    d.insert(0, log__ten)


def button_clear():
    d.delete(0, END)


def button_add():
    F_n = d.get()
    global f_num
    global math1
    math1 = "addition"
    f_num = float(F_n)
    d.delete(0, END)


def button_subract():
    F_n = d.get()
    global f_num
    global math1
    math1 = "subraction"
    f_num = float(F_n)
    d.delete(0, END)


def button_multiply():
    F_n = d.get()
    global f_num
    global math1
    math1 = "multiplication"
    f_num = float(F_n)
    d.delete(0, END)


def button_divide():
    F_n = d.get()
    global f_num
    global math1
    math1 = "division"
    f_num = float(F_n)
    d.delete(0, END)


def button_sin():
    F_n = d.get()
    global f_num
    global math1
    math1 = "sin"
    f_num = float(F_n)
    d.delete(0, END)
    d.insert(0, math.sin(f_num))


def button_cos():
    F_n = d.get()
    global f_num
    global math1
    math1 = "cos"
    f_num = float(F_n)
    d.delete(0, END)
    d.insert(0, math.cos(f_num))


def button_tan():
    F_n = d.get()
    global f_num
    global math1
    math1 = "tan"
    f_num = float(F_n)
    d.delete(0, END)
    d.insert(0, math.tan(f_num))


def button_asin():
    try:
        F_n = d.get()
        global f_num
        f_num = float(F_n)
        d.delete(0, END)
        d.insert(0, math.asin(f_num))
    except ValueError:
        response = messagebox.showerror("error", "the value is outside the range. range = +/- 1")


def button_acos():
    try:
        F_n = d.get()
        global f_num
        f_num = float(F_n)
        d.delete(0, END)
        d.insert(0, math.acos(f_num))
    except ValueError:
        response = messagebox.showerror("error", "the value is outside the range. range = +/- 1")


def button_atan():
    try:
        F_n = d.get()
        global f_num
        f_num = float(F_n)
        d.delete(0, END)
        d.insert(0, math.atan(f_num))
    except ValueError:
        response = messagebox.showerror("error", "the value is outside the range. range = +/- ∞")


def button_rt():
    F_n = d.get()
    global f_num
    global math1
    math1 = "rt"
    f_num = int(F_n)
    d.delete(0, END)
    rt = math.sqrt(f_num)
    d.insert(0, rt)


def button_square():
    global math1
    global f_num
    f_num = d.get()
    math1 = "square"
    d.delete(0, END)


def inverse():
    F_n = d.get()
    global f_num
    global math1
    math1 = "rev"
    f_num = float(F_n)
    d.delete(0, END)
    rev = float(f_num) - (float(f_num)*2)
    d.insert(0, rev)


def button_factorial():
    try:
        F_n = d.get()
        global f_num
        global math1
        math1 = "rev"
        f_num = int(F_n)
        d.delete(0, END)
        fac = math.factorial(f_num)
        d.insert(0, fac)
    except ValueError:
        response = messagebox.showerror("error", "This function can only take positive whole number values")


def button_eq():
    sec_num = d.get()
    d.delete(0, END)
    if math1 == "addition":
        d.insert(0, (f_num + float(sec_num)))
    elif math1 == "subraction":
        d.insert(0, (f_num - float(sec_num)))
    elif math1 == "multiplication":
        d.insert(0, (f_num * float(sec_num)))
    elif math1 == "division":
        d.insert(0, (f_num / float(sec_num)))
    elif math1 == "square":
        d.insert(0, float(f_num) ** float(sec_num))
    elif math1 == "dec":
        lol = f_num + (float(sec_num) / 10 * (len(str(sec_num))))
        d.insert(0, lol)
    else:
        d.insert(0, "invalid input")


def popup():
    response = messagebox.askyesno("control check", "Are you sire you want to exit?")
    if response == 1:
        exit()
    else:
        return


# padx, pady:
x = 40
y = 15

# creating all the buttons

# numbers
button_1 = Button(root, text="1", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(1))
button_2 = Button(root, text="2", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(2))
button_3 = Button(root, text="3", padx=x+2, pady=y, fg="black", bg="gray", command=lambda: calculations(3))
button_4 = Button(root, text="4", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(4))
button_5 = Button(root, text="5", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(5))
button_6 = Button(root, text="6", padx=x+2, pady=y, fg="black", bg="gray", command=lambda: calculations(6))
button_7 = Button(root, text="7", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(7))
button_8 = Button(root, text="8", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(8))
button_9 = Button(root, text="9", padx=x+2, pady=y, fg="black", bg="gray", command=lambda: calculations(9))
button_0 = Button(root, text="0", padx=x, pady=y, fg="black", bg="gray", command=lambda: calculations(0))
button_decimal = Button(root, text=".", padx=x + 1, pady=y, bg="gray", command=decimal).grid(row=4, column=1)
button_inverse = Button(root, text="+ --> -", padx=x - 15, pady=y, bg="red", command=inverse).grid(row=0, column=6)

# normal operations:
button_add = Button(root, text="+", padx=x - 2, pady=y, fg="black", bg="orange", command=button_add)
button_subract = Button(root, text="-", padx=x, pady=y, fg="black", bg="orange", command=button_subract)
button_multiply = Button(root, text="*", padx=x, pady=y, fg="black", bg="orange", command=button_multiply)
button_divide = Button(root, text="/", padx=x, pady=y, fg="black", bg="orange", command=button_divide)

# trig functions:
button_sin = Button(root, text="sin", padx=x + 1, pady=y, bg="blue", command=button_sin).grid(row=1, column=5)
button_cos = Button(root, text="cos", padx=x - 1, pady=y, bg="blue", command=button_cos).grid(row=2, column=5)
button_tan = Button(root, text="tan", padx=x, pady=y, bg="blue", command=button_tan).grid(row=3, column=5)

# factorial button:
button_factorial = Button(root, text="!", padx=x+1, pady=y, bg="cyan", command=button_factorial).grid(row=5, column=0)

# inverse trig buttons
button_asin = Button(root, text="asin", padx=x, pady=y, bg="blue", command=button_asin).grid(row=1, column=6)
button_acos = Button(root, text="acos", padx=x-2, pady=y, bg="blue", command=button_acos).grid(row=2, column=6)
button_atan = Button(root, text="atan", padx=x-1, pady=y, bg="blue", command=button_atan).grid(row=3, column=6)

# constants and logs:
button_e = Button(root, text="e^x", padx=x-6, pady=y, bg="cyan", command=e).grid(row=5, column=1)
button_pi = Button(root, text="π", padx=x, pady=y, bg="cyan", command=pi).grid(row=5, column=2)
button_iox = Button(root, text="10^x", padx=x-10, pady=y, bg="cyan", command=iox).grid(row=5, column=4)
button_log_e = Button(root, text="ln", padx=x+4, pady=y, bg="cyan", command=natural_log).grid(row=5, column=5)
button_log_10 = Button(root, text="log 10", padx=x-6, pady=y, bg="cyan", command=log_ten).grid(row=5, column=6)

# inverse and power button
button_inv = Button(root, text="√", padx=x + 5, pady=y, bg="blue", command=button_rt).grid(row=4, column=5)
button_pow = Button(root, text="x^y", padx=x, pady=y, bg="blue", command=button_square).grid(row=4, column=6)

# equal and clear button
button_equal = Button(root, text="=", padx=x+1, pady=y, fg="black", bg="orange", command=button_eq)
button_clear = Button(root, text="clear", padx=x - 10, pady=y, fg="black", bg="red", command=button_clear)

# exit button
button_exit = Button(root, text="exit", padx=x - 10, pady=y, fg="black", bg="red", command=popup)

# displaying all the buttons(numbers)
button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=0)

# displaying all the buttons(operations)
button_equal.grid(row=4, column=2)
button_clear.grid(row=0, column=5)

button_add.grid(row=1, column=4)
button_subract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)

# displaying the exit button:
button_exit.grid(row=0, column=4)

root.mainloop()
