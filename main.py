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
window.config(height=223, width=400)



canvas = Canvas(height=443, width=400)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(200,212, image = tomato)
canvas.create_text(200,232, text="00:00", fill="white", font=(FONT_NAME, 30) )
canvas.pack()


window.mainloop()



