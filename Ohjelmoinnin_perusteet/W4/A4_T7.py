print("Program starting.")
print()
print("Check multiplicative persistence.")

luku_str = input("Insert an integer: ")

Persistence_laskuri = 0

while len(luku_str) > 1: 
    Tulo = 1
    Tulostus_lauseke = ""
    
    for i, numero_char in enumerate(luku_str):
        numero_int = int(numero_char)
        
        Tulo *= numero_int 
        
        Tulostus_lauseke += numero_char
        
        if i < len(luku_str) - 1:
            Tulostus_lauseke += " * "
            
    print(f"{Tulostus_lauseke} = {Tulo}")
    
    luku_str = str(Tulo)
    
    Persistence_laskuri += 1


print("No more steps.")
print("")


print(f"This program took {Persistence_laskuri} step(s)")


print() 
print("Program ending.")