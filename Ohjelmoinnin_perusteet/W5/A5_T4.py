def askDimension(pPrompt: str) -> float:
    Feed = input(f"Insert {pPrompt}: ")
    return float(Feed)

def calcRectangleArea(pWidth: float, pHeight: float) -> float:
    Area = pWidth * pHeight
    return Area

def calculateArea():
    print("Program starting.")
    
    Width = askDimension("width")
    Height = askDimension("height")
    
    Area = calcRectangleArea(Width, Height)
    
    print("") 
    
    print(f"Area is {Area:.1f}²")
    
    print("Program ending.")

calculateArea()