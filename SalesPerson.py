# Thomas Marshall
# SalesForce.py
#  Purpose - This program builds a class that gets a person's ID number, name
#  and list of sales made, set a person's name, add more sales to an individual, calculate
#  a person's total sales, decide if an individual's quota was met, and compare the total
#  sales of two sales people
# I certify this lab is my own work, but I discussed it with Nick Mancabelli.

# Class name
class SalesPerson:
    # Initializer
    def __init__(self, tag, name, salesList):
        # Declares the ID number the ID number
        self.tag = tag

        # Declares the sale person's the sales person's
        self.name = name

        # Declares the list of sales
        self.salesList = salesList

    # Function to get the person's name
    def getName(self):
        # Returns their name
        return self.name

    # Function to get the person's ID number
    def getID(self):
        # Returns their ID number
        return self.tag

    # Function to set the person's name
    def setName(self, name):
        # Returns their name
        self.name = name

    # Function to add another sale to the list of a person's sales
    def enterSale(self, aSale):
        # Adds another sale to the list of a person's sales
        self.salesList.append(aSale)

    # Function to add up a person's sales
    def totalSales(self):
        # Set up a sum
        total = 0
        # Range built to add all the sales
        for i in range(len(self.salesList)):
            # Adds each sale
            total += float(self.salesList[i])
        # Returns sale total
        return total
    
    # Function to get the person's list of sales
    def getSales(self):
        # Returns their sales list
        return self.salesList

    # A function to find out if the quota was met
    def metQuota(self, quota):
        # Returns if the quota was met
        return self.totalSales() >= quota

    # A function that compares two people's total sales
    def compareTo(self, otherPerson):
        # Person 1 total sales
        personTotal = self.totalSales()
        # Person 2 total sales
        otherPerson = otherPerson.totalSales()

        # Person 1 had more
        if personTotal > otherPerson:
            # Returns positive
            return 1
        # Person 2 had more
        elif personTotal < otherPerson:
            # Returns negative
            return -1
        # They had the same amount
        elif personTotal == otherPerson:
            # Returns 0
            return 0

    # String of info
    def __str__(self):
        # Returns ID number, name, and total sales
        return ("Sales Person:\n\tI.D. Number: " + str(self.tag) + "\n\tName: "
                + self.name + "\n\tTotal Sales: " + str(self.totalSales()))
