print("===========Grocery shop billing calculator===========")

sugar_quantity = float(input("Enter the quantity of sugar(in kg): "))
sugar_price_per_kg = 40.0 
sugar_total = sugar_quantity * sugar_price_per_kg

rice_quantity = float(input("Enter the quantity of rice(in kg): "))
rice_price_per_kg = 75.0
rice_total = rice_quantity * rice_price_per_kg

wheat_quantity = float(input("Enter the quantity of wheat(in kg): "))
wheat_price_per_kg = 100.0
wheat_total = wheat_quantity * wheat_price_per_kg

print("===========Billing details==========")
print("Total cost of sugar: Rs.",sugar_total)
print("Total cost of rice: Rs.",rice_total)
print("Total cost of wheat: Rs.",wheat_total)

Total_bill = sugar_total + rice_total + wheat_total
print("Total bill amount: Rs.",Total_bill)

discount = 0
if Total_bill >= 1000:
    discount = Total_bill * 0.10
    print("Discount applied: Rs",discount)

elif Total_bill >= 500:
    discount = Total_bill * 0.05
    print("Discount applied: Rs",discount)

else:
    print("No discount applied.") 


final_bill = Total_bill -  discount
print("Final bill amount: Rs. ",final_bill)

    