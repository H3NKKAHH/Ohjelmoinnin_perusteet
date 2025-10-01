# A3_T4 More menu options
# Extend the previous menu program by adding three more options to the menu.

# Options:

# Print the name backwards
# Your name backwards is "{NameBackwards}"
# Print the first character
# The first character in name "{Name}" is "{FirstChar}"
# Show the amount of characters in the name
# There are {NameLength} characters in the name "{Name}"
# run 1 run 2 run 3 run 4 run 5 run 6
# Program starting.
# This is a program with simple menu, where you can choose which operation the program performs.
# Before the menu, please insert your name: John

# Options:
# 1 - Print welcome message
# 2 - Print the name backwards
# 3 - Print the first character
# 4 - Show the amount of characters in the name
# 0 - Exit
# Your choice: 1
# Welcome John!

# Program ending.

print("Program starting.")

print("This is a program with simple menu, where you can choose which operation the program performs")

Name = input("Before the menu, please insert your name: ")
print("")

# Menu

print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

Choice = int(input("Your choice: "))
Reverse = Name[::-1]
First = Name[0]

if (Choice == 1):
    print(f"Welcome {Name}!")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option")
if (Choice == 2):
    print(f"Your name backwards is \"{Reverse}\"")
if (Choice == 3):
    print(f"The first character in name \"{Name}\" is \"{First}\"")
if (Choice == 4):
    print(f"There are {len(Name)} characters in the name \"{Name}\"")

print("Program ending.")