print("Program starting.")

Alku = int(input("Insert starting value: "))
Loppu = int(input("Insert stopping value: "))

print("")
print("Starting for-loop:")

for Luku in range(Alku, Loppu + 1):
    if Luku == Loppu:
        print(Luku, end="")
    else:
        print(Luku, end=" ")


print("")
print("")
print("Program ending.")
