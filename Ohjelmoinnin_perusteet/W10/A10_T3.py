###############################################################
# # Task: A10_T3
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import sys
import copy 


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

def BubbleSort(PValues: list[int], PAsc: bool = True) -> None:

    n = len(PValues)
    
    
    for i in range(n - 1):

        for j in range(n - i - 1):
            

            
            should_swap = False
            
            if PAsc:
                
                if PValues[j] > PValues[j+1]:
                    should_swap = True
            else:
                
                if PValues[j] < PValues[j+1]:
                    should_swap = True
            
            if should_swap:
                
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]


def display_sorted_results(filename: str, raw_data: list[int], sorted_asc: list[int], sorted_desc: list[int]) -> None:

    
    raw_str = ", ".join(map(str, raw_data))
    asc_str = ", ".join(map(str, sorted_asc))
    desc_str = ", ".join(map(str, sorted_desc))
    
    
    print(f"Raw '{filename}' -> {raw_str}")
    print(f"Ascending '{filename}' -> {asc_str}")
    print(f"Descending '{filename}' -> {desc_str}")


def main() -> None:

    print("Program starting.")

   
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
    else:
        
        filename = input("Insert filename: ")

    
    values = read_values(filename)
    
    if values is None:
        print("Program ending.")
        return

    
    raw_data = copy.deepcopy(values)
    asc_data = copy.deepcopy(values)
    desc_data = copy.deepcopy(values)

    
    BubbleSort(asc_data, PAsc=True)

    
    BubbleSort(desc_data, PAsc=False)

    
    display_sorted_results(filename, raw_data, asc_data, desc_data)

    print("Program ending.")


if __name__ == "__main__":
    main()