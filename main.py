import secrets
import pyperclip
import re
import tkinter as tk
from tkinter import ttk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

SIMPLE_PASSWORD_PATTERN = '^(?=.*?[a-z])(?=.*?[0-9])'
SPECIAL_CHARACTER_PATTERN = '(?=.*?[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]).*'
CAPITAL_CHARACTER_PATTERN = '(?=.*?[A-Z])'


def copy_password():
    pyperclip.copy(ent_password.get())


def generate_password():
    password_characters = ascii_lowercase + digits
    password_pattern = SIMPLE_PASSWORD_PATTERN
    if bv_special_characters.get():
        password_characters += punctuation
        password_pattern += SPECIAL_CHARACTER_PATTERN
    if bv_capital_alphabet.get():
        password_characters += ascii_uppercase
        password_pattern += CAPITAL_CHARACTER_PATTERN
    password_pattern += '.*$'
    new_password = ''.join(secrets.choice(password_characters) for _ in range(iv_password_length.get()))
    while not re.match(password_pattern, new_password):
        new_password = ''.join(secrets.choice(password_characters) for _ in range(iv_password_length.get()))
    ent_password.delete(0, tk.END)
    ent_password.insert(0, new_password)


root = tk.Tk()
root.title('Password generator')
root.minsize(width=275, height=155)
root.maxsize(width=-1, height=155)
root.geometry('275x150')
frm_main = ttk.Frame(root, padding=5, borderwidth=2, relief='solid')
frm_main.pack(expand=True, padx=10, pady=10, fill=tk.BOTH)

# special character CheckButton
bv_special_characters = tk.BooleanVar(value=False)
cb_special_characters = ttk.Checkbutton(frm_main, variable=bv_special_characters, text='Special Characters')
cb_special_characters.grid(column=0, row=1, sticky=tk.W)

# capital alphabet CheckButton
bv_capital_alphabet = tk.BooleanVar(value=False)
cb_capital_alphabet = ttk.Checkbutton(frm_main, variable=bv_capital_alphabet, text='Capital Alphabet')
cb_capital_alphabet.grid(column=0, row=2, sticky=tk.W)

# password output Entry
ent_password = ttk.Entry(frm_main)
ent_password.grid(column=0, row=3, sticky=tk.EW)
frm_main.columnconfigure(0, weight=1)

# password length OptionMenu
iv_password_length = tk.IntVar()
opt_length = ttk.OptionMenu(frm_main, iv_password_length, 16, *[length for length in range(16, 65)], )
opt_length.grid(column=0, row=0, sticky=tk.EW)

frm_btn_actions = ttk.Frame(master=frm_main, padding=5)
frm_btn_actions.grid(column=0, row=4, pady=5)

# generate password Button
btn_generate_password = ttk.Button(master=frm_btn_actions, text="Generate Password", command=generate_password)
btn_generate_password.grid(column=0, row=0)

# copy password button
btn_copy_password = ttk.Button(master=frm_btn_actions, text="Copy password", command=copy_password)
btn_copy_password.grid(column=1, row=0)
root.mainloop()
