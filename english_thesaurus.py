import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def check_word(word):   
    if word in data.keys():
        return(word)
    elif word.lower() in data.keys(): 
        return(word.lower())
    else:
        sim_word = get_close_matches(word, data.keys())
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