###############################################################
# # Task: A10_T2
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import sys
import math

def read_values(PFilename: str) -> list[int] | None:

    values = []
    try:
        
        with open(PFilename, 'r') as file:
            for line in file:
                clean_line = line.strip() 
                if clean_line:
                    try:
                        values.append(int(clean_line))
                    except ValueError:
                        
                        pass
    except FileNotFoundError:
       
        print(f"Error: Tiedostoa '{PFilename}' ei löydy.")
        sys.exit(1) 
    
    return values

def sumOfValues(PValues: list[int]) -> int:

    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:

    if not PValues:
        return 0 
    
    
    result = 1
    for number in PValues:
        result *= number
    return result
    



def main() -> None:

    
    print("Program starting.")
    filename = input("Insert filename: ")

    
    values = read_values(filename)
    
    if values is None:
        
        print("Program ending.")
        return

    
    total_sum = sumOfValues(values)

    
    total_product = productOfValues(values)


    print(f"\n# --- Sum of numbers --- #")
    print(total_sum)
    print(f"# --- Sum of numbers --- #\n")

    
    print(f"# --- Product of numbers --- #")
    print(total_product)
    print(f"# --- Product of numbers --- #")



    print("")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()