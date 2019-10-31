#Thomas Marshall
#traffic.py

def traffic():
    roads = eval(input("Enter the number of roads were surveyed: "))
    total = 0
    total2 = 0

    for i in range(roads):
        days = eval(input("\nEnter the number of days were surveyed on road: "))
        for j in range(days):
            cars = eval(input("\tEnter how many cars traveled: "))
            total = total + cars
            avg = total/days
            total2 = total2 + cars
            
        print("Average number of cars per day:", avg)
        total = 0

    avg2 = total2/roads 
        
    print("\nTotal number of vehicles traveled on all roads:", total2)
    print("Average number of vehicles per road:", avg2)
    

traffic()
    
