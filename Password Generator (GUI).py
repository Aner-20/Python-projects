from tkinter import *
from random import randint   # another way to use randint, without import randint it would be random.randint()


window = Tk()
window.title("A good Password Generator")
window.geometry("450x320")
icon = PhotoImage(file="Pw.png")
window.iconphoto(True, icon)


def new_random():
    password_entry.delete(0, END)
    password_length = int(my_entry.get())   # get password length and convert to integer
    new_pw = ''                             # create a variable to hold the password
    for x in range(password_length):
        new_pw += chr(randint(1,144))

        password_entry.insert(0,new_pw)    # output password to the screen


# Copy to clipboard
def clip():
    window.clipboard_clear()    # clear the clipboard
    window.clipboard_append(password_entry.get())   # copy to clipboard





# Label Frame
label = LabelFrame(window, text="How many characters?")
label.pack(pady=22)

# Creating an entry box to assign number of characters
my_entry = Entry(label, font=("Arial", 25))
my_entry.pack(pady=15, padx=15)

# Create entry box for the returned password
password_entry = Entry(window, text="", font=("Arial", 22), bd=0, bg="systembuttonface") # systembuttonface makes the background invisible, but visible when the user generate a new password
password_entry.pack(pady=22)

# Create a frame for the buttons
my_frame = Frame(window)
my_frame.pack(pady=20)

# Create the buttons
button_1 = Button(my_frame, text="Generate Good Password", command=new_random)
button_1.grid(row=0, column=0, padx=12)

clip_button = Button(my_frame, text="Copy to clipboard", command=clip)
clip_button.grid(row=0, column=1, padx=12)



window.mainloop()