from tkinter import *
import requests

data = "Click to read"
def get_quote():
    # Connect to API Endpoint URL
    response = requests.get(url="https://api.kanye.rest/")
    # Request module for various Error responses
    response.raise_for_status()
    # Reading position of ISS
    quote = response.json()["quote"] 
    canvas.itemconfig(quote_text, text=quote)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click button for quote", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()