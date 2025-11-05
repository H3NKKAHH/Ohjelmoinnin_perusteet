def analysoi_nimet():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    
    tiedostonimi = input("Insert filename to read: ")
    
    rivit = []
    
    try:
        print(f"Reading names from \"{tiedostonimi}\".")
        with open(tiedostonimi, 'r', encoding='utf-8') as f:
            for rivi in f:
                puhdistettu_rivi = rivi.strip()
                if puhdistettu_rivi:
                    rivit.append(puhdistettu_rivi)
            
    except FileNotFoundError:
        print(f"Error: File '{tiedostonimi}' not found.")
        print("Program ending.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during reading: {e}")
        print("Program ending.")
        return

    # Käsittele ja analysoi nimet
    kaikki_nimet = []
    for rivi in rivit:
        osat = rivi.split(';')
        for nimi in osat:
            nimi = nimi.strip()
            if nimi:
                kaikki_nimet.append(nimi)

    print("Analyzing names...")

    if not kaikki_nimet:
        print("No valid names found for analysis.")
        print("Program ending.")
        return

    # Laskennat
    nimien_lkm = len(kaikki_nimet)
    nimien_pituudet = [len(nimi) for nimi in kaikki_nimet]
    
    lyhin_pituus = min(nimien_pituudet)
    pisin_pituus = max(nimien_pituudet)
    keskiarvo_pituus = sum(nimien_pituudet) / nimien_lkm
    
    # Tulosta raportti
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count: {nimien_lkm}")
    print(f"Shortest name: {lyhin_pituus} chars")
    print(f"Longest name: {pisin_pituus} chars")
    print(f"Average name length: {keskiarvo_pituus:.2f} chars")
    print("#### REPORT END ####")
    print("Program ending.")

analysoi_nimet()