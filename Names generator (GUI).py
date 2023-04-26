from tkinter import *   # 20/04/2022 - 22/04/2022 - 23/04/2022
import names
from tkinter import messagebox
import pyperclip


window = Tk()
window.title("Names generator")
window.geometry("1200x400")
window.resizable(False,False)
title_label = Label(window, text="Generate some names",justify="center", font=("Arial", 20))
title_label.pack(pady=25)

def generate():
    names_store = []

    if (gender.get() == 1) and (type.get() == 1) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            rand_names = names.get_first_name(gender="male")

            names_store.append(rand_names)

        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete",fg="#192a56")


    elif (gender.get() == 1) and (type.get() == 3) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            rand_names = names.get_full_name(gender="male")

            names_store.append(rand_names)

        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete", fg="#192a56")

    elif (gender.get() == 2) and (type.get() == 1) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            rand_names = names.get_first_name(gender="female")

            names_store.append(rand_names)


        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete", fg="#1A0117")

    elif (gender.get() == 2) and (type.get() == 3) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            rand_names = names.get_full_name(gender="female")

            names_store.append(rand_names)

        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete", fg="#1A0117")

    elif (type.get() == 2) and (gender.get() == 1) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            name_1 = names.get_full_name()

            names_store.append(name_1)

        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete")

    elif (type.get() == 2) and (gender.get() == 2) and number_entry.get().isdigit():
        number_item = int(number_entry.get())
        for i in range(number_item):
            name_2 = names.get_full_name()

            names_store.append(name_2)

        for name in names_store:
            names_list.insert(END, name)

        title_label.config(text="Now you can copy or delete")

    else:
        number_entry.delete(0, END)
        messagebox.showwarning("Error", "That's not a number")


def copy():
    index = names_list.curselection()
    index_copy = names_list.get(index)
    pyperclip.copy(index_copy)

def delete():
    number_entry.delete(0, END)
    names_list.delete(0, END)
    if gender.get() == 1:
        title_label.config(text="You chose Male", fg="#192a56")

    elif gender.get() == 2:
        title_label.config(text="You chose Female", fg="#1A0117")



def pick_gender():
    if(gender.get() == 1):
        window.config(bg="#0fbcf9")
        left_frame.config(bg="#0fbcf9")
        right_frame.config(bg="#0fbcf9")
        gender_label.config(bg="#0fbcf9")
        title_label.config(bg="#0fbcf9")
        number_names.config(bg="#0fbcf9")
        first_name.config(bg="#0fbcf9", activebackground="#0fbcf9")
        last_name.config(bg="#0fbcf9", activebackground="#0fbcf9")
        full_name.config(bg="#0fbcf9", activebackground="#0fbcf9")
        kind_label.config(bg="#0fbcf9")
        male_radio.config(bg="#0fbcf9", activebackground="#0fbcf9")
        female_radio.config(bg="#0fbcf9", activebackground="#0fbcf9")
        title_label.config(text="You chose Male", fg="#192a56")

    elif(gender.get() == 2):
        window.config(bg="#fd79a8")
        left_frame.config(bg="#fd79a8")
        right_frame.config(bg="#fd79a8")
        gender_label.config(bg="#fd79a8")
        title_label.config(bg="#fd79a8")
        number_names.config(bg="#fd79a8")
        first_name.config(bg="#fd79a8", activebackground="#fd79a8")
        last_name.config(bg="#fd79a8", activebackground="#fd79a8")
        full_name.config(bg="#fd79a8", activebackground="#fd79a8")
        kind_label.config(bg="#fd79a8")
        male_radio.config(bg="#fd79a8", activebackground="#fd79a8")
        female_radio.config(bg="#fd79a8", activebackground="#fd79a8")
        title_label.config(text="You chose Female", fg="#1A0117")

def pick_kind():
    if(type.get() == 1):
        print("You chose First name")

    elif(type.get() == 2):
        print("You chose Last name")

    elif (type.get() == 3):
        print("You chose Full name")


# Left frame #

left_frame = Frame(window)
left_frame.pack(pady=20, side="left", fill="y", expand=0)

# ------------ #

# Gender label #

gender_label = Label(left_frame, text="Gender", font=("Arial", 15))
gender_label.grid(row=0, column=0, pady=10, padx=60)

# ------------ #

# Gender radio buttons #

gender = IntVar()

male_radio = Radiobutton(left_frame, text="Male", font=("Arial", 14), variable=gender, value=1,
                         fg="#394DC0", activeforeground="#394DC0", command=pick_gender)
male_radio.grid(row=1, column=0, pady=10, padx=70)

female_radio = Radiobutton(left_frame, text="Female", variable=gender, font=("Arial", 14), value=2,
                           fg="#C518B7", activeforeground="#C518B7", command=pick_gender)
female_radio.grid(row=2, column=0, pady=10, padx=90)


# ------------------ #

# Kind of name label #

kind_label = Label(left_frame, text="Kind", font=("Arial", 15))
kind_label.grid(row=0, column=1, pady=10, padx=60)

# -------------- #

# Kind of name radio buttons #

type = IntVar()

first_name = Radiobutton(left_frame, text="First name", font=("Arial", 14),
                         variable=type, value=1, command=pick_kind)
first_name.grid(row=1, column=1, pady=10, padx=50)

last_name = Radiobutton(left_frame, text="Last name", font=("Arial", 14),
                         variable=type, value=2, command=pick_kind)
last_name.grid(row=2, column=1, pady=10, padx=50)

full_name = Radiobutton(left_frame, text="Full name", font=("Arial", 14),
                         variable=type, value=3, command=pick_kind)
full_name.grid(row=3, column=1, pady=10, padx=50)

# -------------- #

# Number frame #

right_frame = Frame(window)
right_frame.pack(pady=30, side="left", fill="y", expand=1)

# -------------- #

# Number label #

number_names = Label(right_frame, text="Numbers of names", font=("Arial", 14))
number_names.grid(row=0)

# ------------------- #


# Number entry #

number_entry = Entry(right_frame, font=("Arial", 30), width=6)
number_entry.grid(row=1, pady=35)


# -------------- #

# Buttons #

generate_button = Button(window, text="Generate", font=("Arial", 14), command=generate)
generate_button.place(x=1000, y=100)

copy_button = Button(window, text="Copy", font=("Arial", 14), command=copy)
copy_button.place(x=1000, y=150)

delete_button = Button(window, text="Delete", font=("Arial", 14), command=delete)
delete_button.place(x=1000, y=200)

# -------- #


# List #

names_list = Listbox(window, width=33)
names_list.place(x=500, y=130)



# --------- #

window.mainloop()