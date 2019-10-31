#usury.py
#Thomas Marshall

#My program will calculate the monthly payments, the total payments, and the total
#interest payments of a loan.

#The inputs are principal, interest, and months. The outputs are monthly payments,
#total amount paid, and total interest paid.

#Certification of Authenticity
    #I certify that this lab is entirely my own work.


def monthlyPayments():
    #Shows the user what the program will do
    print("This program will allow you to enter your initial payments, your interesr")
    print("rates, and months into a calculator and it will give you your monthly payments,")
    print("your total payment, and your interest payments back.")
    
    #This will allow the user to enter their loan amount.
    principal = eval(input("\nEnter your initial amount: "))

    #This will allow the user to enter their interest percentage
    interest = eval(input("Enter your interest rate: "))

    #This will allow the user to enter how many months their loan is scheduled to be paid
    #off in
    months = eval(input("Enter how many months are remaining: "))

    #This will calculate the interest rate from the interest percentage
    rate = interest / 1200

    #This will calculate how much they paid each month
    monthlyPayment = (principal*(rate*((1+rate)**(months))))/((1+rate)**(months) - 1)

    #This will calculate how much they paid in total
    totalPayment = monthlyPayment * months

    #This will calculate how much they paid in just interest
    totalInterest = totalPayment - principal

    #This will tell the user how much they paid each month
    print("Monthly payments =", monthlyPayment)

    #This will tell the user how much they paid in total
    print("Total amount paid =", totalPayment)

    #This will tell the user how much they paid in just interest
    print("Total interest paid =", totalInterest)
