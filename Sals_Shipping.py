#@author Chewbacca625
#@version 9/30/2022

#This project is calculating the cost of Ground Shipping, Ground Shipping Premium, and drone shipping for Sal's Shipping company and it checks to see which one is the cheapest for a customer.

#Loops over user input and checks if the input is a floating point number
while True:
    try:
        weight = float(input("Enter the weight of your package in pounds: "))
        break
    #If the value is not a floating poing number a value error will occur, so it reprompts the user for a floating point number
    except ValueError:
        print("Please enter the weight of the package.")

#Calculates the cost of ground shipping based one the weight of package and adds a flat charge of 20
if weight <= 2:
    ground_ship_cost = (1.50 * weight) + 20
elif 2 < weight <= 6:
    ground_ship_cost = (3.00 * weight) + 20
elif 6 < weight <= 10:
    ground_ship_cost = (4.00 * weight) + 20
elif weight > 10:
    ground_ship_cost = (4.75 * weight) + 20    
    
#Ground Shipping Premium
ground_ship_premium = 125.00

#Calculates the cost of drone shipping based one the weight of package and with no flat charge
if weight <= 2:
    drone_ship_cost = (4.50 * weight)
elif 2 < weight <= 6:
    drone_ship_cost = (9.00 * weight)
elif 6 < weight <= 10:
    drone_ship_cost = (12.00 * weight)
elif weight > 10:
    drone_ship_cost = (14.25 * weight)
    
#Checks to see what shipping method is the cheapest for the customer 
if ground_ship_cost < drone_ship_cost:
    if ground_ship_cost < ground_ship_premium:
        print("Ground Shipping cost is the cheapest!")
    else:
        print("Ground Ship Premium is the cheapest!")
else:
    print("Drone Shipping is the cheapest!")

#prints the costs of all the shipping methods 
print("Ground shipping cost $", f"{ground_ship_cost:,.2f}")
print("Ground shipping premium cost $", f"{ground_ship_premium:,.2f}")
print("Drone shipping cost $", f"{drone_ship_cost:,.2f}")