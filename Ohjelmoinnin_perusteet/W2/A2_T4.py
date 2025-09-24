print("Program starting.")

print("Estimate how many minutes you spent on programming...\n")

Task_1 = int(input("A1_T1: "))
Task_2 = int(input("A1_T2: "))
Task_3 = int(input("A1_T3: "))
Task_4 = int(input("A1_T4: "))
Task_5 = int(input("A1_T5: "))
Task_6 = int(input("A1_T6: "))
Task_7 = int(input("A1_T7: "))

Total = Task_1 + Task_2 + Task_3 + Task_4 + Task_5 + Task_6 + Task_7
Average = float(Total / 7)

print(f"\nIn total you spent {Total} minutes on programming.")
print(f"Average per task was {round(Average, 2)} minutes and same rounded to the nearest integer {round(Average)} minutes.")

print("\nProgram ending.")