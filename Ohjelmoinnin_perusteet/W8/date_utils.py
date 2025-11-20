from datetime import datetime


MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def readTimestamps(filename, timestamps_list):
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    
                    
                    dt_object = datetime.strptime(line, "%Y-%m-%dT%H:%M")
                    timestamps_list.append(dt_object)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def calculateYears(year, timestamps_list):
    
    count = 0
    for dt in timestamps_list:
        if dt.year == year:
            count += 1
    return count

def calculateMonths(month_name, timestamps_list):
    
    count = 0
    
    
    if month_name in MONTHS:
        month_number = MONTHS.index(month_name) + 1
        
        for dt in timestamps_list:
            if dt.month == month_number:
                count += 1
    return count

def calculateWeekdays(weekday_name, timestamps_list):
    
    count = 0
    
    if weekday_name in WEEKDAYS:
        weekday_number = WEEKDAYS.index(weekday_name)
        
        for dt in timestamps_list:
            if dt.weekday() == weekday_number:
                count += 1
    return count