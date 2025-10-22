def frameWord(pWord):
    kehyksen_leveys = len(pWord) + 4
    merkki_rivi = "*" * kehyksen_leveys
    sana_rivi = f"* {pWord} *"
    
    print(merkki_rivi)
    print(sana_rivi)
    print(merkki_rivi)
    
    return None

def main():
    print("Program starting.")
    
    
    syote = input("Insert word: ")
    
    frameWord(syote)
    
    print()
    
    print("Program ending.")
    
    return None

main()