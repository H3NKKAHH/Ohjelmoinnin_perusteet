def kopioi_tiedosto():

    print("Program starting.")
    print("This program can copy a file.")

    Lahdetiedosto = input("Insert source filename: ")
    Kohdetiedosto = input("Insert destination filename: ")

    try:
    
        print(f"Reading file {Lahdetiedosto} content.")
        with open(Lahdetiedosto, "r", encoding="utf-8") as lahde:
            sisalto = lahde.read()
        print("File content ready in memory.")
    except FileNotFoundError:
        print(f"Error: Source file {Lahdetiedosto} not found. Copying aborted.")
        print("Program ending.")
        return
    
    try:

        print(f"Writing content into file {Kohdetiedosto}.")
        with open(Kohdetiedosto, "w", encoding="utf-8") as kohde:
            kohde.write(sisalto)
        print("Copying operation complete.")
    except Exception as e:
        print(f"An unexpected error occured during writing: {e}")
    
    print("Program ending.")

kopioi_tiedosto()