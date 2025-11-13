import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Rotor:
    def __init__(self, wiring_str, name):
        self.wiring = wiring_str
        self.name = name
        self.position = 0

    def set_position(self, pos):
        self.position = pos

    def rotate(self):
        self.position = (self.position + 1) % 26

    def forward(self, char_index):
        offset = (char_index + self.position) % 26
        scrambled_char = self.wiring[offset]
        scrambled_index = ALPHABET.find(scrambled_char)
        return (scrambled_index - self.position + 26) % 26

    def reverse(self, char_index):
        offset = (char_index + self.position) % 26
        char_in_wiring = ALPHABET[offset]
        index_in_wiring = self.wiring.find(char_in_wiring)
        return (index_in_wiring - self.position + 26) % 26


class Reflector:
    def __init__(self, wiring_str, name):
        self.wiring = wiring_str
        self.name = name

    def reflect(self, char_index):
        reflected_char = self.wiring[char_index]
        return ALPHABET.find(reflected_char)


class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def _rotate_wheels(self):
        self.rotors[0].rotate()

    def set_initial_positions(self, positions):
        for i, pos in enumerate(positions):
            self.rotors[i].set_position(pos)

    def process_char(self, char):
        if char not in ALPHABET:
            return char
            
        self._rotate_wheels()

        char_index = ALPHABET.find(char)
        
        current_index = char_index
        for rotor in self.rotors:
            current_index = rotor.forward(current_index)
            
        current_index = self.reflector.reflect(current_index)
        
        for rotor in reversed(self.rotors):
            current_index = rotor.reverse(current_index)
            
        return ALPHABET[current_index]

    def process_row(self, text):
        converted_row = ""
        
        self.set_initial_positions([0, 0, 0])

        for char in text.upper():
            
            if char in ALPHABET:
                
                converted_char = self.process_char(char)
                converted_row += converted_char
                
                print(f"Character '{char}' illuminated as '{converted_char}'")
            else:
                converted_row += char
                
        print(f"Converted row - '{converted_row}'.")
        print("")
        return converted_row


def load_config(filename):
    CONFIGS = {
        "iconf1.txt": {
            "Rotor I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "Rotor II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "Rotor III": "BDFHJLCPRTXVZNYEIWGAKMSUQO",
            "Reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        },
        "iconf2": {
            "Rotor I": "QAZWSXEDCRFVTGBYHNUJMIKOLP",
            "Rotor II": "PLMOKNIBJHVGYTFCXDRZESWAUQ",
            "Rotor III": "MNBVCXZLKJHGFDSAPOIUYTREWQ",
            "Reflector": "NOPQRSTUVWXYZABCDEFGHIJKLM"
        },
        "iconf3": {
            "Rotor I": "ZBFHUYXLTKOSQPAEGNIRMWJDVC",
            "Rotor II": "XNZJGBLHVUDFOQPTCIAMKSWYER",
            "Rotor III": "KPCYGRMSWLJOFTBUVNXQAIHZED",
            "Reflector": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        }
    }
    
    config = CONFIGS.get(filename)
    if config is None:
        print(f"Error: Configuration '{filename}' not found. Using iconf1.txt defaults.")
        config = CONFIGS["iconf1.txt"]

    rotors_config = {
        'Rotor I': config['Rotor I'],
        'Rotor II': config['Rotor II'],
        'Rotor III': config['Rotor III']
    }
    reflector_wiring = config['Reflector']
    
    return rotors_config, reflector_wiring


def main():
    print("Program starting.")
    
    config_filename = input("Insert config(filename): ")
    
    plugs_choice = input("Insert plugs (y/n)?: ")
    if plugs_choice.lower() == 'n':
        print("No extra plugs inserted.")
    
    rotors_config, reflector_wiring = load_config(config_filename)
    
    rotor_i = Rotor(rotors_config['Rotor I'], "Rotor I")
    rotor_ii = Rotor(rotors_config['Rotor II'], "Rotor II")
    rotor_iii = Rotor(rotors_config['Rotor III'], "Rotor III")
    
    reflector = Reflector(reflector_wiring, "Reflector B")
    
    enigma = EnigmaMachine(rotors=[rotor_i, rotor_ii, rotor_iii], reflector=reflector)
    
    print("Enigma initialized.")
    print("")

    while True:
        try:
            text_input = input("Insert row (empty stops): ")
            
            if not text_input:
                break
            
            enigma.process_row(text_input.upper())
            
        except EOFError:
            break
            
    print("Enigma closing.")
    
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    main()


# KOODI ANTAA TEHTÄVÄNANNOSTA POIKETEN VÄÄRÄN TULOKSEN. TAPPELIN TÄMÄN KANSSA 2H MUTTA EN SAA TOIMIMAAN.