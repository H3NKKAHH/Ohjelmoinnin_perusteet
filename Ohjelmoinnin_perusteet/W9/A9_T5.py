####################################################################
# Task: A9_T5
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################
import sys

RGB_MIN = 0
RGB_MAX = 255

def get_color_component(color_name):
    prompt = f"Insert {color_name}: "
    raw_input = input(prompt)
    
    
    try:
        value = int(raw_input)
        
        if RGB_MIN <= value <= RGB_MAX:
            return value
        else:
            print(f"Value \"{raw_input}\" is out of the range {RGB_MIN}-{RGB_MAX}.")
            raise Exception("Input out of range")
            
    except ValueError:
        print(f"\"{raw_input}\" is non-numeric value.")
        raise Exception("Invalid integer input")

def convert_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def main():
    print("Program starting.")
    
    try:
        r = get_color_component("red")
        g = get_color_component("green")
        b = get_color_component("blue")
        
        print("RGB Details:")

        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        
        hex_color = convert_to_hex(r, g, b)
        
        print(f"- Hex {hex_color}")
        
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()