
values = []

print("Program starting.")

while True:
    print("")
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    
    print("")
    choice = input("Your choice: ")
    
    if choice == "1":
        filename = input("Insert filename: ")
        print("")
        try:
            
            with open(filename, 'r') as file:
                values = [] 
                for line in file:
                    stripped_line = line.strip() 
                    if stripped_line != "":      
                        values.append(float(stripped_line)) 
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    elif choice == "2":
        
        count = len(values)
        print(f"Amount of values: {count}")

    elif choice == "3":
        
        total_sum = sum(values)
        print(f"Sum of values: {round(total_sum, 1)}")

    elif choice == "4":
        
        if len(values) > 0:
            avg = sum(values) / len(values)
            print(f"Average of values: {round(avg, 1)}")
        else:
            print("Average of values: 0.0") 

    elif choice == "0":
        print("Exiting program.")
        break

print("")
print("Program ending.")
