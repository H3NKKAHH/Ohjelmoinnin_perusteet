def showOptions():
    print("Options:")
    print("1. - Show count")
    print("2. - Increase count")
    print("3. - Reset count")
    print("0. - Exit")
    return None

def askChoice():
    
    choice = input("Your choice: ") 
    
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1
    
def main():
    count = 0
    print("Program starting.")
    
    while True:
        showOptions()
        user_choice = askChoice()
        
        if user_choice == 1:
            
            print(f"Current count - {count}") 
            
        elif user_choice == 2:
            count += 1
            print("Count increased!")
            
        elif user_choice == 3:
            count = 0
            print("Cleared count!")
            
        elif user_choice == 0:
            print("Exiting program.")
            print("Program ending.")
            break
            
        elif user_choice == -1:
            pass 

        else:
            print("Unknown option!")
            
if __name__ == "__main__":
    main()