from tkinter import *          # 24/04/2022
from tkinter import messagebox
import pygame

audio_add = 'add.mp3'
audio_reduce = 'reduce.mp3'
audio_clear = 'clear.mp3'

BACKGROUND_COLOR = "#721515"
FOREGROUND_COLOR = "#B2BEC3"
LIFE_POINTS = 8000
changed_lp = 8000

def decrease():
    global LIFE_POINTS
    global changed_lp
    global audio_reduce
    if lp_box.get().isdigit():
        amount = int(lp_box.get())
        changed_lp -= amount
        life_points.config(text=changed_lp)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_reduce)
        pygame.mixer.music.play()

    elif not lp_box.get().isdigit():
        lp_box.delete(0,END)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_reduce)
        pygame.mixer.music.play()
        messagebox.showerror("Error", "Type a number")

def increase():
    global LIFE_POINTS
    global changed_lp
    global audio_add
    if lp_box.get().isdigit():
        amount = int(lp_box.get())
        changed_lp += amount
        life_points.config(text=changed_lp)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_add)
        pygame.mixer.music.play()

    elif not lp_box.get().isdigit():
        lp_box.delete(0,END)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_add)
        pygame.mixer.music.play()
        messagebox.showerror("Error", "Type a number")


def reset_key(event):
    global amount
    global changed_lp
    global audio_clear
    changed_lp = 8000
    lp_box.delete(0, END)
    life_points.config(text=changed_lp)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_clear)
    pygame.mixer.music.play()



def clear_button():
    global amount
    global changed_lp
    global audio_clear
    changed_lp = 8000
    lp_box.delete(0, END)
    life_points.config(text=changed_lp)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_clear)
    pygame.mixer.music.play()

window = Tk()
window.title("LIfe points calculator")
window.geometry("330x280")
window.resizable(False, False)
window.config(bg=BACKGROUND_COLOR)

life_points_label = Label(text="Life points", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=("Georgia", 30))
life_points_label.pack(pady=15)


life_points = Label(text=LIFE_POINTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=("Georgia", 30))
life_points.pack(pady=10)

increase_decrease_frame = Frame(window, bg=BACKGROUND_COLOR)
increase_decrease_frame.pack(pady=10)

decrease_button = Button(increase_decrease_frame, text="-", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR,
                         font=("Georgia", 20), activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR,
                         width=2, command=decrease)
decrease_button.grid(row=0, column=0)


lp_box = Entry(increase_decrease_frame, bg=FOREGROUND_COLOR, fg=BACKGROUND_COLOR, font=("Georgia", 18), width=5,)
lp_box.grid(row=0, column=1, padx=20)

increase_button = Button(increase_decrease_frame, text="+", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR,
                         font=("Georgia", 20), activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_COLOR,
                         width=2, command=increase)
increase_button.grid(row=0, column=2)


reset_button = Button(increase_decrease_frame, text="Reset", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR,
                      font=("Georgia", 15), activeforeground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                      command=clear_button)
reset_button.grid(row=1, column=1)

window.bind("<Return>", lambda event: reset_key("Return"))   # window.bind is quite important
#window.bind("<Return>", clear_button)   #another way to bind the key(in this case)

window.mainloop()