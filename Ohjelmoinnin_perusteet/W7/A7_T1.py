def positive_integer_collector():
    collected_integers = []
    
    print("Program starting.")
    print("Collect positive integers.")

    while True:
        try:
            user_input = input("Insert positive integer (negative stops): ")
            number = int(user_input)
            
            if number < 0:
                print("Stopped collecting positive integers.")
                break
            
            if number > 0:
                collected_integers.append(number)
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    if not collected_integers:
        print("No integers to display.")
    else:
        print(f"Displaying {len(collected_integers)} integers:")
        
        for index, integer in enumerate(collected_integers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {integer}")

    print("Program ending.")

if __name__ == "__main__":
    positive_integer_collector()