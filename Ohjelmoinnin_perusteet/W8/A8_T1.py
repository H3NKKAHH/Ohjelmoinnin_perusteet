import time 

pause_duration = 0

print("Program starting.")

while True:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    
    choice = input("Your choice: ")

    if choice == "1":
        pause_duration = float(input("Insert pause duration (s): "))
    
    elif choice == "2":
        print(f"Pausing for {pause_duration} seconds.")
        time.sleep(pause_duration)
        print("Unpaused.")
    
    elif choice == "0":
        print("Exiting program.")
        break

print("")
print("Program ending.")