import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def check_word(word):   
    word_small = word.lower()
    if word_small in data.keys():
        return(word_small)
    elif word_small.title() in data.keys(): 
        return(word_small.title())
    elif word_small.upper() in data.keys():
        return(word_small.upper())
    else:
        sim_word_upper = get_close_matches(word_small.upper(), data.keys())[0]
        sim_word_small = get_close_matches(word_small, data.keys())[0]
        sim_word_capital = get_close_matches(word_small.title(), data.keys())[0]
        sim_word = get_close_matches(word, [sim_word_capital, sim_word_small, sim_word_upper])
        if len(sim_word) > 0:
            while True:
                user_new_word_y_n = input(f"Did you mean {sim_word[0]}?\n[yes] | [no] ")
                if user_new_word_y_n == "yes":
                    return(sim_word[0])
                elif user_new_word_y_n == "no":
                    print("Word not found")
                    return 0
                else:
                    print('Type "yes" or "no"')
        else:
            print("Word not found")
            return 0

def definition(word):
    n = 0
    for i in data[word]:
        print(data[word][n])
        n = n+1

while True:
    word = input("Word: ")
    word = check_word(word)
    if word != 0:
        definition(word)