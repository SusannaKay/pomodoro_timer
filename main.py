from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps+=1
    if reps%8 == 0:
        countdown(LONG_BREAK_MIN)
        title_label.config(text="Break",fg=RED)
    elif reps%2 == 0:
        countdown(SHORT_BREAK_MIN)
        title_label.config(text="Break",fg=PINK)
    else:
        countdown(WORK_MIN)
        title_label.config(text="Timer",fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    
    minutes = math.floor(count/60)
    seconds= count%60
    if seconds < 10:
        seconds =f"0{seconds}"
    

    canvas.itemconfig(timer_text,text=f'{minutes}:{seconds}')
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW, padx=100,pady=50)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1,row=0)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato)
timer_text = canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 30) )
canvas.grid(column=1,row=1)



reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=3)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

check_text = Label(text="✓", fg=GREEN, bg=YELLOW, font=(20))
check_text.grid(column=1, row=2)
window.mainloop()




