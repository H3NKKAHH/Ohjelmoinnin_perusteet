###############################################################
# # Task: A10_T7
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import random
import sys
from typing import List, Dict, Tuple


random.seed(1234)



def generateMinefield(PMineField: List[List[int]], PRows: int, PCols: int, PMines: int) -> None:

    
    PMineField.clear()
    
    
    for _ in range(PRows):
        
        row = [0] * PCols
        PMineField.append(row)
        
    
    layMines(PMineField, PMines)
    
    
    calculateNearbys(PMineField)

    return None



def layMines(PMineField: List[List[int]], PMines: int) -> None:

    if not PMineField:
        return
        
    rows = len(PMineField)
    cols = len(PMineField[0])
    max_cells = rows * cols
    
    if PMines > max_cells:
        print("Varoitus: Miinoja on enemmän kuin ruutuja. Kenttä täytetään miinoilla.")
        PMines = max_cells 
        
    mines_placed = 0
    
    while mines_placed < PMines:
        
        r = random.randrange(rows)
        c = random.randrange(cols)
        

        if PMineField[r][c] != 9:
            PMineField[r][c] = 9 
            mines_placed += 1
            
    return None
    


def calculateNearbys(PMineField: List[List[int]]) -> None:

    if not PMineField:
        return
        
    rows = len(PMineField)
    cols = len(PMineField[0])
    
    
    for r in range(rows):
        for c in range(cols):
            
            
            if PMineField[r][c] == 9:
                continue
            
            
            mine_count = 0
            
            
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    
                    
                    if dr == 0 and dc == 0:
                        continue
                        
                    
                    nr, nc = r + dr, c + dc
                    

                    if 0 <= nr < rows and 0 <= nc < cols:
                        
                        
                        if PMineField[nr][nc] == 9:
                            mine_count += 1
            
           
            PMineField[r][c] = mine_count
            
    return None



def show_board(PMineField: List[List[int]]) -> None:

    if not PMineField:
        print("Kenttä on tyhjä.")
        return
        
    print("Generated board:")
    for row in PMineField:
       
        row_str = f"[{', '.join(map(str, row))}]"
        print(row_str)

def save_board(PMineField: List[List[int]]) -> None:
    
    if not PMineField:
        print("Error: Kenttää ei ole luotu.")
        return
        
    filename = input("Insert filename to save: ")
    
    try:
        with open(filename, 'w') as f:
            for row in PMineField:
                
                row_str = ",".join(map(str, row))
                f.write(row_str + '\n')
        
        print(f"Board saved to '{filename}'.")
        
    except IOError:
        print(f"Error: Could not write to file '{filename}'.")




def run_menu(minefield: List[List[int]], current_rows: int, current_cols: int, current_mines: int) -> Tuple[List[List[int]], int, int, int, int]:
    
    
    print("\nOptions:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")
    
    choice = input("Your choice: ")
    
    if choice == '1':
        
        try:
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            
            if rows <= 0 or cols <= 0 or mines < 0:
                print("Error: Rows, columns must be > 0 and mines must be >= 0.")
                return minefield, current_rows, current_cols, current_mines, 1

            
            generateMinefield(minefield, rows, cols, mines)
            current_rows, current_cols, current_mines = rows, cols, mines
            print("Board generated.")
            
        except ValueError:
            print("Error: Invalid input. Please insert integers.")
            
        return minefield, current_rows, current_cols, current_mines, 1
    
    elif choice == '2':
        
        if not minefield:
            print("Error: Board not generated. Please choose option 1 first.")
        else:
            show_board(minefield)
            
        return minefield, current_rows, current_cols, current_mines, 2

    elif choice == '3':
       
        save_board(minefield)
        return minefield, current_rows, current_cols, current_mines, 3
        
    elif choice == '0':
        
        print("Exiting program.")
        return minefield, current_rows, current_cols, current_mines, 0
        
    else:
        print("Invalid choice. Please choose 0, 1, 2, or 3.")
        return minefield, current_rows, current_cols, current_mines, 4


def main() -> None:
    
    
    
    minefield: List[List[int]] = [] 
    rows, cols, mines = 0, 0, 0
    
    print("Program starting.")
    
    
    choice = 1
    while choice != 0:
        
        minefield, rows, cols, mines, choice = run_menu(minefield, rows, cols, mines)
    
    print("Program ending.")


if __name__ == "__main__":
    main()