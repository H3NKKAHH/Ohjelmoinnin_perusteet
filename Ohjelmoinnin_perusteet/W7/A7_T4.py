import csv
import sys
import os
from typing import List, Tuple, Dict, Any

TIMESTAMP: Tuple[str] = ("Weekday", "Hour", "Consumption(kWh)", "Price(€/kWh)") 

def readTimestamps(pFilename: str, pRows: List[str]) -> None:
    pRows.clear()
    
    if not os.path.exists(pFilename):
        print(f"Error: File not found: {pFilename}")
        pRows.clear()
        return

    try:
        with open(pFilename, 'r', newline='') as filehandle: 
            reader = csv.reader(filehandle, delimiter=';') 
            
            next(reader) 
            
            for row_list in reader:
                trimmed_row_list = [item.strip() for item in row_list]
                
                if trimmed_row_list and trimmed_row_list[0]:
                    pRows.append(';'.join(trimmed_row_list))

    except Exception as e:
        print(f"Error reading file: {e}")
        pRows.clear()
        
    return None

def analyseConsumption(pRows: List[str], pResults: List[str]) -> None:
    pResults.clear()
    
    for row in pRows:
        row_data = row.split(';')
        
        if len(row_data) != 4:
            continue
            
        weekday_str = row_data[0]
        hour_str = row_data[1]
        consumption_str = row_data[2]
        price_str = row_data[3]
        
        try:
            consumption = float(consumption_str.replace(',', '.'))
            price = float(price_str.replace(',', '.'))
            
        except ValueError:
            continue

        total_cost = consumption * price
        
        time_str = f"{hour_str}:00"

        result_string = (
            f" - "
            f"{weekday_str} {time_str}, "
            f"price {price:.2f}, "
            f"consumption {consumption:.2f} kWh, "
            f"total {total_cost:.2f} €"
        )
        pResults.append(result_string)

    return None

def displayTimestamps(pResults: List[str]) -> None:
    print("Electricity usage:")
    
    
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
        
    readTimestamps(filename, data_rows)
    
    if data_rows:
        analyseConsumption(data_rows, analysis_results)
    
    displayTimestamps(analysis_results)
    
    data_rows.clear()
    analysis_results.clear()
    
    print("Program ending.")
    
    return None

if __name__ == "__main__":
    main()