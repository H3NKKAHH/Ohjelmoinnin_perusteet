def one_multi_branched_decision(initial_value: int) -> int:
    result = initial_value
    print("Using: One multi-branched decision structure.")

    if result >= 400:
        result += 44
    elif result >= 200:
        result += 22
    elif result >= 100:
        result += 11
        
    return result

def independent_if_statements(initial_value: int) -> int:
    result = initial_value
    print("Using: In multiple independent if-statements.")

    if result >= 400:
        result += 44
        
    if result >= 200:
        result += 22

    if result >= 100:
        result += 11
        
    return result

def main():
    print("Program starting.")
    print("Testing decision structures.")
    
    initial_value = None
    while initial_value is None:
        try:
            initial_value = int(input("Insert an integer: "))
        except ValueError:
            print("Invalid input. Please insert a whole number (integer).")
    
    try:
        print("\nOptions:")
        print("1 - In one multi-branched decision")
        print("2 - In multiple independent if-statements")
        print("0 - Exit")
        
        choice = int(input("Your choice: "))
        
        final_result = None

        if choice == 1:
            final_result = one_multi_branched_decision(initial_value)
            
        elif choice == 2:
            final_result = independent_if_statements(initial_value)
            
        elif choice == 0:
            print("Exiting...")
            
        else:
            print("Unknown option.")

        if final_result is not None:
            print(f"Result is: {final_result}")

    except ValueError:
        print("Invalid choice. Please enter 1, 2, or 0.")
    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()
