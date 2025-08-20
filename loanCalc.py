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

        loanAmountLabel = tk.Label(root, text="Mortgage Amount:" + "$".rjust(4), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        loanAmountLabel.place(x=125, y=125)
        loanAmount = tk.Entry(root, width=15, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        loanAmount.place(x=375, y=128)

        interestRateLabel = tk.Label(root, text="Interest Rate:" + "%".rjust(4), font=('Times New Roman', 20), bg='white', width=50, anchor="w", justify="left")
        interestRateLabel.place(x=700, y=125)
        interestRate = tk.Entry(root, width=10, font=('Times New Roman', 18), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        interestRate.place(x=900, y=128)

        downPaymentPercentLabel1 = tk.Label(root, text="Down Payment:" + "%".rjust(4) + "\n" + "$".rjust(31), font=('Times New Roman', 16), bg='white', width=50, anchor="w", justify="left")
        downPaymentPercentLabel1.place(x=75, y=200)
        downPaymentPercent1 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent1.place(x=250, y=200)
        downPaymentValue1 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue1.place(x=250, y=225)

        downPaymentPercentLabel2 = tk.Label(root, text="Down Payment:" + "%".rjust(4) + "\n" + "$".rjust(31), font=('Times New Roman', 16), bg='white', width=50, anchor="w", justify="left")
        downPaymentPercentLabel2.place(x=425, y=200)
        downPaymentPercent2 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent2.place(x=600, y=200)
        downPaymentValue2 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue2.place(x=600, y=225)

        downPaymentPercentLabel3 = tk.Label(root, text="Down Payment:" + "%".rjust(4) + "\n" + "$".rjust(31), font=('Times New Roman', 16), bg='white', width=50, anchor="w", justify="left")
        downPaymentPercentLabel3.place(x=785, y=200)
        downPaymentPercent3 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentPercent3.place(x=960, y=200)
        downPaymentValue3 = tk.Entry(root, width=10, font=('Times New Roman', 16), highlightbackground='black', highlightcolor='black', highlightthickness='2')
        downPaymentValue3.place(x=960, y=225)

        amortizationPeriod1 = StringVar(root)
        amortizationPeriod1.set("Amortization Period")
        amortizationPeriodMenu1 = OptionMenu(root, amortizationPeriod1, "1 Year", "2 Years", "3 Years", "4 Years", "5 Years", "6 Years", "7 Years", "8 Years",
                                             "9 Years", "10 Years", "11 Years", "12 Years", "13 Years", "14 Years", "15 Years", "16 Years", "17 Years",
                                             "18 Years", "19 Years", "20 Years", "21 Years", "22 Years", "23 Years", "24 Years", "25 Years", "26 Years",
                                             "27 Years", "28 Years", "29 Years", "30 Years")
        amortizationPeriodMenu1.place(x=100, y=275, height=50, width=225)

        amortizationPeriod2 = StringVar(root)
        amortizationPeriod2.set("Amortization Period")
        amortizationPeriodMenu2 = OptionMenu(root, amortizationPeriod2, "1 Year", "2 Years", "3 Years", "4 Years", "5 Years", "6 Years", "7 Years", "8 Years",
                                             "9 Years", "10 Years", "11 Years", "12 Years", "13 Years", "14 Years", "15 Years", "16 Years", "17 Years",
                                             "18 Years", "19 Years", "20 Years", "21 Years", "22 Years", "23 Years", "24 Years", "25 Years", "26 Years",
                                             "27 Years", "28 Years", "29 Years", "30 Years")
        amortizationPeriodMenu2.place(x=460, y=275, height=50, width=225)

        amortizationPeriod3 = StringVar(root)
        amortizationPeriod3.set("Amortization Period")
        amortizationPeriodMenu3 = OptionMenu(root, amortizationPeriod3, "1 Year", "2 Years", "3 Years", "4 Years", "5 Years", "6 Years", "7 Years", "8 Years",
                                             "9 Years", "10 Years", "11 Years", "12 Years", "13 Years", "14 Years", "15 Years", "16 Years", "17 Years",
                                             "18 Years", "19 Years", "20 Years", "21 Years", "22 Years", "23 Years", "24 Years", "25 Years", "26 Years",
                                             "27 Years", "28 Years", "29 Years", "30 Years")
        amortizationPeriodMenu3.place(x=820, y=275, height=50, width=225)

        #payment frequency weekly, monthly and annually
        paymentFrequency1 = StringVar(root)
        paymentFrequency1.set("Payment Frequency")
        paymentFrequencyMenu1 = OptionMenu(root, paymentFrequency1, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu1.place(x=100, y=325, height=50, width=225)

        paymentFrequency2 = StringVar(root)
        paymentFrequency2.set("Payment Frequency")
        paymentFrequencyMenu2 = OptionMenu(root, paymentFrequency2, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu2.place(x=460, y=325, height=50, width=225)

        paymentFrequency3 = StringVar(root)
        paymentFrequency3.set("Payment Frequency")
        paymentFrequencyMenu3 = OptionMenu(root, paymentFrequency3, "Weekly", "Monthly", "Annually")
        paymentFrequencyMenu3.place(x=820, y=325, height=50, width=225)

        totalAmount1 = tk.Label(root, text="Total Amount: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        totalAmount1.place(x=75, y=400)

        totalAmount2 = tk.Label(root, text="Total Amount: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        totalAmount2.place(x=435, y=400)

        totalAmount3 = tk.Label(root, text="Total Amount: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        totalAmount3.place(x=795, y=400)

        insurance1 = tk.Label(root, text="Insurance: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        insurance1.place(x=78, y=430)

        insurance2 = tk.Label(root, text="Insurance: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        insurance2.place(x=438, y=430)

        insurance3 = tk.Label(root, text="Insurance: $ 0.00 ", font=('Times New Roman', 18), bg='white')
        insurance3.place(x=798, y=430)

        payment1 = tk.Label(root, text="Payment: $ 0.00 ", font=('Times New Roman', 20), bg='white')
        payment1.place(x=438, y=475)

        payment2 = tk.Label(root, text="Payment: $ 0.00 ", font=('Times New Roman', 20), bg='white')
        payment2.place(x=78, y=475)

        payment3 = tk.Label(root, text="Payment: $ 0.00 ", font=('Times New Roman', 20), bg='white')
        payment3.place(x=798, y=475)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: loanCalculator(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)

        def getUserInput():

            userAmortizationPeriod1 = amortizationPeriod1.get()
            if userAmortizationPeriod1 == "Amortization Period":
                messagebox.showerror("Input Error", "Please select an amortization period")
                return

            userAmortizationPeriod2 = amortizationPeriod2.get()
            if userAmortizationPeriod2 == "Amortization Period":
                messagebox.showerror("Input Error", "Please select an amortization period")
                return

            userAmortizationPeriod3 = amortizationPeriod3.get()
            if userAmortizationPeriod3 == "Amortization Period":
                messagebox.showerror("Input Error", "Please select an amortization period")
                return

            userPaymentFrequency1 = paymentFrequency1.get()
            if userPaymentFrequency1 == "Payment Frequency":
                messagebox.showerror("Input Error", "Please select a payment frequency")
                return

            userPaymentFrequency2 = paymentFrequency2.get()
            if userPaymentFrequency2 == "Payment Frequency":
                messagebox.showerror("Input Error", "Please select a payment frequency")
                return

            userPaymentFrequency3 = paymentFrequency3.get()
            if userPaymentFrequency3 == "Payment Frequency":
                messagebox.showerror("Input Error", "Please select a payment frequency")
                return

            try:
                userAmount = float(loanAmount.get().replace(",", "").replace(".", "", 1).strip() or 0)
                userInterestRate = float(interestRate.get().replace(",", "").replace(".", "", 1).strip() or 0)
                userDownPayment1 = float(downPaymentValue1.get().replace(",", "").replace(".", "", 1).strip() or 0)
                userDownPayment2 = float(downPaymentValue2.get().replace(",", "").replace(".", "", 1).strip() or 0)
                userDownPayment3 = float(downPaymentValue3.get().replace(",", "").replace(".", "", 1).strip() or 0)
            except ValueError:
                messagebox.showerror('Input Error', 'Error: Please Enter a Valid Number')
                return

    def loan():
        frames(root)

        returnButton = tk.Button(root, text="Back", font=('Times New Roman', 12), command=lambda: loanCalculator(root, mainScreen))
        returnButton.place(x=1050, y=600, height=50, width=100)