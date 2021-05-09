from tkinter import *
import time
import math
duration = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text= "Timer")
    global duration
    duration = 0

def start_timer():
    global duration
    duration += 1
    if duration % 8 == 0:
        title_label.config(text="Break")
        count_down(20 * 60)
    elif duration % 2 == 0:
        title_label.config(text="Break")
        count_down(5 * 60)
    else :
        title_label.config(text="Work")
        count_down(25 *60)
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro Timer")
window.config( padx=80, pady = 80, bg = "#a8dadc")
title_label = Label(text = "Timer", fg = "#f4a261", bg = "#a8dadc", font=("Roboto", 50))
title_label.grid(column = 1 , row = 0)
canvas = Canvas(width= 200, height = 224, bg="#a8dadc", highlightthickness=0)
tomato_photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_photo)
timer_text = canvas.create_text(100, 140, text='00:00', fill="white", font=("Poppins", 32, "bold"))
canvas.grid(column=1, row=1)

start= Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
