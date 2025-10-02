print("Program starting.")
print("Testing decision structures.")

initial_value_str = input("Insert an integer: ")
initial_value = int(initial_value_str)
result_value = initial_value

print("\nOptions:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice_str = input("Your choice: ")
choice = int(choice_str)

print("")

if choice == 1:
    print("Using: one multi-branched decision structure.")

    if initial_value >= 400:
        result_value += 44
        # print(f"Condition: Value >= 400 was met. Added 44.")

    elif initial_value >= 200:
        result_value += 22
        # print(f"Condition: Value >= 200 was met. Added 22.")

    elif initial_value >= 100:
        result_value += 11
        # print(f"Condition: Value >= 100 was met. Added 11.")

    


elif choice == 2:
    print("Using: multiple independent if-statements.")

    added_count = 0

    if initial_value >= 400:
        result_value += 44
        added_count += 44
    

    if initial_value >= 200:
        result_value += 22
        added_count += 22
    

    if initial_value >= 100:
        result_value += 11
        added_count += 11
    
        
    if added_count == 0:
        print("No conditions were met. Value remains unchanged.")


elif choice == 0:
    print("Exiting...")
    result_value = initial_value

else:
    print("Unknown option.")
    result_value = initial_value

if choice in [1, 2]:
    print("-" * 30)
    print(f"Result is: {result_value}")

print("\nProgram ending.")
