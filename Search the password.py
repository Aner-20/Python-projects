from tkinter import *   # (07/03/2022) - (08/03/2022)
import pyperclip        # 10/03/2022

def update(info):                     # password_store = info (07/03/2022)
    password_list.delete(0, END)
    for web_site in info:                 # add the sites to the list, it works even with dictionaries (07/03/2022)
        password_list.insert(END, web_site)

def copy():
# (10/03/2022)

    chosen_site = search_bar.get()

    for web_site in password_store:
        if chosen_site == web_site:
            chosen_password = password_store[chosen_site]
            pyperclip.copy(chosen_password)           # (10/03/2022) pyperclip.copy is useful to print only the value(password) linked to the key(web site) and cancel the previous password copied


def delete():
    search_bar.delete(0, END)

def fillin(event):
    search_bar.delete(0, END)
    search_bar.insert(0, password_list.get(ACTIVE))

def display(event):

    written = search_bar.get()
    if written == "":
        info = password_store       # update(info) is quite important to make sure that the function works properly (07/03/2022)

    else:
        info = []
        for web_site in password_store:
            if written.lower() in web_site.lower():
                info.append(web_site)

    update(info)

window = Tk()
window.title("Search the password")
window.geometry("600x500")

header = Label(window, text="Please enter here the site to pick the password", font=("Work Sans", 18))
header.pack(pady=20)

search_bar = Entry(window, font=("Work Sans", 18), width=30)
search_bar.pack(pady=20)

password_list = Listbox(window, width=50)
password_list.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=10)

copy_button = Button(button_frame, text="Copy", font=("Helvetica", 20), command=copy)
copy_button.grid(row=0, column=0, padx=20)

delete_button = Button(button_frame, text="Delete", font=("Helvetica", 20), command=delete)
delete_button.grid(row=0, column=1, padx=20)

password_store = {'Delphi': '6cd+tJ9/',
                  'Economia': 'j784.FsyzùF§-f,GO)[p',
                   'Gmail': 'Ag-400/j500',
                   'Spid': 'xxj.akSJT.,^8Dz',
                   'Steam': '36912-15-30-90-(abc=2000)-"df950"',
                   'Amazon': 'uEF#5V36v-!3bBz',
                    'Wind': 'Md100-f230-e500',
                    'Gmail-2': 'Ap-200/r400',
                     'Reddit': 'wL|iMQ2ù3k5b@)x2è[J0',
                     'Real Python': '*T5@Q=°ùù8UawPèb-)^/',
                      'Cesare Pozzo': 'M50-l100/d25',
                      'Randstad': 'G?;Gè7ZTCp-?I8x$29iS6d;l',
                       'Gmail_mamma': 'T1Pd-Nu;',
                        'Zeiss_mamma': '?|nMuy$é;3Lg',
                        'Giappichelli':'N|;9g§|&lKUrn7',
                        'ZapSplat': 'wlx}JqT!a1à',
                        'Fondo Priamo': 'b%Y6ww_F+E5qNKQ',
                         'Ford': 'q*C!d89xVTWy!QM',
                         'Font awesome':'z-N*$BAFq$A',
                         'Teams': 'kimAAhnxXeS2B.J',
                          'SQL': 'My6-|àkn:}6U',
                          'Ikea': 'sU])|K2wwZ8Y',
                          'Nimbus': '-aZ^,R°6kU@=',
                           'Gmail-Davide': 'W120.kopl',
                            'Microsoft': 'pyfkyz-Gygkev-1varhi',
                            'Gigroup': '2awFQMc9oe-E',
                            'WAM': '-B%mRC2%pCh?7RA',
                            'Webex': '/0wYzit;/Dg&',
                            'Euroclub': 'J300o1200',
                            'App password': 'enxfoaqgajifjhcq',
                            'Github': 'S@t7RzqUPRzeWQL',
                            'Web dev Simplified': 'T55ap9H7QUcNcSH',
                            'Heroku': 'Mkh.%,XQ5gf7^cU',
                            'Linkedin': 'E#*2Q+CyktLC(xu',
                            'Leetcode': '395Ts4C4iFQTJ*f',
                             'Bethesda': 'P6RyN!vmjZwn6Nw',
                              'Amazon': '%-Tw3Zd4AznDLJc',
                              'ADP': 'dsbFTT467BQeR$c',
                               'Mc': 'N4JH?hvgQQLtbxY',
                                'Starbucks': 'BeYs.2@@nQnf6N7',
                                'Synergie': '9b(^A[6C:&§pJ7bXSV',
                                 'ADP(mamma)': 'BeYs.2@@nQnf6N7',
                                 'Spid(mamma)': '/0wYzit;/Dg&',
                                 'Codice(posteid mamma)': 'Kl1234'}

update(password_store)


password_list.bind("<<ListboxSelect>>", fillin)
search_bar.bind("<KeyRelease>", display)



window.mainloop()