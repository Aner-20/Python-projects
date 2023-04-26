from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def lock():

    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("Warning", "You didn't fill out all the fields")
    else:
        # Disable entry boxes

        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        # to enable to the 2nd tab
        my_notebook.tab(1, state="normal")
        # change tab field
        amount_label.config(text=f"Amount of {home_entry.get()} to convert to {converted_entry.get()}")
        converted_label.config(text=f"Equals This many {conversion_entry.get()}")
        convert_button.config(text=f"Convert from {home_entry.get()}")



def unlock():
    # Enable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")

    # Disable tab
    my_notebook.tab(1, state="disabled")

def convert():
    # Delete converted entry box
    converted_entry.delete(0, END)

    # Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())

    # Convert to two decimals
    conversion = round(conversion, 2)

    # Add commas
    conversion = "{:,}".format(conversion)

    # Update entry box
    converted_entry.insert(0, conversion)



def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


window = Tk()
window.title("Currency Converter")
window.geometry("500x500")

my_notebook = ttk.Notebook(window)
my_notebook.pack(pady=5)

currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)
currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")


# disable 2nd tab
my_notebook.tab(1, state="disabled")


# Currency tab #


home = LabelFrame(currency_frame, text="Your currency", labelanchor="n")
home.pack(pady=20)

home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion currency", labelanchor="n")
conversion.pack(pady=20)

# Convert to label
conversion_label = Label(conversion, text="Currency to convert to...",)
conversion_label.pack(pady=10)

# Convert to entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)


# rate label
rate_label = Label(conversion, text="Current Conversion Rate... ")
rate_label.pack(pady=10)

# Rate to entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# Button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create Buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

#############################


# Convert tab #

amount_label = LabelFrame(conversion_frame, text="Amount to convert",labelanchor="n")
amount_label.pack(pady=20)

# Entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)


# Equal Frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency", labelanchor="n")
converted_label.pack(pady=20, padx=10)

# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# clear button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=2)

# Fake label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()


window.mainloop()