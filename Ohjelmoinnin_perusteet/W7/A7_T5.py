import csv
from collections import defaultdict
import sys

def main(): 
    print("Program starting.")
    
    
    try:
        filename = input("Insert filename: ").strip()
        if not filename:
            print("Virhe: Tiedostonimi puuttuu.")
            
            return
    except EOFError:
        
        filename = "A7_T5_D1.csv"
        
    
    print(f'Reading file "{filename}".') 
    
    
    daily_summary = defaultdict(lambda: {'usage': 0.0, 'cost': 0.0})
    
    
    day_names_order = [
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
    ]

    try:
        
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader) 
            
            print("Analysing timestamps.")

            for row in reader:
                
                if len(row) < 4:
                    continue
                
                day_name = row[0].strip()
                
                try:
                    
                    consumption = float(row[2].replace(',', '.').strip())
                    
                    price = float(row[3].replace(',', '.').strip())
                except ValueError:
                    continue 

                line_cost = consumption * price
                
                daily_summary[day_name]['usage'] += consumption
                daily_summary[day_name]['cost'] += line_cost

    except FileNotFoundError:
        print(f"Error: Tiedostoa ei löydy: {filename}")
        
        
        return
    except Exception as e:
        print(f"Odottamaton virhe: {e}")
        
        return

    print("Displaying results.")
    
    print("### Electricity consumption summary ###")

    
    for day in day_names_order:
        summary = daily_summary[day]
        usage = summary['usage']
        cost = summary['cost']
        
        
        print(f" - {day} usage {usage:.2f} kWh, cost {cost:.2f} €")
        
    
    print("### Electricity consumption summary ###")
    print("Program ending.")
    
    
    
    

main()