####################################################################
# Task:A9_T1
# Developer: Henri Holopainen
# Date: 2025-11-26
####################################################################
def ag_t1_faulty_user_input():
    total_sum = 0.0
    
    print("Program starting.")
    print("")
    
    while True:
        prompt = "Insert a floating-point value. (0:to stop): "
        user_input_raw = input(prompt)
        
        
        if user_input_raw == "0" or user_input_raw.lower() == "stop":
            break
        
        try:
            value = float(user_input_raw)
            total_sum += value
        except ValueError:
            print(f"Error! {user_input_raw} couldn't be converted to float.")
    
    final_sum_str = "{:.2f}".format(total_sum)
    print("")
    print(f"Final sum is {final_sum_str}")
    
    print("Program ending.")

if __name__ == "__main__":
    ag_t1_faulty_user_input()