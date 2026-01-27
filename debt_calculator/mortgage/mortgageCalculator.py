import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sharedFunctions import frames, backButton

# Format the mortgage calculator

def mortgageCalc(root, mainScreen):
        from loanScreen import loan_screen

        mortFrame = frames(root)

        houseAmountLabel = tk.Label(mortFrame, text="House Amount:" + "$".rjust(8), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        houseAmountLabel.place(x=125, y=125)
        houseAmount = tk.Entry(mortFrame, width=15, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        houseAmount.place(x=375, y=128)

        interestRateLabel = tk.Label(mortFrame, text="Interest Rate:" + "%".rjust(4), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        interestRateLabel.place(x=700, y=125)
        interestRate = tk.Entry(mortFrame, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        interestRate.place(x=900, y=128)

        options = []

        for i, x in enumerate([75, 425, 785]):
            downPaymentLabel = tk.Label(mortFrame, text="Down Payment:" + "%".rjust(4) + "\n" + "$".rjust(31), font=('Times New Roman', 16), bg='white', width=50, anchor="w", justify="left")
            downPaymentLabel.place(x=x, y=200)

            downPaymentPercent = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
            downPaymentPercent.place(x=x+175, y=200)

            downPaymentValue = tk.Entry(mortFrame, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
            downPaymentValue.place(x=x+175, y=225)

            amortizationPeriod = StringVar(mortFrame)
            amortizationPeriod.set("Amortization Period")
            amortizationPeriodMenu = OptionMenu(mortFrame, amortizationPeriod, *[f"{y} Years" for y in range(1, 31)])
            amortizationPeriodMenu.place(x=x+25, y=275, height=50, width=225)

            paymentFrequency = StringVar(mortFrame)
            paymentFrequency.set("Payment Frequency")
            paymentFrequencyMenu = OptionMenu(mortFrame, paymentFrequency, "Weekly", "Monthly", "Annually")
            paymentFrequencyMenu.place(x=x+25, y=325, height=50, width=225)

            totalAmountLabel = tk.Label(mortFrame, text="Total Amount: $ 0.00 ", font=('Times New Roman', 18), bg='white')
            totalAmountLabel.place(x=x, y=400)

            insuranceLabel = tk.Label(mortFrame, text="Insurance: $ 0.00 ", font=('Times New Roman', 18), bg='white')
            insuranceLabel.place(x=x, y=430)

            paymentLabel = tk.Label(mortFrame, text="Payment: $ 0.00 ", font=('Times New Roman', 20), bg='white')
            paymentLabel.place(x=x, y=475)

            options.append({"downPaymentPercent": downPaymentPercent, "downPaymentValue": downPaymentValue, "amortizationPeriod": amortizationPeriod, "paymentFrequency": paymentFrequency,
                            "totalAmountLabel": totalAmountLabel, "insuranceLabel": insuranceLabel, "paymentLabel": paymentLabel})

        calculateButton = tk.Button(mortFrame, text="Calculate", font=('Times New Roman', 20), command=lambda: calculate())
        calculateButton.place(x=375, y=550, height=50, width=370)

        backButton(mortFrame, lambda: loan_screen(root, mainScreen))

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