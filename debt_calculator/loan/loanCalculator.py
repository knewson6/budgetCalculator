import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# need to make .grid()
# take from mortgage calculator and adapt to loan calculator

def loanCalc(root, mainScreen, frames, backButton, loanScreen, mortgageCalc, loanCalc):
        loanFrame = frames(root)

        backButton(loanFrame, lambda: loanScreen(root, mainScreen, frames, backButton, loanCalc, mortgageCalc))