import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ..sharedFunctions import frames, backButton

def taxCalc(root, mainScreen):
    calculatorFrame = frames(root)

    provinces = StringVar(calculatorFrame)
    provinces.set("Pick a Province or Territory")
    provinceMenu = OptionMenu(calculatorFrame, provinces ,"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Northwest Territories",
                              "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon")
    provinceMenu.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=5, sticky="nsew")
    provinceMenu.config(font=("Times New Roman", 16))
    provinceMenu["menu"].config(font=("Times New Roman", 16))

    payPeriod = StringVar(calculatorFrame)
    payPeriod.set("Pay Period")
    payPeriodMenu = OptionMenu(calculatorFrame, payPeriod, "Daily" ,"Weekly", "Bi-Weekly", "Bi-Monthly", "Monthly", "Annually")
    payPeriodMenu.grid(row=0, column=2, rowspan=2, columnspan=2, padx=10, pady=5, sticky="nsew")
    payPeriodMenu.config(font=("Times New Roman", 16))
    payPeriodMenu["menu"].config(font=("Times New Roman", 16))

    inputLabels = [
        "Income",
        "RRSP Contribution",
        "FHSA Income",
        "Capitol Gains"
    ]

    for i, (text) in enumerate(inputLabels):
        rowNumber = 2 + (i * 2)
        label = tk.Label(calculatorFrame, text=text, font=("Times New Roman", 24), bg="white")
        label.grid(row=rowNumber, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")

    entries = []
    for i, text in enumerate(inputLabels):
        rowNumber = 2 + (i * 2)
        entry = tk.Entry(calculatorFrame, font=("Times New Roman", 24), highlightbackground="black", highlightcolor="black", highlightthickness="2")
        entry.grid(row=rowNumber, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        entries.append(entry)

    outputLabels = [
        "Take Home Pay",
        "Gross Income",
        "Provincial Taxes",
        "Federal Taxes",
        "CPP Contributions",
        "EI Contributions",
        "FHSA Deductions",
        "RRSP Deductions"
    ]

    for i, (text) in enumerate(outputLabels):
        rowNumber = i + 2
        label = tk.Label(calculatorFrame, text=text, font=("Times New Roman", 16), bg="white")
        label.grid(row=rowNumber, column=2, padx=10, pady=5, sticky="nsew")

    outputValues = []
    for i, text in enumerate(outputLabels):
        rowNumber = i + 2
        valueLabel = tk.Label(calculatorFrame, text="$ 0.00", font=("Times New Roman", 16), bg="White")
        valueLabel.grid(row=rowNumber, column=3, padx=10, pady=5, sticky="nsew")
        outputValues.append(valueLabel)

    calculateButton = tk.Button(calculatorFrame, text="Calculate!", font=('Times New Roman', 20), command=lambda: calculate())
    calculateButton.grid(row=12, column=1, rowspan=2, columnspan=2, sticky="nsew")

    for i in range(16):
        calculatorFrame.rowconfigure(i, weight=1, uniform="row")
    for j in range(4):
        calculatorFrame.columnconfigure(j, weight=1, uniform="col")

    backButton(calculatorFrame, lambda: mainScreen(root))

    def calculate():

        userProvince = provinces.get()
        if userProvince == "Pick a Province or Territory":
            messagebox.showerror("Input Error", "Please select a province.")
            return

        userPayPeriod = payPeriod.get()
        if userPayPeriod == "Pay Period":
            messagebox.showerror("Input Error", "Please select a pay period")
            return

        try:
            userIncome = float(entries[0].get().replace(",", "").strip() or 0)
            userRRSPcontribution = float(entries[1].get().replace(",", "").strip() or 0)
            userFHSAcontribution = float(entries[2].get().replace(",", "").strip() or 0)
            userCapitalGains = float(entries[3].get().replace(",", "").strip() or 0)
        except ValueError:
            messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
            return

        if userPayPeriod == "Daily":
            userAnnualIncome = userIncome * 260
            rrspDeduction = min((userRRSPcontribution * 260), (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min((userFHSAcontribution * 260), 8000)

        elif userPayPeriod == "Weekly":
            userAnnualIncome = userIncome * 52
            rrspDeduction = min((userRRSPcontribution * 52), (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min((userFHSAcontribution * 52), 8000)

        elif userPayPeriod == "Bi-Weekly":
            userAnnualIncome = userIncome * 26
            rrspDeduction = min((userRRSPcontribution * 26), (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min((userFHSAcontribution * 26), 8000)

        elif userPayPeriod == "Bi-Monthly":
            userAnnualIncome = userIncome * 24
            rrspDeduction = min((userRRSPcontribution * 24), (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min((userFHSAcontribution * 24), 8000)

        elif userPayPeriod == "Monthly":
            userAnnualIncome = userIncome * 12
            rrspDeduction = min((userRRSPcontribution * 12), (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min((userFHSAcontribution * 12), 8000)

        elif userPayPeriod == "Annually":
            userAnnualIncome = userIncome
            rrspDeduction = min(userRRSPcontribution, (userAnnualIncome * 0.18), 31560)
            fhsaDeduction = min(userFHSAcontribution, 8000)

        income = userAnnualIncome + userCapitalGains - rrspDeduction - fhsaDeduction

        federalTaxInfo = {
            "brackets" : [57375, 114750, 177882, 253414],
            "rates" : [0.145, 0.205, 0.26, 0.29, 0.33]
        }

        provincialTaxInfo = {
            "Alberta" : {
                "brackets": [60000, 151234, 181481, 241974, 362961],
                "rates": [0.08, 0.10, 0.12, 0.13, 0.14, 0.15]
            },

            "British Columbia" : {
                "brackets" : [49279, 98560, 113158, 137407, 186306, 259829],
                "rates" : [0.0506, 0.077, 0.105, 0.1229, 0.147, 0.168, 0.205]
            },

            "Manitoba" :{
                "brackets" : [47564, 101200],
                "rates" : [0.108, 0.1275, 0.174]
            },

            "New Brunswick" : {
                "brackets" : [51306, 102614, 190060],
                "rates" : [0.094, 0.14, 0.16, 0.195]
            },

            "Newfoundland and Labrador" : {
                "brackets" : [44192, 88382, 157792, 220910, 282214, 564429, 1128858],
                "rates" : [0.087, 0.145, 0.158, 0.178, 0.198, 0.208, 0.213, 0.218]
            },

            "Nova Scotia" : {
                "brackets"  :[30507, 61015, 95883, 154650],
                "rates" : [0.0879, 0.1495, 0.1667, 0.175, 0.21]
            },

            "Northwest Territories" : {
                "brackets" : [51964, 103930, 168967],
                "rates" : [0.059, 0.086, 0.122, 0.1405]
            },

            "Nunavut" : {
                "brackets" : [54707, 109413, 177881],
                "rates" : [0.04, 0.07, 0.09, 0.115]
            },

            "Ontario" : {
                "brackets" : [52886, 105775, 150000, 220000],
                "rates" : [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]
            },

            "Prince Edward Island" : {
                "brackets" : [33328, 64656, 105000, 140000],
                "rates" : [0.095, 0.1347, 0.166, 0.1762, 0.19]
            },

            "Quebec" : {
                "brackets"  :[53225, 106495, 129590],
                "rates" : [0.14, 0.19, 0.24, 0.2575]
            },

            "Saskatchewan" : {
                "brackets" : [53462, 152750],
                "rates" : [0.105, 0.125, 0.145]
            },

            "Yukon" : {
                "brackets" : [57375, 114750, 177882, 500000],
                "rates" : [0.064, 0.09, 0.109, 0.128, 0.15]
            }
        }

        userProvinceInfo = provincialTaxInfo[userProvince]
        provincialTax = calculateTax(income, userProvinceInfo["brackets"], userProvinceInfo["rates"])
        federalTax = calculateTax(income, federalTaxInfo["brackets"], federalTaxInfo["rates"])

        if income <=67800:
            cppContribution = income * 0.0491
        else:
            cppContribution = 3500

        if income <= 65700:
            eiContribution = income * 0.0167
        else:
            eiContribution = 1077.48

        takeHome = income - federalTax - provincialTax - cppContribution - eiContribution


        userValues = [
            takeHome,
            userAnnualIncome,
            provincialTax,
            federalTax,
            cppContribution,
            eiContribution,
            fhsaDeduction,
            rrspDeduction
        ]
        for k in range(len(outputValues)):
            outputValues[k].config(text=f"$ {userValues[k]:.2f}")

        return

def calculateTax(income, taxBracket, taxRate):

    tax = 0
    previousBracket = 0

    for i in range(len(taxBracket)):
        if income > taxBracket[i]:
            tax += (taxBracket[i] - previousBracket) * taxRate[i]
            previousBracket = taxBracket[i]
        else:
            tax += (income - previousBracket) * taxRate[i]
            return tax

    tax += (income - previousBracket) * taxRate[-1]
    return tax
