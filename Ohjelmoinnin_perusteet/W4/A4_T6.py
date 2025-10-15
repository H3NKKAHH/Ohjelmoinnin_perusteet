print("Program starting.")

try:
    aloitusluku_str = input("Insert a positive integer: ")
    aloitusluku = int(aloitusluku_str)
except Exception:
    pass

nykyinen_luku = aloitusluku
lukujono = [aloitusluku]
askeleet = 0

while nykyinen_luku != 1:
    if nykyinen_luku % 2 == 0:
        nykyinen_luku //= 2
    else:
        nykyinen_luku = 3 * nykyinen_luku + 1
    
    lukujono.append(nykyinen_luku)
    askeleet += 1


jono_tekstina = " -> ".join(map(str, lukujono))
print(f"{jono_tekstina}") 

print(f"Sequence had {askeleet} total steps.")


print("") 

print("Program ending.")