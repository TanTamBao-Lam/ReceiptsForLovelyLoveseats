# Lovely love seat description and price.
lovely_loveseat_description = ("Lovely Loveseat. Turfed polyester blend on "
                               "wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white")
lovely_loveseat_price = 254.00

# Stylish Settee description and price
stylish_settee_description = ("Stylish Settee. Faux leather or birch. "
                              "29.50 inches high x 54.75 inches wide x 28 inches deep. Black.")
stylish_settee_price = 180.50

# Luxurious lamp description and price.
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"
luxurious_lamp_price = 52.15

# Sales tax.
sales_tax = .88

# Customer 1
customer_one_total = 0
customer_one_itemization = ""

# Customer 1 purchases Lovely loveseat
customer_one_itemization += lovely_loveseat_description
customer_one_total += lovely_loveseat_price

# Customer 1 also purchases luxurious lamp
customer_one_itemization += "\n"
customer_one_itemization += luxurious_lamp_description
customer_one_total += luxurious_lamp_price

# Tax amount and grand total of customer 1's order.
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Print receipt - List of items - Total
print("Customer One Items: ")
print(customer_one_itemization + "\n")
print("Customer One Total: ")
print(customer_one_total)

