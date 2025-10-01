print("Program starting.")
print("Insert two integers.")

Int1 = int(input("Insert first integer: "))
Int2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if(Int1 > Int2):
    print("First integer is greater.")
elif(Int2 > Int1):
    print("Second integer is greater.")
else:
    print("Integers are the same.")

Sum = Int1 + Int2

print(f"{Int1} + {Int2} = {Sum}")
print("")

Remainder = Sum % 2
if(Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending")
