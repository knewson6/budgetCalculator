import tkinter as tk
from tkinter import *
from tkinter import ttk
from sharedFunctions import frames

def budgetPlanner(root, mainScreen):
    frames(root)

    createFileButton = tk.Button(root, text="Create an Excel File", font=('Times New Roman', 16), bg='gray85', command=lambda: createFile())
    createFileButton.place(x=50, y=200, height=200, width=350)

    editFileButton = tk.Button(root, text="Edit or Manage Files", font=('Times New Roman', 16), bg='gray85', command=lambda: editFile())
    editFileButton.place(x=425, y=200, height=200, width=350)

    noFileButton = tk.Button(root, text="Use Without a File", font=('Times New Roman', 16),bg='gray85', command=lambda: noFile())
    noFileButton.place(x=800, y=200, height=200, width=350)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), bg='gray85', command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    def createFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def editFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def noFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)