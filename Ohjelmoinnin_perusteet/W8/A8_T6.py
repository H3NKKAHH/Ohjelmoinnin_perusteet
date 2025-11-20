import svgwrite
import os 
from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle



def get_shape_input(prompt_data):

    data = {}
    for key, prompt in prompt_data:
        
        user_input = input(f"- {prompt}")
        data[key] = user_input
    return data

def draw_square(dwg: Drawing) -> None:
    """Kysyy neliön tiedot ja lisää Rect-muodon piirrokseen."""
    print("Insert square")
    try:
        data = get_shape_input([
            ("x", "Left edge position: "),
            ("y", "Top edge position: "),
            ("side", "Side length: "),
            ("fill", "Fill color: "),
            ("stroke", "Stroke color: ")
        ])
        
        
        x = float(data["x"])
        y = float(data["y"])
        side = float(data["side"])
        fill = data["fill"]
        stroke = data["stroke"]

        
        square = Rect(
            insert=(x, y), 
            size=(side, side), 
            fill=fill, 
            stroke=stroke
        )
        dwg.add(square)
        

    except ValueError:
        print("Error!")
    except Exception as e:
        print("Error!")

def draw_circle(dwg: Drawing) -> None:
    
    print("Insert circle")
    try:
        data = get_shape_input([
            ("cx", "Center X position: "),
            ("cy", "Center Y position: "),
            ("r", "Radius: "),
            ("fill", "Fill color: "),
            ("stroke", "Stroke color: ")
        ])
        
        
        cx = float(data["cx"])
        cy = float(data["cy"])
        r = float(data["r"])
        fill = data["fill"]
        stroke = data["stroke"]

        circle = Circle(
            center=(cx, cy), 
            r=r, 
            fill=fill, 
            stroke=stroke
        )
        dwg.add(circle)
        print(f"Circle added: cx={cx}, cy={cy}, radius={r}, fill={fill}")

    except ValueError:
        print("Error!")
    except Exception as e:
        print("Error!")


def save_svg(dwg: Drawing) -> None:

    print("Insert filename:")
    
    
    filename = input("- Filename: ").strip()
    if not filename:
        print("Filename cannot be empty. Save cancelled.")
        return

   
    if not filename.lower().endswith('.svg'):
        filename += '.svg'

    print(f"Saving file to: \"{filename}\"")

    
    if os.path.exists(filename):
        
        confirmation = input("Proceed (y/n)?: ").strip().lower()
        if confirmation != 'y':
            print("Save cancelled by user.")
            return

    try:
       
        
        dwg.write(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    except Exception as e:
        
        print(f"!!! Virhe tallennuksessa: {e}") 



def main():
    
    
    print("Program starting.")
    
    
    dwg = svgwrite.Drawing() 

    while True:
        
        print("\nOptions:")
        print("1. - Draw square")
        print("2. - Draw circle")
        print("3. - Save svg")
        print("0. - Exit")
        
        choice = input("Your choice: ").strip()

        if choice == '1':
            draw_square(dwg)
        elif choice == '2':
            draw_circle(dwg)
        elif choice == '3':
            save_svg(dwg)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")

    print("Program ending.")


if __name__ == "__main__":
    
    main()