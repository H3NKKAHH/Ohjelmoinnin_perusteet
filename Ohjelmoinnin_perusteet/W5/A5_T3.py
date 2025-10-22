def askName():
    Nimi = input("Insert name: ")
    return Nimi

def greetUser(pName):
    print(f"Hello {pName}!")
    return None




def main():
    print("Program starting.")

    user_name = askName()
    greetUser(user_name)

    print("Program ending.")
    return None




main()