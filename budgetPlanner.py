import tkinter as tk
from tkinter import *
from tkinter import ttk
from sharedFunctions import frames

def budgetPlanner(root):
    frames(root)

    createFileButton = tk.Button(root, text="Create an Excel File", font=('Times New Roman', 16), bg='gray85', command=lambda: createFile(root))
    createFileButton.place(x=50, y=200, height=200, width=350)

    editFileButton = tk.Button(root, text="Edit or Manage Files", font=('Times New Roman', 16), bg='gray85', command=lambda: editFile(root))
    editFileButton.place(x=425, y=200, height=200, width=350)

    noFileButton = tk.Button(root, text="Use Without a File", font=('Times New Roman', 16),bg='gray85', command=lambda: noFile(root))
    noFileButton.place(x=800, y=200, height=200, width=350)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), bg='gray85', command=lambda: mainScreen())
    backButton.place(x=1050, y=600, height=50, width=100)

    def createFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def editFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)

    def noFile():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: budgetPlanner(root))
        returnButton.place(x=1050, y=600, height=50, width=100)