from tkinter import *

BLACK = "#3d3d3d"
YELLOW = "#e09a19"
WHITE = "#ECDFCC"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
FONT = "Lucida Console"
timer = None

#Timer Reset
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="TIMER", fg=WHITE)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")

#timer mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        title.config(text="LONG BREAK", fg=WHITE)
        count_down(long_break_sec)
    elif reps%2==0:
        title.config(text="BREAK", fg=WHITE)
        count_down(short_break_sec)
    else:
        title.config(text="WORK", fg=WHITE)
        count_down(work_sec)

#countdown mechanism
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔"
        check_mark.config(text=mark)


#User interface
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BLACK)

canvas = Canvas(width=400, height=400, bg=BLACK, highlightthickness=0)
bg_pic = PhotoImage(file="image.png")
canvas.create_image(200, 200, image=bg_pic)
timer_text = canvas.create_text(202, 140, text="00:00", font=(FONT, 54, "bold"), fill=YELLOW)
canvas.grid(row=1, column=1)

title = Label(text="TIMER", font=(FONT, 44, "bold"), fg=WHITE, bg=BLACK)
title.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0, padx=10, pady=10)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=YELLOW, bg=BLACK)
check_mark.grid(row=3, column=1)

window.mainloop()