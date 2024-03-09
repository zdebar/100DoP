import tkinter
import turtle

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)

# Label
my_label = tkinter.Label(text="Miles to kilometer convertor", font=("Courier", 16))
my_label.pack()

# Two options for updating label
# my_label["text"] = "New text"
# my_label.config(text="New Text")

# Button

def button_clicked():
    in_word = input.get()
    my_label.config(text=in_word)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=50)
input.pack()


window.mainloop()

