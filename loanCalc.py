import tkinter as tk
from tkinter import *
from tkinter import ttk

def loanCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()