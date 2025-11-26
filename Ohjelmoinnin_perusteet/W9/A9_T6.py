####################################################################
# Task: A9_T6
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################

def saveLines(lines):
    prompt = "Insert filename: "
    filename = input(prompt)
    

    try:
        lines_with_newline = [line + '' for line in lines]
        with open(filename, 'w', encoding='UTF-8') as f:
            f.writelines(lines_with_newline)
        
    except Exception as e:
        print(f"Error while saving file: {e}")

def main():
    lines = []
    
    print("Program starting.")
    
    try:
        while True:
            
            print("Options:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            
            
            choice = input("Your choice: ")
            
            
            if choice == "1":
                
                text = input("Insert text: ")
                
                lines.append(text)
                
            elif choice == "2":
                
                if not lines:
                    print("No lines to save.")
                else:
                    saveLines(lines)
                    
            elif choice == "0":
                
                break
                
            else:
                
                print("Unknown option!")
                
    except KeyboardInterrupt:
        
        
        
        if not lines:
            
            print("Closing suddenly!")
            
        else:
            print("^Ckeyboard interrupt and unsaved progress!")
            save_prompt = input("Save before quit(y/n)?: ")
            
            
            if save_prompt.lower() == 'y':
                saveLines(lines)
            
            
            
    print("Program ending.")

if __name__ == "__main__":
    main()