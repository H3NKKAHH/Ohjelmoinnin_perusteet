###############################################################
# # Task: A10_T5
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

def recursiveFactorial(PNum: int) -> int:

    if PNum == 0 or PNum == 1:
        return 1
    
    
    elif PNum > 1:
        return PNum * recursiveFactorial(PNum - 1)
    
    
    else:
        raise ValueError("Kertoma on määritelty vain ei-negatiivisille kokonaisluvuille.")

def format_calculation(PNum: int) -> str:

    if PNum <= 0:
        return "1" 

    
    numbers = [str(i) for i in range(1, PNum + 1)]
    return "*".join(numbers)


def main() -> None:

    print("Program starting.")
    
    try:
        user_input = input("Insert factorial: ")
        num = int(user_input)
        
        if num < 0:
            print("Syötteen täytyy olla ei-negatiivinen kokonaisluku.")
            print("Program ending.")
            return

        
        result = recursiveFactorial(num)
        
        
        calculation_str = format_calculation(num)
        
        
        print(f"Factorial {num}!")
        print(f"{calculation_str} = {result}")
        
    except ValueError as e:
        
        print(f"Virhe: {e if 'Kertoma' in str(e) else 'Syötteen täytyy olla kokonaisluku.'}")
        
    print("Program ending.")


if __name__ == "__main__":
    main()