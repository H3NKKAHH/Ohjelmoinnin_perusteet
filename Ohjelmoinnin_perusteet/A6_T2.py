def kirjoita_txt():

    print("Program starting.")
    Etunimi = input("Insert first name: ")
    Sukunimi = input("Insert last name: ")
    Tiedosto_nimi = input("Insert filename: ")

    sisalto = f"{Etunimi}\n{Sukunimi}\n"

    try:
        with open(Tiedosto_nimi, 'w', encoding='utf-8') as f:
            f.write(sisalto)

    except Exception as e:
        print("An error occured while writing this file: {e}")

    print("Program ending.")

kirjoita_txt()