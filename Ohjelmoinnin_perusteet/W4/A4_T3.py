print("Program starting.")

Alku = int(input("Insert starting value: "))
Loppu = int(input("Insert stopping value: "))

print("")
print("Starting  while-loop:")

Luku = Alku

while Luku <= Loppu:
    if Luku == Loppu:
        print(Luku, end="")
    else:
        print(Luku, end=" ")
    Luku +=1




print("")
print("")
print("Program ending.")
