import tkinter as tk
from tkinter import *
from tkinter import ttk


def savingsTracker(root):
    for widget in root.winfo_children():
        widget.destroy()
