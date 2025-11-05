def lue_tiedosto_ja_tulosta():
    print("Program starting.")
    print("This program can read a file.")
    
    tiedostonimi = input("Insert filename: ")
    
    start_rivi = f"#### START \"{tiedostonimi}\" ####"
    end_rivi = f"#### END \"{tiedostonimi}\" ####"
    
    try:
        with open(tiedostonimi, 'r', encoding='utf-8') as f:
            print(start_rivi)
            sisalto = f.read()
            print(sisalto.rstrip())
            print()
            print(end_rivi)
            

    except FileNotFoundError:
        print(f"Error: File '{tiedostonimi}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    print("Program ending.")

lue_tiedosto_ja_tulosta()