import A8_T2_laskut

print("Program starting.")

def showOptions():

    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def askChoice():
    choice = int(input("Your choice: "))
    return choice

def askValue(prompt_text):
    value = float(input(prompt_text + ": "))
    return value

def main():
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.")
            break
            
        if choice == 1:
            v1 = askValue("Insert first addend value")
            v2 = askValue("Insert second addend value")
            res = A8_T2_laskut.add(v1, v2)
            print(f"{v1} + {v2} = {res}")
            
        elif choice == 2:
            v1 = askValue("Insert minuend value")
            v2 = askValue("Insert subtrahend value")
            res = A8_T2_laskut.subtract(v1, v2)
            print(f"{v1} - {v2} = {res}")

        elif choice == 3:
            v1 = askValue("Insert multiplicant value")
            v2 = askValue("Insert multiplier value")
            res = A8_T2_laskut.multiply(v1, v2)
            print(f"{v1} * {v2} = {res}")

        elif choice == 4:
            v1 = askValue("Insert dividend value")
            v2 = askValue("Insert divisor value")
            res = A8_T2_laskut.divide(v1, v2)
            print(f"{v1} / {v2} = {res}")
            
        print() 

if __name__ == "__main__":
    main()
    print("")
    print("Program ending.")

        

