from tkinter import *

window = Tk()
window.title("My first program")
window.minsize(width=500, height=300)

button_click = "I am good"


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

    print("Button clicked")


# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column= 0, row= 0)
my_label['text'] = "New Text"
my_label.config(text="New Text")


# Button

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
print(input.get())


window.mainloop()
