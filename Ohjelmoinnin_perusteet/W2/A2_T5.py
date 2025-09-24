print("Program starting.\n")

Word = input("Insert a closed compound word: ")
Reverse = Word[::-1]

print(f"The word you inserted is '{Word}' and in reverse it is '{Reverse}'.")

Length = len(Word)
print(f"The inserted word length is {Length}")

Last = Word[-1]
print(f"Last character is '{Last}'")

print("\nTake substring from the inserted word by inserting...")
Start = int(input("1) Starting point: "))
End = int(input("2) Ending point: "))
Step = int(input("3) Step size: "))

Whole = Word[Start:End:Step]

print(f"\nThe word '{Word}' sliced to the defined substring is '{Whole}'.")
print("Program ending.")