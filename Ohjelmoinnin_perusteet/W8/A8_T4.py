import date_utils 

def main():
    timestamps = [] 
    
    print("Program starting.")
    
    
    filename = input("Insert filename: ")
    
    
    
    date_utils.readTimestamps(filename, timestamps)

    while True:
        print("Options:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            year = int(input("Insert year: "))
            count = date_utils.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}")
            
        elif choice == "2":
            month = input("Insert month: ")
            count = date_utils.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}")
            
        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = date_utils.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}")
            
        elif choice == "0":
            print("Exiting program.")
            break
            
        print() 

if __name__ == "__main__":
    main()
    print("Program ending.")