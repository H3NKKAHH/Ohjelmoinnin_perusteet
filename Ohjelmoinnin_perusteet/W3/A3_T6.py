print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:")
print("1 - Lenght")
print("2 - Weight")
print("0 - Exit")
Choice = int(input("Your choice: "))

if (Choice == 1):
    print("")
    print("Lenght options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice_Lenght = int(input("Your choice: "))
    if (Choice_Lenght == 1):
        Meters = float(input("Insert meters: "))
        Kilometers = Meters / 1000
        print(f"{Meters} m is {Kilometers} km")
    elif (Choice_Lenght == 2):
        Kilometers = float(input("Insert kilometers: "))
        Meters = Kilometers * 1000
        print(f"{Kilometers} km is {Meters} m")
    elif (Choice_Lenght == 0):
        print("Exiting...")
    else:
        print("Unknown option.")

if (Choice == 2):

    print("")
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice_Weight = float(input("Your choice: "))
    if (Choice_Weight == 1):
        Grams = float(input("Insert grams: "))
        Pounds = Grams * 453.59237
        print(f"{Grams} g is {round(Pounds,1)} lb")
    elif (Choice_Weight == 2):
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds / 453.59237
        print(f"{Pounds} lb is {round(Grams,1)} g")
    elif (Choice_Weight == 0):
        print("Exiting...")
    else:
        print("Unknown option.")



print("")
print("Program ending.")
    



