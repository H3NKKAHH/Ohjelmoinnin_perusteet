# Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”

# 1. Print info message “Calculate fuel consumtion.”
# 2. Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
# 3. Convert the Feed into an integer and assign it to Distance variable
# 4. Ask “Enter fuel usage(liters): ”
# 5. Convert the Feed into an integer and assign it to FuelUsage variable
# 6. Calculate the Consumption for 100 km
# 7. Convert the Consumption back to an integer
# 8. Print “Fuel consumption is {Consumption} l per 100 km”

print("Calculate fuel consumption.")

Feed = input("Enter travel distance (kilometers): ")

Distance = int(Feed)

Feed = input("Enter fuel usage (liters): ")

FuelUsage = int(Feed)

Consumption = (int(FuelUsage) / int(Distance)) * 100

Consumption = int(Consumption)

print("Fuel consumption is ",Consumption,"l per 100 km")

