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

    buttonFrame = tk.Frame(root, bg='white')
    root.configure(bg='white')
    buttonFrame.pack(fill='both', expand=True, padx=25, pady=10)
    return buttonFrame

def backButton(parent, command, width=10, font=("Times New Roman", 16), xOffset=25, yOffset=25):
    returnButton = tk.Button(parent, text="Back", font=font, width=width, command=command)
    returnButton.place(relx=1.0, rely=1.0, anchor="se", x=-xOffset, y=-yOffset)
    return returnButton