# Descriptions and prices of items in the furniture store

# Description and price of the Lovely Loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Description and price of the Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Description and price of the Luxurious Lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales tax rate
sales_tax = 0.088  # 8.8% tax

# Customer one's shopping details

# Initializing total cost for customer one
customer_one_total = 0

# Initializing a string to store item descriptions for customer one
customer_one_itemization = ""

# Adding the price of the Lovely Loveseat to the total cost
customer_one_total += lovely_loveseat_price

# Adding the description of the Lovely Loveseat to the item list
customer_one_itemization += lovely_loveseat_description

# Adding the price of the Luxurious Lamp to the total cost
customer_one_total += luxurious_lamp_price

# Adding the description of the Luxurious Lamp to the item list
customer_one_itemization += luxurious_lamp_description

# Calculating the sales tax for customer one's total
customer_one_tax = customer_one_total * sales_tax

# Adding the tax to customer one's total cost
customer_one_total += customer_one_tax

# Printing the final itemization and total for customer one
print("Customer One Items:", customer_one_itemization)
print("Customer One Total:", customer_one_total)
