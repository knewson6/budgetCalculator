import tkinter as tk
from tkinter import *
from tkinter import ttk


def taxCalculator(root):
    frames(root)

    noticeLabel = tk.Label(root, text="Please Input All Numbers On A Monthly Basis", font=('Times New Roman', 18), bg='white')
    noticeLabel.place(x=350, y=120, height=25, width=500)

    provinces = StringVar(root)
    provinces.set("Pick a Province or Territory")
    provinceMenu = OptionMenu(root, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
    provinceMenu.place(x=125, y=175, height=50, width=225)
    userProvince = provinces.get()

    monthlyIncomeLabel = tk.Label(root, text="Monthly Income \n\t\t $", font=('Times New Roman', 18), bg='white')
    monthlyIncomeLabel.place(x=75, y=250)
    monthlyIncome = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    monthlyIncome.place(x=300, y=275)
    userMonthlyIncome = monthlyIncome.get("1.0", END).strip()

    rrspContributionLabel = tk.Label(root, text="RRSP Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    rrspContributionLabel.place(x=75, y=325)
    rrspContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    rrspContribution.place(x=300, y=350)
    userRRSPcontribution = rrspContribution.get("1.0", END).strip()

    fhsaContributionLabel = tk.Label(root, text="FHSA Contribution \n\t\t $", font=('Times New Roman', 18), bg='white')
    fhsaContributionLabel.place(x=75, y=400)
    fhsaContribution = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    fhsaContribution.place(x=300, y=425)
    userFHSAcontribution = fhsaContribution.get("1.0", END).strip()

    capitolGainsLabel = tk.Label(root, text="Realised Capitol Gains \n\t\t $", font=('Times New Roman', 18), bg='white')
    capitolGainsLabel.place(x=75, y=475)
    capitolGains = tk.Text(root, height=1, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
    capitolGains.place(x=300, y=500)
    userCapitolGains = capitolGains.get("1.0", END).strip()

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    return userProvince, userMonthlyIncome, userRRSPcontribution, userFHSAcontribution, userCapitolGains