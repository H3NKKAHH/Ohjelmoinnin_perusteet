def analyse_separated_values():
    print("Program starting.")
    
    user_input = input("Insert comma-separated integers: ")
    
    entries = user_input.split(',')
    
    valid_integers = []
    
    for entry in entries:
        trimmed_entry = entry.strip()
        
        if not trimmed_entry:
            continue
            
        try:
            number = int(trimmed_entry)
            valid_integers.append(number)
            
        except ValueError:
            print(f"Error: Invalid value detected: '{trimmed_entry}'")

    if not valid_integers:
        print("There are no valid integers to analyze.")
    else:
        count = len(valid_integers)
        print(f"There are {count} integers in the list.")
        
        total_sum = sum(valid_integers)
        
        even_or_odd = "even" if total_sum % 2 == 0 else "odd"
        
        print(f"Sum of the integers is {total_sum} and it's {even_or_odd}.")

    print("Program ending.")

if __name__ == "__main__":
    analyse_separated_values()