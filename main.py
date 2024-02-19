from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW, padx=100,pady=50)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1,row=0)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato)
canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 30) )
canvas.grid(column=1,row=1)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=3)

start_button = Button(text="start", highlightthickness=0)
start_button.grid(column=0, row=3)

check_text = Label(text="✓", fg=GREEN, bg=YELLOW, font=(20))
check_text.grid(column=1, row=2)
window.mainloop()




