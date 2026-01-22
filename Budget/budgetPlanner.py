import tkinter as tk
from tkinter import *
from tkinter import ttk
from sharedFunctions import frames, backButton

def budgetPlanner(root, mainScreen):
    buttonFrame = frames(root)

    buttons = [
        ("Create an Excel File", lambda: createFile()),
        ("Edit or Manage Files", lambda: editFile()),
        ("Use Without a File", lambda: noFile()),
    ]

    for index, (text, cmd) in enumerate(buttons):
        row, col = divmod(index, 3)
        button = tk.Button(buttonFrame, text=text, font=('Times New Roman', 18), bg='gray85', command=cmd if cmd else None)
        button.grid(row=row, column=col, padx=10, pady=25, sticky="nsew")

    buttonFrame.rowconfigure(0, weight=1, uniform="row")
    buttonFrame.rowconfigure(1, weight=1)
    for j in range(3):
        buttonFrame.columnconfigure(j, weight=1, uniform="col")

    backButton(buttonFrame, command=lambda: mainScreen(root))

    def createFile():
        createFileFrame = frames(root)

        backButton(buttonFrame, command=lambda: budgetPlanner(root, mainScreen))

    def editFile():
        editFileFrame = frames(root)

        backButton(buttonFrame, command=lambda: budgetPlanner(root, mainScreen))

    def noFile():
        noFileFrame = frames(root)

        backButton(buttonFrame, command=lambda: budgetPlanner(root, mainScreen))