'''
Fuel Expense Calculator

Take:

Vehicle Name
Petrol Price/Litre
Mileage
Distance

Calculate:

Fuel Required
Fuel Cost
Cost per Kilometer
'''

vehicle_name = str(input('Enter vehicle name:'))
petrol = float(input('Enter price per litre:'))
mileage = float(input('Enter mileage of your vehicle:'))
distance =float(input('Enter distance you want to travel :'))

fuel_required = distance/mileage
fuel_cost = fuel_required * petrol
cost_per_kilometer = fuel_cost/distance

print("\n------ Fuel Cost Report ------")
print("Vehicle Name        :", vehicle_name)
print("Fuel Required       :", fuel_required, "litres")
print("Fuel Cost           :", fuel_cost)
print("Cost Per Kilometer  :", cost_per_kilometer)