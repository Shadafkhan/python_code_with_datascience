'''
Supermarket Invoice System

Take details for 3 products.

Calculate:

Item totals
Grand Total
Discount
GST
Packing Charges
Final Bill
Print a supermarket invoice.

'''

# Supermarket Billing System

item_name1 = input("Enter name of Item 1: ")
price1 = float(input("Enter price of Item 1: "))
quantity1 = int(input("Enter quantity of Item 1: "))

item_name2 = input("Enter name of Item 2: ")
price2 = float(input("Enter price of Item 2: "))
quantity2 = int(input("Enter quantity of Item 2: "))

item_name3 = input("Enter name of Item 3: ")
price3 = float(input("Enter price of Item 3: "))
quantity3 = int(input("Enter quantity of Item 3: "))

# Calculate item totals
item_total1 = price1 * quantity1
item_total2 = price2 * quantity2
item_total3 = price3 * quantity3

# Grand Total
grand_total = item_total1 + item_total2 + item_total3

# Discount (10%)
discount = grand_total * (10 / 100)

# GST (3%)
gst = grand_total * (3 / 100)

# Packaging Charges
packaging_charges = 70

# Final Bill
final_bill = grand_total - discount + gst + packaging_charges

# Print Bill
print("\n======================================")
print("         SUPERMARKET BILL")
print("======================================")
print("Item\t\tPrice\tQty\tTotal")
print("--------------------------------------")
print(item_name1, "\t\t", price1, "\t", quantity1, "\t", item_total1)
print(item_name2, "\t\t", price2, "\t", quantity2, "\t", item_total2)
print(item_name3, "\t\t", price3, "\t", quantity3, "\t", item_total3)
print("--------------------------------------")
print("Grand Total       :", grand_total)
print("Discount (10%)    :", discount)
print("GST (3%)          :", gst)
print("Packaging Charges :", packaging_charges)
print("--------------------------------------")
print("Final Bill        :", final_bill)
print("======================================")

