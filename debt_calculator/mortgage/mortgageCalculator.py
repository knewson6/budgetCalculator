import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Format the mortgage calculator into .grid() instead of .place()

def mortgageCalc(root, mainScreen, frames, backButton, loanScreen, loanCalc, mortgageCalc):
        mortFrame = frames(root)

        # Row 0: House Amount and Interest Rate
        houseAmountLabel = tk.Label(mortFrame, text="House Amount:", font=('Times New Roman', 20), bg='white', anchor="e")
        houseAmountLabel.grid(row=0, column=0, padx=(50, 5), pady=30, sticky="e")

        houseAmount = tk.Entry(mortFrame, font=('Times New Roman', 20), highlightbackground='black', highlightcolor='black', highlightthickness='2', width=15)
        houseAmount.grid(row=0, column=1, padx=(0, 2), pady=30, sticky="w")

        houseAmountCurrency = tk.Label(mortFrame, text="$", font=('Times New Roman', 20), bg='white')
        houseAmountCurrency.grid(row=0, column=1, padx=(0, 50), pady=30, sticky="e")

        interestRateLabel = tk.Label(mortFrame, text="Interest Rate:", font=('Times New Roman', 20), bg='white', anchor="e")
        interestRateLabel.grid(row=0, column=2, padx=(50, 5), pady=30, sticky="e")

        interestRate = tk.Entry(mortFrame, font=('Times New Roman', 20), highlightbackground='black', highlightcolor='black', highlightthickness='2', width=10)
        interestRate.grid(row=0, column=3, padx=(0, 2), pady=30, sticky="w")

        interestRateCurrency = tk.Label(mortFrame, text="%", font=('Times New Roman', 20), bg='white')
        interestRateCurrency.grid(row=0, column=3, padx=(0, 50), pady=30, sticky="e")

        options = []

        # fix the layout of the following
        # it does not look good at all


        # Option 1
        downPaymentLabel1 = tk.Label(mortFrame, text="Down Payment:", font=('Times New Roman', 16), bg='white', justify="left")
        downPaymentLabel1.grid(row=1, column=0, padx=25, pady=(15, 5), sticky="w")

        percentLabel1 = tk.Label(mortFrame, text="%", font=('Times New Roman', 16), bg='white')
        percentLabel1.grid(row=2, column=0, padx=(25, 2), pady=5, sticky="e")
        downPaymentPercent1 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent1.grid(row=2, column=1, padx=(2, 10), pady=5, sticky="w")

        dollarLabel1 = tk.Label(mortFrame, text="$", font=('Times New Roman', 16), bg='white')
        dollarLabel1.grid(row=3, column=0, padx=(25, 2), pady=5, sticky="e")
        downPaymentValue1 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue1.grid(row=3, column=1, padx=(2, 10), pady=5, sticky="w")

        amortizationPeriod1 = StringVar(mortFrame)
        amortizationPeriod1.set("Amortization Period")
        amortizationPeriodMenu1 = OptionMenu(mortFrame, amortizationPeriod1, *[f"{y} Years" for y in range(1, 31)])
        amortizationPeriodMenu1.grid(row=4, column=0, padx=25, pady=5, sticky="ew")

        paymentFrequency1 = StringVar(mortFrame)
        paymentFrequency1.set("Payment Frequency")
        paymentFrequencyMenu1 = OptionMenu(mortFrame, paymentFrequency1, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu1.grid(row=5, column=0, padx=25, pady=5, sticky="ew")

        totalAmountLabel1 = tk.Label(mortFrame, text="Total Amount: $ 0.00", font=('Times New Roman', 18), bg='white')
        totalAmountLabel1.grid(row=6, column=0, padx=25, pady=5)

        insuranceLabel1 = tk.Label(mortFrame, text="Insurance: $ 0.00", font=('Times New Roman', 18), bg='white')
        insuranceLabel1.grid(row=7, column=0, padx=25, pady=5)

        paymentLabel1 = tk.Label(mortFrame, text="Payment: $ 0.00", font=('Times New Roman', 20), bg='white')
        paymentLabel1.grid(row=8, column=0, padx=25, pady=5)

        options.append({"downPaymentPercent": downPaymentPercent1, "downPaymentValue": downPaymentValue1, "amortizationPeriod": amortizationPeriod1, "paymentFrequency": paymentFrequency1,
                        "totalAmountLabel": totalAmountLabel1, "insuranceLabel": insuranceLabel1, "paymentLabel": paymentLabel1})


        # Option 2
        downPaymentLabel2 = tk.Label(mortFrame, text="Down Payment:", font=('Times New Roman', 16), bg='white', justify="left")
        downPaymentLabel2.grid(row=1, column=1, padx=25, pady=(15, 5), sticky="w")

        percentLabel2 = tk.Label(mortFrame, text="%", font=('Times New Roman', 16), bg='white')
        percentLabel2.grid(row=2, column=1, padx=(25, 2), pady=5, sticky="e")
        downPaymentPercent2 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent2.grid(row=2, column=2, padx=(2, 10), pady=5, sticky="w")

        dollarLabel2 = tk.Label(mortFrame, text="$", font=('Times New Roman', 16), bg='white')
        dollarLabel2.grid(row=3, column=1, padx=(25, 2), pady=5, sticky="e")
        downPaymentValue2 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue2.grid(row=3, column=2, padx=(2, 10), pady=5, sticky="w")

        amortizationPeriod2 = StringVar(mortFrame)
        amortizationPeriod2.set("Amortization Period")
        amortizationPeriodMenu2 = OptionMenu(mortFrame, amortizationPeriod2, *[f"{y} Years" for y in range(1, 31)])
        amortizationPeriodMenu2.grid(row=4, column=1, columnspan=2, padx=25, pady=5, sticky="ew")

        paymentFrequency2 = StringVar(mortFrame)
        paymentFrequency2.set("Payment Frequency")
        paymentFrequencyMenu2 = OptionMenu(mortFrame, paymentFrequency2, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu2.grid(row=5, column=1, columnspan=2, padx=25, pady=5, sticky="ew")

        totalAmountLabel2 = tk.Label(mortFrame, text="Total Amount: $ 0.00", font=('Times New Roman', 18), bg='white')
        totalAmountLabel2.grid(row=6, column=1, columnspan=2, padx=25, pady=5)

        insuranceLabel2 = tk.Label(mortFrame, text="Insurance: $ 0.00", font=('Times New Roman', 18), bg='white')
        insuranceLabel2.grid(row=7, column=1, columnspan=2, padx=25, pady=5)

        paymentLabel2 = tk.Label(mortFrame, text="Payment: $ 0.00", font=('Times New Roman', 20), bg='white')
        paymentLabel2.grid(row=8, column=1, columnspan=2, padx=25, pady=5)

        options.append({"downPaymentPercent": downPaymentPercent2, "downPaymentValue": downPaymentValue2, "amortizationPeriod": amortizationPeriod2, "paymentFrequency": paymentFrequency2,
                        "totalAmountLabel": totalAmountLabel2, "insuranceLabel": insuranceLabel2, "paymentLabel": paymentLabel2})


        # Option 3
        downPaymentLabel3 = tk.Label(mortFrame, text="Down Payment:", font=('Times New Roman', 16), bg='white', justify="left")
        downPaymentLabel3.grid(row=1, column=3, padx=25, pady=(15, 5), sticky="w")

        percentLabel3 = tk.Label(mortFrame, text="%", font=('Times New Roman', 16), bg='white')
        percentLabel3.grid(row=2, column=3, padx=(25, 2), pady=5, sticky="e")
        downPaymentPercent3 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent3.grid(row=2, column=4, padx=(2, 10), pady=5, sticky="w")

        dollarLabel3 = tk.Label(mortFrame, text="$", font=('Times New Roman', 16), bg='white')
        dollarLabel3.grid(row=3, column=3, padx=(25, 2), pady=5, sticky="e")
        downPaymentValue3 = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue3.grid(row=3, column=4, padx=(2, 10), pady=5, sticky="w")

        amortizationPeriod3 = StringVar(mortFrame)
        amortizationPeriod3.set("Amortization Period")
        amortizationPeriodMenu3 = OptionMenu(mortFrame, amortizationPeriod3, *[f"{y} Years" for y in range(1, 31)])
        amortizationPeriodMenu3.grid(row=4, column=3, padx=25, pady=5, sticky="ew")

        paymentFrequency3 = StringVar(mortFrame)
        paymentFrequency3.set("Payment Frequency")
        paymentFrequencyMenu3 = OptionMenu(mortFrame, paymentFrequency3, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu3.grid(row=5, column=3, padx=25, pady=5, sticky="ew")

        totalAmountLabel3 = tk.Label(mortFrame, text="Total Amount: $ 0.00", font=('Times New Roman', 18), bg='white')
        totalAmountLabel3.grid(row=6, column=3, padx=25, pady=5)

        insuranceLabel3 = tk.Label(mortFrame, text="Insurance: $ 0.00", font=('Times New Roman', 18), bg='white')
        insuranceLabel3.grid(row=7, column=3, padx=25, pady=5)

        paymentLabel3 = tk.Label(mortFrame, text="Payment: $ 0.00", font=('Times New Roman', 20), bg='white')
        paymentLabel3.grid(row=8, column=3, padx=25, pady=5)

        options.append({"downPaymentPercent": downPaymentPercent3, "downPaymentValue": downPaymentValue3, "amortizationPeriod": amortizationPeriod3, "paymentFrequency": paymentFrequency3,
                        "totalAmountLabel": totalAmountLabel3, "insuranceLabel": insuranceLabel3, "paymentLabel": paymentLabel3})

        calculateButton = tk.Button(mortFrame, text="Calculate", font=('Times New Roman', 20), command=lambda: calculate())
        calculateButton.grid(row=9, column=0, columnspan=4, padx=25, pady=30, sticky="ew")

        backButton(mortFrame, lambda: loanScreen(root, mainScreen, frames, backButton, loanCalc, mortgageCalc))

        def calculate():
            try:
                userHouseAmount = float(houseAmount.get().replace(",", "").strip() or 0)
                userInterestRate = float(interestRate.get().strip() or 0)
            except ValueError:
                messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
                return

            userInterestRate = userInterestRate / 100

            for i, opt in enumerate(options, start=1):
                try:
                    userDownPaymentPercent = float(opt["downPaymentPercent"].get().replace(",", "").strip() or 0)
                    userDownPaymentValue = float(opt["downPaymentValue"].get().replace(",", "").strip() or 0)
                except valueError:
                    messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
                    continue

                if userDownPaymentPercent == 0 and userDownPaymentValue >0:
                    userMortgageAmount = userHouseAmount - userDownPaymentValue
                    userDownPaymentPercent = userDownPaymentValue / userMortgageAmount
                else:
                    userDownPaymentPercent = userDownPaymentPercent / 100
                    userDownPaymentValue = userHouseAmount * userDownPaymentPercent
                    userMortgageAmount = userHouseAmount - userDownPaymentValue

                if userDownPaymentPercent == 0 and userDownPaymentValue == 0:
                    messagebox.showerror('Input Error', f'Error: Please Enter a down payment amount or percent for option {i}')

                userAmortizationPeriod = opt["amortizationPeriod"].get()
                if  userAmortizationPeriod == "Amortization Period":
                    messagebox.showerror('Input Error', f'Error: Please Enter a Amortization Period for option {i}')
                    return
                userAmortizationPeriod = int(userAmortizationPeriod.split()[0])

                userPaymentFrequency = opt["paymentFrequency"].get()
                if userPaymentFrequency == "Payment Frequency":
                    messagebox.showerror('Input Error', f'Error: Please Enter a Payment Frequency for option {i}')
                    return

                if userPaymentFrequency == "Weekly":
                    interestRatePeriods = 52
                elif userPaymentFrequency == "Monthly":
                    interestRatePeriods = 12
                elif userPaymentFrequency == "Annually":
                    interestRatePeriods = 1

                if userHouseAmount < 1500000 and userDownPaymentPercent < 0.2:
                    if 0.05 <= userDownPaymentPercent < 0.1:
                        cmhcInsurance = (userMortgageAmount * 0.04)
                    elif 0.1 <= userDownPaymentPercent < 0.15:
                        cmhcInsurance = (userMortgageAmount * 0.031)
                    elif 0.15 <= userDownPaymentPercent < 0.2:
                        cmhcInsurance = (userMortgageAmount * 0.028)
                    else:
                        cmhcInsurance = 0
                else:
                    cmhcInsurance = 0

                r = userInterestRate / interestRatePeriods
                n = interestRatePeriods * userAmortizationPeriod
                totalMortgageAmount = userMortgageAmount + cmhcInsurance
                userPayment = (totalMortgageAmount * r) / (1 - ((1 + r) ** -n))

                opt["totalAmountLabel"].config(text=f"Total Amount: $ {userMortgageAmount + cmhcInsurance:.2f}")
                opt["insuranceLabel"].config(text=f"Insurance: $ {cmhcInsurance:.2f}")
                opt["paymentLabel"].config(text=f"Payment: $ {userPayment:.2f}")