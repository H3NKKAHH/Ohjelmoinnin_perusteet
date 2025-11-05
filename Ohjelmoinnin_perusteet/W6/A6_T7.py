import os
import codecs
import time 

PLAYER_PROGRESS_FILE = 'player_progress.txt'
PLACE_NAMES = {
    0: 'home',
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}


GAME_DATA = {
    1: ("Cneg.o.Lrne.bs.gur.Sbhe.Rzceref.", "1;2;bgubfcnynpr"),
    2: ("Yvir.ybat.naq.cebfcre.gur.Rzcrebe.", "2;3;vugryyvhfcnynpr"),
    3: ("Gur.Ebg13.vpure.vf.fb.rnfl.gb.fbyir.", "3;4;irfcbafvnavfcnynpr"),
    4: ("Rira.zber.qrirybe", "4;0;ubzrcynpr") 
}
# -----------------------------------------------------

def rot13_decode(text):
    return codecs.encode(text, 'rot_13')

def get_current_progress():
    
    if not os.path.exists(PLAYER_PROGRESS_FILE) or os.stat(PLAYER_PROGRESS_FILE).st_size == 0:
        initial_progress = "current_location;next_location;passphrase\n0;1;qvfpvcyvar"
        with open(PLAYER_PROGRESS_FILE, 'w') as f:
            f.write(initial_progress + '\n')
        
        lines = initial_progress.split('\n')
        last_line = lines[-1]
    else:
        
        with open(PLAYER_PROGRESS_FILE, 'r') as f:
            lines = f.readlines()
        
        
        last_line = ""
        for line in reversed(lines):
            stripped = line.strip()
            if stripped and stripped.count(';') == 2 and stripped != 'current_location;next_location;passphrase':
                last_line = stripped
                break
        
        
        if not last_line:
             last_line = "0;1;qvfpvcyvar"

    parts = last_line.split(';')
    if len(parts) != 3:
        
        return 0, 1, 'qvfpvcyvar'
    
    current_loc = int(parts[0])
    next_loc = int(parts[1])
    passphrase = parts[2]
    return current_loc, next_loc, passphrase

def update_progress(ciphered_message_line, next_step_line):
    with open(PLAYER_PROGRESS_FILE, 'a') as f:
        f.write(ciphered_message_line + '\n')
        if next_step_line:
            f.write(next_step_line + '\n')

def run_program():
    current_id, next_id, cipher_pass = get_current_progress()

    
    if current_id == 4 and next_id == 0:
        print("All emperors visited. Mission complete.")
        return

    plain_pass = rot13_decode(cipher_pass)
    
    print("Travel starting.")
    print(f"Currently at {PLACE_NAMES.get(current_id, 'Unknown')}.")
    print(f"Travelling to {PLACE_NAMES.get(next_id, 'Unknown')}...")
    
   
    if next_id in GAME_DATA:
        cipher_msg_line, next_step_line = GAME_DATA[next_id]
        plain_msg_line = rot13_decode(cipher_msg_line)
        
        
        print(f"...Arriving to the {PLACE_NAMES.get(next_id, 'Unknown')}.")
        print("Passing the guard at the entrance.")
        print(f'"{plain_pass.upper()}"')

        
        print("Looking for the message in the palace...")
        print("Ah, there it is! Seems cryptic.")
        
        
        plain_text_file_name = f"{next_id}-{plain_pass}.txt"
        with open(plain_text_file_name, 'w') as f:
            f.write(plain_msg_line + '\n')
            
       
        update_progress(cipher_msg_line, next_step_line)

        
        print("[Game] Progress autosaved!")
        print("Deciphering Emperor's message...")
        print("Looks like I've got now the plain version copy of the Emperor's message.")
        print("Time to leave.")
    
    
    print("Travel ending.")

if __name__ == "__main__":
    run_program()