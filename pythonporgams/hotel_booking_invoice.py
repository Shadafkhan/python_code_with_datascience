"""11. Hotel Booking Invoice

Take:

Guest Name
Room Rent/Day
Number of Days
Food Charges
Laundry Charges
GST %

Generate the final invoice."""

username = input("Enter guest full name: ")
roomrent = float(input("Enter room rent per day: "))
numofdays = int(input("Enter number of days stayed: "))
foodcharges = float(input("Enter food charges: "))
laundrycharges = float(input("Enter laundry charges: "))
gst = float(input("Enter GST (%): "))

room_cost = roomrent * numofdays
subtotal = room_cost + foodcharges + laundrycharges
gst_amount = subtotal * gst / 100
final_price = subtotal + gst_amount

print("\n----- HOTEL BOOKING INVOICE -----")
print("Guest Name:", username)
print("Room Cost:", room_cost)
print("Food Charges:", foodcharges)
print("Laundry Charges:", laundrycharges)
print("Subtotal:", subtotal)
print("GST Amount:", gst_amount)
print("Final Bill:", final_price)