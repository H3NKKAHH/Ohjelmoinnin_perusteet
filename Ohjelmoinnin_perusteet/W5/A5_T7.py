DELIMITER = ','

def collect_words():
    words = []
    print("Program starting.")
    while True:
        user_input = input("Insert word(empty stops): ")
        
        if not user_input:
            break
        
        words.append(user_input)
    
    return DELIMITER.join(words)

def analyse_words(words_string):
    words = list(filter(None, words_string.split(DELIMITER)))
    
    word_count = len(words)
    
    character_count = sum(len(word) for word in words)
    
    if word_count > 0:
        average_word_length = character_count / word_count
    else:
        average_word_length = 0.0

    
    print(f"- {character_count} Characters")
    
    
    print(f"- {word_count} Words")
    
    
    print("- {:.2f} Average word length".format(average_word_length))

def main_function():
    collected_words_string = collect_words()
    
    analyse_words(collected_words_string)
    
    print("Program ending.")

if __name__ == "__main__":
    main_function()