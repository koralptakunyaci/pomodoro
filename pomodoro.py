from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DEFAULT = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(time)
    timer_text.config(text=" WORK TIME ", font=(FONT_NAME, 60), bg=YELLOW, fg=DEFAULT)
    check_mark.config(text="")
    canvas.itemconfig(timer, text=f"00 00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 0 and reps != 8:
        count_down(short_break)
        timer_text.config(text="SHORT BREAK", font=(FONT_NAME, 60), fg=RED)
    elif reps % 8 == 0:
        count_down(long_break)
        timer_text.config(text="LONG  BREAK", font=(FONT_NAME, 60), fg=RED)
    else:
        count_down(work_sec)
        timer_text.config(text=" WORK TIME ", font=(FONT_NAME, 60), bg=YELLOW, fg=DEFAULT)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text=f"{count_min} {count_seconds}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=525, pady=300, bg=YELLOW)
window.attributes("-fullscreen", True)

# Canvas
canvas = Canvas(width=420, height=305, bg=YELLOW, highlightthickness=0)
clock = PhotoImage(file="clock.png")
canvas.create_image(210, 152, image=clock)
timer = canvas.create_text(209, 138, text="00 00", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_text = Label(text=" WORK TIME ", font=(FONT_NAME, 60), bg=YELLOW)
timer_text.grid(column=1, row=0)

# Start Button
start_btn = Button(text="Start", width=25, height=2, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", width=25, height=2, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Check Label
check_mark = Label(font=(FONT_NAME, 20), bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
