print("Program starting.")

print("")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

Choice = float(input("Your choice: "))

if (Choice == 1):
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = (Celsius * 1.8) + 32 
    print(f"{Celsius} °C equals to {round(Fahrenheit,1)} °F\n")
if (Choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(f"{Fahrenheit} °F equals to {round(Celsius,1)} °C\n")
if (Choice == 0 ):
    print("Exiting...")
else:
    print("Unknown option.\n")

print("Program ending.")

