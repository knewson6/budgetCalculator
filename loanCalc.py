import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sharedFunctions import frames

def loanCalculator(root, mainScreen):
    frames(root)

    mortgageButton = tk.Button(root, text="Mortgage", font=('Times New Roman', 32), command=lambda: mortgage())
    mortgageButton.place(x=75, y=150, height=300, width=500)

    loanButton = tk.Button(root, text="Loan", font=('Times New Roman', 32), command=lambda: loan())
    loanButton.place(x=625, y=150, height=300, width=500)

    backButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: mainScreen(root))
    backButton.place(x=1050, y=600, height=50, width=100)

    def mortgage():
        frames(root)

        mortgageAmountLabel = tk.Label(root, text="Mortgage Amount:" + "$".rjust(4), font=('Times New Roman', 20),
                                       bg='white', width=50, anchor="w", justify="left")
        mortgageAmountLabel.place(x=125, y=125)
        mortgageAmount = tk.Entry(root, width=15, font=('Times New Roman', 18), highlightbackground='black',
                                  highlightcolor='black', highlightthickness='2')
        mortgageAmount.place(x=375, y=128)

        interestRateLabel = tk.Label(root, text="Interest Rate:" + "%".rjust(4), font=('Times New Roman', 20),
                                     bg='white', width=50, anchor="w", justify="left")
        interestRateLabel.place(x=700, y=125)
        interestRate = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black',
                                highlightcolor='black', highlightthickness='2')
        interestRate.place(x=900, y=128)

        options = []

        for i, x in enumerate([75, 425, 785]):
            downPaymentLabel = tk.Label(root, text="Down Payment:" + "%".rjust(4) + "\n" + "$".rjust(31), font=('Times New Roman', 16), bg='white', width=50, anchor="w", justify="left")
            downPaymentLabel.place(x=x, y=200)

            downPaymentPercent = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
            downPaymentPercent.place(x=x+175, y=200)

            downPaymentValue = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
            downPaymentValue.place(x=x+175, y=225)

            amortizationPeriod = StringVar(root)
            amortizationPeriod.set("Amortization Period")
            amortizationPeriodMenu = OptionMenu(root, amortizationPeriod, *[f"{y} Years" for y in range(1, 31)])
            amortizationPeriodMenu.place(x=x+25, y=275, height=50, width=225)

            paymentFrequency = StringVar(root)
            paymentFrequency.set("Payment Frequency")
            paymentFrequencyMenu = OptionMenu(root, paymentFrequency, "Weekly", "Monthly", "Annually")
            paymentFrequencyMenu.place(x=x+25, y=325, height=50, width=225)

            totalAmountLabel = tk.Label(root, text="Total Amount: $ 0.00 ", font=('Times New Roman', 18), bg='white')
            totalAmountLabel.place(x=x, y=400)

            insuranceLabel = tk.Label(root, text="Insurance: $ 0.00 ", font=('Times New Roman', 18), bg='white')
            insuranceLabel.place(x=x, y=430)

            paymentLabel = tk.Label(root, text="Payment: $ 0.00 ", font=('Times New Roman', 20), bg='white')
            paymentLabel.place(x=x, y=475)

            options.append({"downPaymentPercent": downPaymentPercent, "downPaymentValue": downPaymentValue, "amortizationPeriod": amortizationPeriod, "paymentFrequency": paymentFrequency,
                            "totalAmountLabel": totalAmountLabel, "insuranceLabel": insuranceLabel, "paymentLabel": paymentLabel})

        calculateButton = tk.Button(root, text="Calculate", font=('Times New Roman', 20), command=lambda: calculate())
        calculateButton.place(x=375, y=550, height=50, width=370)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: loanCalculator(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)

        def calculate():

            try:
                userMortgageAmount = float(mortgageAmount.get().replace(",", "").replace(".", "", 1).strip() or 0)
                userInterestRate = float(interestRate.get().replace(",", "").replace(".", "", 1).strip() or 0)
            except ValueError:
                messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
                return

            for i, opt in enumerate(options, start=1):

                userDownPaymentPercent = float(opt["downPaymentPercent"].get().replace(",", "").replace(".", "", 1).strip() or 0)
                userDownPaymentValue = float(opt["downPaymentValue"].get().replace(",", "").replace(".", "", 1).strip() or 0)

                if userDownPaymentPercent == 0:
                    userDownPaymentPercent = userDownPaymentValue / userMortgageAmount
                else:
                    userDownPaymentPercent = userDownPaymentPercent / 100

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

            #calculate insurance
            if userMortgageAmount < 1500000:
                if 0.05 < userDownPaymentPercent < 0.1:
                    cmhcInsurance = (userMortgageAmount * 0.04)
                elif 0.1 < userDownPaymentPercent < 0.15:
                    cmhcInsurance = (userMortgageAmount * 0.031)
                elif 0.15 < userDownPaymentPercent < 0.2:
                    cmhcInsurance = (userMortgageAmount * 0.028)
                else:
                    cmhcInsurance = 0
            else:
                cmhcInsurance = 0

            totalMortgageAmount = userMortgageAmount + cmhcInsurance - userDownPaymentValue



            if userPaymentFrequency == "Weekly":
                r = userInterestRate / 100 / userAmortizationPeriod / 52
                n = 52 * userAmortizationPeriod
                userPayment = ((userMortgageAmount - userDownPaymentValue) * r) / (1 - ((1+r) ** -n))

            elif userPaymentFrequency == "Monthly":
                r = userInterestRate / 100 / userAmortizationPeriod / 12
                n = 12 * userAmortizationPeriod
                userPayment = ((userMortgageAmount - userDownPaymentValue) * r) / (1 - ((1+r) ** -n))

            elif userPaymentFrequency == "Yearly":
                r = userInterestRate / 100 / userAmortizationPeriod
                n = userAmortizationPeriod
                userPayment = ((userMortgageAmount - userDownPaymentValue) * r) / (1 - ((1+r) ** -n))

            opt["totalAmountLabel"].config(text=f"Total Amount: $ {totalMortgageAmount:.2f}")
            opt["insuranceLabel"].config(text=f"Insurance: $ {cmhcInsurance:.2f}")
            opt["paymentLabel"].config(text=f"Payment: $ {userPayment:.2f}")

    #only 3rd option is being calculated


    def loan():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: loanCalculator(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)