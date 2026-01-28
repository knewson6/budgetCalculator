import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# back button overlaps loan and mortgage, squish them vertically
# buttons do not even work atm

def loanScreen(root, mainScreen, frames, backButton, loanCalc, mortgageCalc):
    window = frames(root)

    mortgageButton = tk.Button(window, text="Mortgage", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: mortgageCalc(root, mainScreen, frames, backButton, loanScreen, loanCalc, mortgageCalc))
    mortgageButton.grid(row=0, column=0, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    loanButton = tk.Button(window, text="Loan", font=('Times New Roman', 32), height = 10, width = 22, command=lambda: loanCalc(root, mainScreen, frames, backButton, loanScreen, mortgageCalc))
    loanButton.grid(row=0, column=1, rowspan=1, columnspan=1, padx=15, pady=15, sticky="nsew")

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    backButton(window, lambda: mainScreen(root))