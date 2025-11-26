####################################################################
# Task: A9_T3
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################
import sys

def ag_t3_file_exists():
    
    print("Program starting.")
    
    
    prompt = "Insert filename: "
    filename = input(prompt)
    
    
    
    
    try:
        
        with open(filename, 'r') as file:
            content = file.read()
            
            
            print(f"##.{filename}.##")
            print(content.strip())
            print(f"##.{filename}.##")
            
    except FileNotFoundError:
        
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)
    
   
    print("Program ending.")

if __name__ == "__main__":
    ag_t3_file_exists()