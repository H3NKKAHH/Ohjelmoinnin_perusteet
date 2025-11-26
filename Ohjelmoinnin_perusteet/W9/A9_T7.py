####################################################################
# Task: A9_T7
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################

# OHJELMA KÄYNNISTYY TAPAAN "py A9_T7.py A9_T7_D2.txt A9_T7_F2.txt"

import sys
import os

ERROR_EXIT_CODE = -1

def show_synopsis():
    print("Usage: python A9_T7.py src_file.txt dst_file.txt")

def copy_file(src_file, dst_file):
    
    if not os.path.exists(src_file):
        print(f"Error! Source file \"{src_file}\" doesn't exist.")
        sys.exit(ERROR_EXIT_CODE)
        
    if os.path.exists(dst_file):
        overwrite_prompt = input(f"File '{dst_file}' exists. Overwrite (y/n)?: ")
        print(f" {overwrite_prompt}")
        
        if overwrite_prompt.lower() != 'y':
            print("Operation aborted by user.")
            sys.exit(ERROR_EXIT_CODE)
            
    try:
        with open(src_file, 'r', encoding='UTF-8') as f_in:
            content = f_in.readlines()
        
        with open(dst_file, 'w', encoding='UTF-8') as f_out:
            f_out.writelines(content)
            
        print(f"Copying file \"{src_file}\" to \"{dst_file}\".")
        
    except Exception as e:
        print(f"Error during file operation: {e}")
        sys.exit(ERROR_EXIT_CODE)

def main():
    
    
    if len(sys.argv) != 3:
        print("Error! Invalid amount of arguments.")
        show_synopsis()
        sys.exit(ERROR_EXIT_CODE)
    
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    print("Program starting.")
    print(f"Source file \"{src_file}\"")
    print(f"Destination file \"{dst_file}\"")
    
    copy_file(src_file, dst_file)
    
    print("Program ending.")
    sys.exit(0)

if __name__ == "__main__":

    main()
