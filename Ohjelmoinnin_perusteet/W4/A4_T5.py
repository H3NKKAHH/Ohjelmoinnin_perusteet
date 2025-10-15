print("Program starting.")
print("")

try:
    aloitus_arvo = int(input("Insert starting point: "))
    lopetus_arvo = int(input("Insert stopping point: "))
    tarkistus_arvo = int(input("Insert inspection point: "))
    print("")

    virheet = False

    if aloitus_arvo >= lopetus_arvo:
        
        print('Starting point value must be less than the stopping point value.')
        virheet = True
    
    if tarkistus_arvo < aloitus_arvo or tarkistus_arvo > lopetus_arvo:
        print('Inspection value must be within the range of start and stop.')
        virheet = True

    if not virheet:
        
        luvut_sarja = range(aloitus_arvo, lopetus_arvo + 1)
        
       
        
        print("First loop - inspection with break:")
        
        tulostus_rivi_break = "" 
        
        for luku in luvut_sarja:
            
            if luku == tarkistus_arvo:
                break
            
            tulostus_rivi_break += str(luku) + " "
        
        print(tulostus_rivi_break.rstrip())

        print("Second loop - inspection with continue:")
        
        tulostus_rivi_continue = ""

        for luku in luvut_sarja:
            
            if luku == tarkistus_arvo:
                continue
            
            tulostus_rivi_continue += str(luku) + " "

        print(tulostus_rivi_continue.rstrip())

except ValueError:
    print("Invalid input. Please insert only integers.")


print() 
print("Program ending.")