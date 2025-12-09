###############################################################
# # Task: A10_T1
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import os

def read_data_from_file(filename):

    data_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                
                clean_line = line.strip()
                if clean_line:
                    
                    try:
                        data_list.append(int(clean_line))
                    except ValueError:

                        pass
    except FileNotFoundError:
        return None  
    return data_list

def display_data(data_list):

    if not data_list:
        return

    
    print("# --- Vertically --- #")
    for item in data_list:
        print(item)
    print("# --- Vertically --- #")

    
    print("# --- Horizontally --- #")
    
    horizontal_output = ", ".join(map(str, data_list))
    print(horizontal_output)
    print("# --- Horizontally --- #")


def main():

    print("Program starting.")

    
    filename = input("Insert filename: ")

    
    data = read_data_from_file(filename)
    
    
    if data is not None:
        display_data(data)
    else:
        
        print(f"Error: Could not read data from file '{filename}'.")

    print("Program ending.")


if __name__ == "__main__":
    main()