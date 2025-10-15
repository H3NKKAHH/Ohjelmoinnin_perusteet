print("Program starting.")

Sanat_lkm = 0
Merkit_lkm = 0 

while True:
    Feed = input("Insert word (empty stops): ")
    if Feed == "":
        break
    
    Sanat_lkm += 1

    Merkit_lkm += len(Feed)

print("")
print("You inserted:")
print(f"- {Sanat_lkm} words")
print(f"- {Merkit_lkm} characters")

print("")
print("Program ending.")