#Thomas Marshall
#The program will calculate RMS mean and harmonic mean of a list of numbers
#Inputs - amount of numbers and their values
#Outputs - The two different mean types
#I certify that this lab is entirely my own work.
from math import *

def mean():
    #Describe the programs purpose.
    print("This program will allow you to enter a list and be given the RMS average and")
    print("the harmonic mean of the list")

    #variables for later use
    total = 0
    total2 = 0

    #Number of variables in the list.
    l = eval(input("Enter how many numbers in your list: "))

    #This code calculates the different mean types
    for i in range(l):
        var = eval(input("Enter a variable: "))
        total = total + var**2
        total2 = total2 + (1/var)

    rms_average = sqrt(total/l)
    harmonic_mean = l/total2

    #Outputs
    print("RMS Average:", rms_average)
    print("Harmonic Mean:", harmonic_mean)
