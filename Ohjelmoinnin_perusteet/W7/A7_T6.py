import random
import sys

random.seed(1234)

options_map = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def ascii_art(val):
    
    art = {
        # 1: Kivi
        1: ["    _______", 
            "---'   ____)", 
            "      (_____)", 
            "      (_____)", 
            "      (____)", 
            "---.__(___)"], 
        # 2: Paperi
        2: ["      _______",
            "---'    ____)____",
            "            ______)",
            "           _______)",
            "          _______)",
            "---.__________)"],
        # 3: Sakset
        3: ["    _______",
            "---'   ____)____",
            "          ______)",
            "        __________) # Huom: Tämän rivin pituus vaikuttaa muiden symbolien tasaamiseen",
            "      (____)", 
            "---.__(___)"]
    }
    
    return art.get(val, ["", "", "", "", "", ""]) 

def print_result(player_choice_str, bot_choice_str, winner, reason, player_name, opponent_name):
    print("Rock! Paper! Scissors! Shoot!\n", flush=True)
    print(f"{player_choice_str}", flush=True)
    print("#########################", flush=True)
    
    player_choice_key = player_choice_str.split(' ')[-1].capitalize().replace('.', '')
    bot_choice_key = bot_choice_str.split(' ')[-1].capitalize().replace('.', '')
    
    player_art_num = options_map.get(player_choice_key)
    bot_art_num = options_map.get(bot_choice_key)
    
    player_art = ascii_art(player_art_num)
    bot_art = ascii_art(bot_art_num)

    for i in range(6): 
        print(f"{player_art[i]}", flush=True)
    
    print("#########################", flush=True)
    print(f"{bot_choice_str}", flush=True)

    for i in range(6): 
        print(f"{bot_art[i]}", flush=True)

    print("#########################", flush=True)
    
    if winner == "Draw":
        print(f"Draw! Both players chose {player_choice_key.lower()}.", flush=True)
    elif winner == "Player":
        print(f"{player_name} beats {opponent_name}. {reason}.", flush=True)
    else:
        print(f"{opponent_name} beats {player_name}. {reason}.", flush=True)

options_list = ["", "Rock", "Paper", "Scissors"]

player_wins = 0
player_losses = 0
player_draws = 0
bot_wins = 0
bot_losses = 0
bot_draws = 0

print("Program starting.", flush=True)
player_name = input("Insert player name: ")
opponent_name = "RPS-3PO"
print(f"Welcome {player_name}!", flush=True)
print(f"Your opponent is {opponent_name}.", flush=True)
print("Game starts...", flush=True)

while True:
    print("\nOptions:", flush=True)
    print("1 - Rock", flush=True)
    print("2 - Paper", flush=True)
    print("3 - Scissors", flush=True)
    print("0 - Quit game", flush=True)
    
    try:
        player_choice_num = int(input("Your choice:"))
    except ValueError:
        print("Invalid input. Please enter a number (0-3).", flush=True)
        continue

    if player_choice_num == 0:
        break
    elif player_choice_num in [1, 2, 3]:
        bot_choice_num = random.randint(1, 3)
        
        player_choice_str = options_list[player_choice_num]
        bot_choice_str = options_list[bot_choice_num]
        
        player_full_choice = f"{player_name} chose {player_choice_str.lower()}."
        bot_full_choice = f"{opponent_name} chose {bot_choice_str.lower()}."
        
        winner = "Draw"
        reason = ""

        if player_choice_num == bot_choice_num:
            player_draws += 1
            bot_draws += 1
        else:
            if (player_choice_num == 1 and bot_choice_num == 3):
                winner = "Player"
                reason = f"{player_choice_str} beats {bot_choice_str.lower()}"
                player_wins += 1
                bot_losses += 1
            elif (player_choice_num == 2 and bot_choice_num == 1):
                winner = "Player"
                reason = f"{player_choice_str} beats {bot_choice_str.lower()}"
                player_wins += 1
                bot_losses += 1
            elif (player_choice_num == 3 and bot_choice_num == 2):
                winner = "Player"
                reason = f"{player_choice_str} beats {bot_choice_str.lower()}"
                player_wins += 1
                bot_losses += 1
            else:
                winner = "Bot"
                if bot_choice_num == 1 and player_choice_num == 3:
                    reason = f"{bot_choice_str} beats {player_choice_str.lower()}"
                elif bot_choice_num == 2 and player_choice_num == 1:
                    reason = f"{bot_choice_str} beats {player_choice_str.lower()}"
                elif bot_choice_num == 3 and player_choice_num == 2:
                    reason = f"{bot_choice_str} beats {player_choice_str.lower()}"
                bot_wins += 1
                player_losses += 1

        print_result(player_full_choice, bot_full_choice, winner, reason, player_name, opponent_name)

    else:
        print("Invalid option. Please choose from 1, 2, 3, or 0.", flush=True)
        
print("\nResults:", flush=True)
print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})", flush=True)
print(f"{opponent_name} - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})", flush=True)
print("Program ending.", flush=True)