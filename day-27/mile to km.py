from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometres_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to KM Convertor")
miles_input = Entry(width=7)
window.config(padx=20, pady=20)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
kilometres_result_label = Label(text="0")
kilometres_result_label.grid(column=1, row=1)
kilometres_label = Label(text="Km")
kilometres_label.grid(column=2, row=2)
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window, mainloop()
