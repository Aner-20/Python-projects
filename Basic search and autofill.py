from tkinter import *

def update(data):
    my_list.delete(0, END)
    # add foods to listbox
    for item in data:
        my_list.insert(END, item)

# update entry box with listbox clicked
def fillout(event):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ACTIVE))

def check(event):
    # grab what was typed
    typed = my_entry.get()
    if typed == "":
        data = foods
    else:
        data = []
        for item in foods:
            if typed.lower() in item.lower():
                data.append(item)

    # update the listbox with selected items
    update(data)

window = Tk()
window.title("Basic search and autofill")
window.geometry("500x320")

my_label = Label(window, text="Typing...", font=("Helvetica", 15), fg="grey")
my_label.pack(pady=20)
my_entry = Entry(window, font=("Helvetica", 20),width=25, justify="left")
my_entry.pack()

my_list = Listbox(window, width=50)
my_list.pack(pady=20)

foods = ["Pepperoni", "Peppers", "Mushrooms", "Garlic", "Onion", "French Fries", "Artichokes",
         "Marrows", "Taco", "Cheese", "Pasta", "Spelt", "Barley", "Honey", "Ham", "Bacon", "Lobster", "Trout", "Beef"]

update(foods)

my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>", check)
window.mainloop()