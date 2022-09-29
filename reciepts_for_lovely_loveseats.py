#Lovely Love Seat
lovely_loveseat_description = "Loveley Loveseat. Tufed polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#Stylish Sattee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inchecs high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#Luxurious Lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#Sales Tax = 8.8%
sales_tax = 0.088

#Customer one
customer_one_total = 0

#list of descriptions customer is purchasing
customer_one_itemization = ""

#customer one purchases
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + " " + luxurious_lamp_description

#customer one taxes
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#print totals
print("Customer one Total:")
print("Total cost: $", f"{customer_one_total:,.2f}")
print("-------------------------------------------")
print("Itemization: ", customer_one_itemization)


