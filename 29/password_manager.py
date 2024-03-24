from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


#Creating a new window and configurations

window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20)

# Canvas

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="29/logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1, row=0)


# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w")
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2, sticky="w")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w")

#Entries

website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, sticky="w", columnspan=2)
website_entry.focus()

user_entry = Entry(width=55)
user_entry.insert(END, string="zdebarth@gmail.com")
user_entry.grid(column=1, row=2, sticky="w",columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons

password_button = Button(window, text="Generate Password", width=18)
password_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=46)
add_button.grid(column=1, row=4, columnspan=2, sticky="w" )


window.mainloop()