import sys


SEPARATOR = ";"

def read_and_analyze(filename: str) -> str:
 
    all_numbers = []
    
    try:
        
        with open(filename, 'r') as f:
            
            
            
            for line in f:
                
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                try:
                    
                    num = int(clean_line)
                    
                    
                    if num > 0:
                        all_numbers.append(num)
                        
                except ValueError:
                    
                    continue
                        
    except FileNotFoundError:
        return f"Error: File not found at path: {filename}"
    except Exception as e:
        return f"Error reading file: {e}"

    
    if not all_numbers:
        return "Error: No valid positive integer data found in file."

    
    total_sum = sum(all_numbers)
    count = len(all_numbers) 
    greatest = max(all_numbers)
    average = total_sum / count
    
    formatted_average = '{:.2f}'.format(average)
    
    
    result_string = (
        f"{count}{SEPARATOR}"
        f"{total_sum}{SEPARATOR}"
        f"{greatest}{SEPARATOR}"
        f"{formatted_average}"
    )
    
    return result_string

if __name__ == "__main__":
    
    print("Program starting.")
    
    
    filename = input("Insert filename: ")
    
    print("#### Number analysis - START ####")
    
    analysis_result = read_and_analyze(filename)
    
    
    if analysis_result.startswith("Error:"):
        print(analysis_result)
    else:
        
        print(f"File \"{filename}\" results:")
        print("Count;Sum;Greatest;Average")
        print(analysis_result)
        
    print() 
    print("#### Number analysis - END ####")
    print("Program ending.")