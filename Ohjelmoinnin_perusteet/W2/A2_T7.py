print("Program starting.")

Fahrenheit = float(input("Insert fahrenheits: "))

Celsius = (Fahrenheit - 32) / 1.8
Celsius_round = round(Celsius, 1)

print(f"{Fahrenheit}°F is {Celsius}°C")
print("Program ending.")