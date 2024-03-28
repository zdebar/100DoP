from tkinter import *
import datetime

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 





# ---------------------------- TIMER MECHANISM ------------------------------- # 


def repetitions(R):
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    match R % 8:
        case 1|3|5|7: 
            count_down_time = work_sec
        case 2|4|6: count_down_time = short_break_sec
        case 0: count_down_time = long_break_sec
    return count_down_time

def start_timer():
    global REPS
    count_down(repetitions(REPS))
    REPS += 1 

def reset_time():
    window.after_cancel(TIMER)
    global REPS
    REPS = 1
    canvas.itemconfig(time_text, text=seconds_to_mm_ss(repetitions(REPS)))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def seconds_to_mm_ss(seconds):
    td = datetime.timedelta(seconds=seconds)
    return str(td)[-5:]

def count_down(count):
    global TIMER
    canvas.itemconfig(time_text, text=seconds_to_mm_ss(count))
    if count > 0:
       TIMER = window.after(1000, count_down, count-1) # po 1000ms udělá akci
    else:
        canvas.itemconfig(time_text, text=seconds_to_mm_ss(repetitions(REPS)))


# ---------------------------- UI SETUP ------------------------------- #


#Creating a new window and configurations

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
time_text = canvas.create_text(100, 135, text = seconds_to_mm_ss(repetitions(REPS)), fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)


# Buttons

button_start = Button(text="Start", width=10, command=start_timer)
button_start.grid(column=2, row=1)
button_start.config(pady=5)

button_reset = Button(text="Reset", width=10, command=reset_time)
button_reset.grid(column=0, row=1)
button_reset.config(pady=5)



window.mainloop()