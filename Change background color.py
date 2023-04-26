from tkinter import *
import random

def change_color():
    colors = ["red", "blue", "green", "yellow", "cyan", "purple", "orange", "gray", "aqua", "turquoise"]
    pick_color = random.choice(colors)
    window.config(bg=pick_color)
    change_button.config(bg=pick_color, activebackground=pick_color)

window = Tk()
window.title("Change background color")
window.geometry("400x300")
window.resizable(False, False)

change_button = Button(window, text="Click me!", font=("consolas", 20), command=change_color)
change_button.pack(pady=110)

window.mainloop()