import csv
import sys
import os # Lisätty tiedostopolun tarkistusta varten
from typing import List, Tuple, Dict

WEEKDAYS: Tuple[str] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def readfile(pFilename: str, pRows: List[str]) -> None:
    print(f"Reading file: \"{pFilename}\"")
    pRows.clear()
    
    if not os.path.exists(pFilename):
        print(f"Error: File not found: {pFilename}")
        pRows.clear()
        return

    try:
        # Muutettu: Poistettu 'encoding='utf-8''
        with open(pFilename, 'r', newline='') as filehandle: 
            reader = csv.reader(filehandle, delimiter=';') 
            
            next(reader) 
            
            for row_list in reader:
                if row_list and row_list[0].strip():
                    pRows.append(';'.join(row_list))

    except Exception as e:
        print(f"Error reading file: {e}")
        pRows.clear()
        
    return None

def analyseTimestamps(pRows: List[str], pResults: List[str]) -> None:
    print("Analysing timestamps.")
    
    pResults.clear()
    
    weekday_stamp_amount: List[int] = [0] * len(WEEKDAYS)
    
    for row in pRows:
        for j, day in enumerate(WEEKDAYS):
            if row.startswith(day + ';'):
                weekday_stamp_amount[j] += 1
                break

    pResults.append("### Timestamp analysis ###")
    for i, day in enumerate(WEEKDAYS):
        stamps = weekday_stamp_amount[i]
        pResults.append(f"-- {day:10} {stamps} stamps")
        
    pResults.append("### Timestamp analysis ###")
    
    weekday_stamp_amount.clear()

    return None

def displayResults(pResults: List[str]) -> None:
    print("Displaying results.")
    
    for result in pResults:
        print(result)
        
    return None

def main():
    data_rows: List[str] = []
    analysis_results: List[str] = []
    
    print("Program starting.")
    
    if sys.stdin.isatty():
        filename = input("Insert filename: ")
    else:
        filename = sys.stdin.readline().strip()
        print(f"Insert filename: {filename}")

    readfile(filename, data_rows)
    
    if data_rows:
        analyseTimestamps(data_rows, analysis_results)
    else:
        analysis_results.append("### Timestamp analysis ###")
        for day in WEEKDAYS:
            analysis_results.append(f"-- {day:10} 0 stamps")
        analysis_results.append("### Timestamp analysis ###")

    displayResults(analysis_results)
    
    data_rows.clear()
    analysis_results.clear()
    
    print("Program ending.")
    
    return None

if __name__ == "__main__":
    main()