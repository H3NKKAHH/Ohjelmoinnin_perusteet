####################################################################
# Task: A9_T2
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################
import sys

def ag_t2_exit_codes():
    
    print("Program starting.")
    
    prompt = "Insert exit code (0-255): "
    exit_code_input = input(prompt)
    
    
    
    try:
        exit_code = int(exit_code_input)
        
        
        if 0 == exit_code:
            print("Clean exit")
            sys.exit(0)
        else:
            
            print("Error code")
            
            sys.exit(1)
            
    except ValueError:
       
        print("Error code")
        
        sys.exit(1)

if __name__ == "__main__":
    ag_t2_exit_codes()