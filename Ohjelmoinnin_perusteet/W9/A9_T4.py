####################################################################
# Task: A9_T4
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000.0

def collectCelsius():
    prompt = "Insert Celsius: "
    raw_input = input(prompt)
    
    

    try:
        celsius_value = float(raw_input)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{raw_input}'")
        
    if not (TEMP_MIN <= celsius_value <= TEMP_MAX):
        raise Exception(f"{celsius_value} temperature out of range.")
        
    return celsius_value

def main():
    print("Program starting.")
    
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius:.1f}°C")
        
    except ValueError as ve:
        print(f"{ve}")
        
    except Exception as e:
        print(f"{e}")
        
    print("Program ending.")

if __name__ == "__main__":
    main()