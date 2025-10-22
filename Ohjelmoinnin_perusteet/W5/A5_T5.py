def insertWord():
    Sana = input("Insert word: ")
    return Sana

def showWord(pWord):
    print(f"Current word: -\"{pWord}\"")
    return None

def reverseshowWord(pWord):
    ReverseWord = pWord[::-1]
    print(f"Word reversed: -{ReverseWord}")
    return None

def print_menu():
    print("Options:")
    print("1. - Insert word")
    print("2. - Show current word")
    print("3. - Show current word in reverse")
    print("0. - Exit")

def main():
    word = ""
    print("Program starting.")
    
    while True:
        print_menu()
        
        choice = input("Your choice: ")
        
        if choice == '1':
            word = insertWord()
            
        elif choice == '2':
            showWord(word)
            
        elif choice == '3':
            reverseshowWord(word)
            
        elif choice == '0':
            print("Exiting program.")
            print("Program ending.")
            break
            
        else:
            print("Unknown option")
            
        print()

main()