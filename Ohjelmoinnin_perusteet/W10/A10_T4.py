###############################################################
# # Task: A10_T4
# # Developer: Henri Holopainen
# # Date: 2025-12-09
# #############################################################

import sys
import copy


def read_values(PFilename: str) -> list[int] | None:

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
        sys.exit(1)
    
    return values

def display_sorted_results(filename: str, raw_data: list[int], sorted_asc: list[int], sorted_desc: list[int]) -> None:

    raw_str = ", ".join(map(str, raw_data))
    asc_str = ", ".join(map(str, sorted_asc))
    desc_str = ", ".join(map(str, sorted_desc))
    
    print(f"Raw '{filename}' -> {raw_str}")
    print(f"Ascending '{filename}' -> {asc_str}")
    print(f"Descending '{filename}' -> {desc_str}")
# -----------------------------------------------------------------


def merge(arr: list[int], left: int, mid: int, right: int, PAsc: bool):

    
    n1 = mid - left + 1
    n2 = right - mid
    
    
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]
    
    i = 0  
    j = 0  
    k = left 

    
    while i < n1 and j < n2:

        should_use_left = False
        
        if PAsc:
            
            if L[i] <= R[j]:
                should_use_left = True
        else:
            
            if L[i] >= R[j]:
                should_use_left = True

        if should_use_left:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def recursive_merge_sort(arr: list[int], left: int, right: int, PAsc: bool):

    if left < right:
        
        mid = left + (right - left) // 2
        
        
        recursive_merge_sort(arr, left, mid, PAsc)       
        recursive_merge_sort(arr, mid + 1, right, PAsc)  
        
        
        merge(arr, left, mid, right, PAsc)


def MergeSort(PValues: list[int], PAsc: bool = True) -> None:

    if not PValues:
        return
        
    n = len(PValues)
    recursive_merge_sort(PValues, 0, n - 1, PAsc)


def main() -> None:

    print("Program starting.")

    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    
    values = read_values(filename)
    
    if values is None:
        print("Program ending.")
        return

    
    raw_data = copy.deepcopy(values)
    asc_data = copy.deepcopy(values)
    desc_data = copy.deepcopy(values)

    
    MergeSort(asc_data, PAsc=True)

    
    MergeSort(desc_data, PAsc=False)

    
    display_sorted_results(filename, raw_data, asc_data, desc_data)

    print("Program ending.")


if __name__ == "__main__":
    main()