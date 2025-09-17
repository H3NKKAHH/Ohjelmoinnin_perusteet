#Assign value 47 to variable Num1
#Assign value 102 to a variable Num2
#Sum variables Num1 and Num2, and put the result into Sum variable
#Subtract Num1 from Num2, then store the result in the Diff variable.
#Multiply Sum and Diff, then place the resulting product in Product.
#Print the sum operation “{Num1} + {Num2} = {Sum}”
#Print the sub operation “{Num2} - {Num1} = {Diff}”
#Print the multiply operation “{Sum} * {Diff} = {Product}”
#Print the sum, sub and multiply operations together. See “program run” below.

Num1 = 47
Num2 = 102

Sum = Num1 + Num2 

Diff = Num2 - Num1

Product = Sum * Diff

print(Num1, "+", Num2, "=", Sum)

print(Num2, "-", Num1, "=", Diff)

print(Sum, "*", Diff, "=", Product)

print("(" ,Num1, " + " ,Num2, ") * (" ,Num2, " - ", Num1, ") = " ,Product)
