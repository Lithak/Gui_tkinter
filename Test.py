from tkinter import *
from tkinter import Tk

window = Tk()
window.title("TempConvert Web Service")
window.geometry('980x400')
window.configure(background="#7C7FBC")
# window.configure(width=700, height=600)

label1 = Label(text="Temperature Convert Web Service", padx="21", pady="20",background="#7C7FBC", font="Bold" )
label1.grid(row=0, column=3)

Mylabels1 = LabelFrame(window, text="Celsius to F", padx=50, pady=50, background='#7C7FBC', font="Bold")
Mylabels1.grid(row=1, column=1)

fstNum = Entry(Mylabels1, state="disable")
fstNum.grid(row=2, column=3)

Mylabels2 = LabelFrame(window, text="Celsius to F", padx=50, pady=50, background='#7C7FBC', font="Bold")
Mylabels2.grid(row=1, column=5)

secNum = Entry(Mylabels2, state="disable")
secNum.grid(row=4, column=3)

celsius_var = IntVar()
fahrenheit_var = IntVar()

# (0°F − 32) × 5/9 = -17,78°C
# (0°C × 9/5) + 32 = 32°F


"""def convert_to_fahrenheit():
celsius_1 = float(celsius_var.get())
fahrenheit_1 = (celsius_1 - 9/5) + 32
answer_lbl_F.config(text=round(fahrenheit_1, 2))"""


def Cel_Active():
    fstNum.configure(state="normal")


btn_activate_cel = Button(window, text="Activate Cel to Fah", bg="grey",  background='#4D5195',command=Cel_Active, font="Bold")
btn_activate_cel.grid(row=12, column=1)
answer_lbl = Label(text="", justify=RIGHT, width=8, background='#6D71BE', font="Bold")
answer_lbl.grid(row=6, column=3)


def conversion():
    if fstNum:
        celsius = float(celsius_var.get())
        fahrenheit = (celsius - 9 / 5) + 32
        answer_lbl.config(text=round(fahrenheit, 2))
    if secNum:
        fahrenheit = float(fahrenheit_var.get())
        celsius = (fahrenheit - 32) * 5 / 9
        answer_lbl.config(text=round(celsius, 2))


"""def convert_to_celsius():
fahrenheit = float(fahrenheit_var.get())
celsius = (fahrenheit - 32) * 5 / 9
answer_lbl_C.config(text=round(celsius, 2))"""


def Fah_Active():
    secNum.configure(state="normal")


btn_activate_Fah = Button(window, text="Activate Fah to Cel", bg="grey", background='#4D5195',font="Bold", command=Fah_Active)
btn_activate_Fah.grid(row=12, column=5)

btn_calc_conv = Button(window, text="Calculate Conversion", bg="grey",  background='#6D71BE', font="Bold", command=conversion)
btn_calc_conv.grid(row=18, column=3)


def clear():
    fstNum.delete(0, END)
    secNum.delete(0, END)


clear_button = Button(window, text="Clear", bg="grey", font="Bold", command=clear)
clear_button.grid(row=24, column=8)


def exit_program():
        window.destroy()


exit_btn = Button(text="Exit", font="Bold", bg='red', command=exit_program)
exit_btn.grid(row=28, column=8)

window.mainloop()
