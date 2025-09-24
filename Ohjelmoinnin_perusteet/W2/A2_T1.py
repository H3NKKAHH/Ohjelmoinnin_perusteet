# Make a Python program, which prompts the user name and two floating numbers.
# Multiply the inserted numbers to get product. Round the product in two decimal precision. Complete the program output as shown below.

print("Program starting.")

Name = input("What is your name: ")

First_number = input("Enter a floating point number: ")

First_number = float(First_number)

Second_number = input("Enter second floating point number: ")

Second_number = float(Second_number)

print(f"{Name} you gave numbers {First_number} and { Second_number}")

Multi = First_number * Second_number

print(f"Multiplying first and second number will result in product {round(Multi, 2)}")
print("Program ending.")