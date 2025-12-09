###############################################################
# # Task: A10_T6
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import sys
import copy
import time
from typing import Callable, List, Dict, Union



def read_values(PFilename: str) -> List[int] | None:
    
    values = []
    try:
        with open(PFilename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    try:
                        values.append(int(clean_line))
                    except ValueError:
                        pass
    except FileNotFoundError:
        
        print(f"Error: Tiedostoa '{PFilename}' ei löydy.")
        return None
    
    return values

def BubbleSort(PValues: List[int], PAsc: bool = True) -> None:
    """Lajittelee listan PValues nousevasti (PAsc=True) paikallaan (in place)."""
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
           
            if PValues[j] > PValues[j+1]:
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]



def partition(arr: List[int], low: int, high: int) -> int:
    """Quick Sortin ositus (partition) -toiminto."""
    
    pivot = arr[high]
    i = low - 1  
    
    for j in range(low, high):
        
        if arr[j] <= pivot:
            i = i + 1
           
            arr[i], arr[j] = arr[j], arr[i]
            
   
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _quickSortRecursive(arr: List[int], low: int, high: int) -> None:
    
    if low < high:
       
        pi = partition(arr, low, high)
        
        
        _quickSortRecursive(arr, low, pi - 1)
        _quickSortRecursive(arr, pi + 1, high)

def QuickSort(PValues: List[int], PAsc: bool = True) -> None:

    if PValues:
        _quickSortRecursive(PValues, 0, len(PValues) - 1)



def measureSortingTime(PSortingAlgorithm: Callable[[List[int], bool], None], PArr: List[int]) -> int:

    
    StartTimeNs = time.perf_counter_ns()
    

    if PSortingAlgorithm.__name__ == 'sort':
        PArr.sort()
    
    else:
        PSortingAlgorithm(PArr, True)

    EndTimeNs = time.perf_counter_ns()
    
    
    ElapsedTimeNs = EndTimeNs - StartTimeNs
    
    return ElapsedTimeNs


def BuiltInSorted(PValues: List[int], PAsc: bool = True) -> None:

    sorted_list = sorted(PValues)
    PValues[:] = sorted_list 



def run_menu(current_values: List[int], filename: str, results: Dict[str, int]) -> tuple[List[int], str, Dict[str, int], int]:

    
    print("\nOptions:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")
    
    choice = input("Your choice: ")
    
    if choice == '1':
        
        new_filename = input("Insert dataset filename: ")
        
        data = read_values(new_filename)
        if data is not None:
            current_values = data
            filename = new_filename
            print(f"Data set '{filename}' read. Size: {len(current_values)}")
            
            results = {} 
        
        return current_values, filename, results, 1
    
    elif choice == '2':
        
        if not current_values:
            print("Error: No dataset loaded. Please choose option 1 first.")
            return current_values, filename, results, 2

        print(f"Measuring speeds for dataset: '{filename}'.")
        
        
        algorithms_to_test = {
            "Built-in sorted": BuiltInSorted, 
            "Bubble sort": BubbleSort,
            "Quick sort": QuickSort
        }
        
        measured_results = {}
        
        for name, func in algorithms_to_test.items():
            
            data_copy = copy.deepcopy(current_values)
            
            
            time_ns = measureSortingTime(func, data_copy)
            measured_results[name] = time_ns
            print(f"{name}: {time_ns} ns")

        results = measured_results
        return current_values, filename, results, 2

    elif choice == '3':
        
        if not results:
            print("Error: No measurement results to save. Please choose option 2 first.")
            return current_values, filename, results, 3

        output_filename = input("Insert results filename: ")
        
        try:
            with open(output_filename, 'w') as f:
                f.write(f"Measured speeds for dataset: '{filename}':\n")
                
                
                sorted_results = sorted(results.items(), key=lambda item: item[1])
                
                for name, time_ns in sorted_results:
                    f.write(f"..{name}: {time_ns} ns\n")
            
            print(f"Results saved to '{output_filename}'")
            
        except IOError:
            print(f"Error: Could not write to file '{output_filename}'.")

        return current_values, filename, results, 3
        
    elif choice == '0':
        
        print("Exiting program.")
        return current_values, filename, results, 0
        
    else:
        print("Invalid choice. Please choose 0, 1, 2, or 3.")
        return current_values, filename, results, 4


def main() -> None:

    
    
    current_values: List[int] = []
    current_filename: str = ""
   
    speed_results: Dict[str, int] = {} 
    
    print("Program starting.")
    
    
    choice = 1 
    while choice != 0:
        
        current_values, current_filename, speed_results, choice = run_menu(
            current_values, current_filename, speed_results
        )
    

    print("Program ending.")


if __name__ == "__main__":
    main()