# 1_name_app_tkinter.py
import tkinter as tk
from tkinter import messagebox

def clicked():
  messagebox.showinfo(
    '', f'あなたの名前は {entry_1.get()} です'
    )

root = tk.Tk()
root.geometry('250x120')
root.title('名前入力アプリ')

label_1 = tk.Label(root, text='名前を入力してください')
entry_1 = tk.Entry(root, width=20)
button_1 = tk.Button(root, text='Submit', command=clicked)
root.columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

label_1.grid(column=0, row=0, sticky='s')
entry_1.grid(column=0, row=1)
button_1.grid(column=0, row=2, sticky='n')

root.mainloop()