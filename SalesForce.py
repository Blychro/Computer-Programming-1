# Thomas Marshall
# SalesForce.py
#  Purpose - This program builds a class that creates sales people's
#  information including ID number, name, and sales. It can analyze quotas,
#  add additional profiles, find the best sales person, and locate an
#  individual's information, based on their ID number.
# I certify this lab is my own work, but I discussed it with Nick Mancabelli.

# Import last class
from SalesPerson import SalesPerson

# Class name
class SalesForce:
    # Initializer
    def __init__(self):
        # Empty list to start us off
        self.list = []

    # Function that adds a profile
    def addData(self, fileName):
        # Opens the file
        file = open(fileName)

        # Reads each line
        for line in file:
            # Creates a list of pieces
            pieces = line.split()
            # Defines the ID number
            tag = pieces[0]
            # Defines the person's name
            name = str(pieces[1]) + " " + str(pieces[2])
            # Creates a list of sales
            salesList = pieces[3:]

            # Creates a new profile
            self.list.append(SalesPerson(tag, name, salesList))

    # Function that finds out if quotas were met
    def quotaReport(self, quota):
        # Goes through each person
        for person in self.list:
            # Defines a person's ID number
            tag = person.getID()
            # Defines a person's name
            name = person.getName()
            # Defines a person's total sales
            totalSales = person.totalSales()
            # Decides if a person's quota wsa met
            metQuota = person.metQuota(quota)
            # Message shown
            show = ("\tI.D. Number: " + str(tag) + "\n\tSales Person: " + name +
                    "\n\tTotal Sales: " +  str(totalSales))
            # If quota was met
            if metQuota == True:
                show += "\n\tQuota met\n"
            # If quota wasn't met
            else:
                show += "\n\tQuota not met\n"

            # Shows the results of each profile
            print(show)

    # Function that finds the top sales person
    def topSalesPerson(self):
        # Begins with the first choice
        topSales = self.list[0]
        # Goes through each person
        for person in self.list:
            # Calculates if the current person has more sales than the current
            # leader
            if (topSales.compareTo(person) == -1):
                topSales = person
        # Returns the best person     
        return topSales

    # Function finds a person's sales based on their ID number
    def individualSales(self, tag):
        # Set up if number is not found
        worker = -1
        # Goes through each person
        for person in self.list:
            # Sees if the person being searched for exists
            if person.getID() == str(tag):
                # Changes worker to set up the if statement
                worker = person
                
        # Decides if a person was found
        if worker == -1:
            # Statement if a person was not found
            print("Sales Person Not Found")      
        else:
            # Displays the list of sales and total sales of the searched sales
            # person
            print("\tSales made: " + str(worker.getSales()) +
                  "\n\tTotal Sales: " + str(worker.totalSales()))
