from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

current_card = ""

def load_dictionary():
    dict_french = pandas.read_csv("31/data/french_words.csv")
    # dict_french = dict_french.head() # for testing purposes
    dict_french = dict_french.set_index("French")["English"].to_dict()
    dict_english = {v: k for k, v in dict_french.items()}
    return dict_french, dict_english

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=dict_french[current_card], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list(dict_french))
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    window.after(3000, func=flip_card)


# Creating a new window and configurations
window = Tk()
window.title("Flash Card Application")
window.minsize(width=500, height=500)
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)


# Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="31/images/card_front.png")
card_back_image = PhotoImage(file="31/images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_image)
title = canvas.create_text(400, 150, text = "Title", fill="black", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text = "Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Wrong button
wrong_image = PhotoImage(file="31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, background=BACKGROUND_COLOR, bd=0, relief="flat", command=next_card)
wrong_button.grid(row=1, column=0)


# Right button
right_image = PhotoImage(file="31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, background=BACKGROUND_COLOR, bd=0, relief="flat", command=next_card)
right_button.grid(row=1, column=1)

dict_french, dict_english = load_dictionary()
next_card()
window.mainloop()

