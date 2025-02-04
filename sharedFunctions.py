import tkinter as tk
from tkinter import *
from tkinter import ttk


def frames(root):
    for widget in root.winfo_children():
        widget.destroy()

    headFrame = tk.Frame(root, bg='gray75', width=1200, height=150)
    headFrame.pack(fill='x', side='top')
    headTitle = tk.Label(headFrame, text="Welcome To Your Financial Aid", font=('Times New Roman', 22), bg='gray75', fg='black')
    headTitle.pack(padx=0, pady=20)

    divider = ttk.Separator(root, orient='horizontal')
    divider.pack(fill='x')

    buttonFrame = tk.Frame(root, bg='white', width=1200, height=680)
    buttonFrame.pack(fill='x', side='bottom')