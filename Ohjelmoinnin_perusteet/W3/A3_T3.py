print("Program starting.")

print("This is a program with simple menu, where you can choose which operation the program performs")

Name = input("Before the menu, please insert your name: ")
print("")

# Menu

print("Options:")
print("1 - Print welcome message")
print("0 - Exit")

Choice = int(input("Your choice: "))

if (Choice == 1):
    print(f"Welcome {Name}!")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option")

print("Program ending.")