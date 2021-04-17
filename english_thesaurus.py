from difflib import get_close_matches
import mysql.connector

connection = mysql.connector.connect(
user = "ardit700_student", 
password = "ardit700_student", 
host = "108.167.140.122", 
database = "ardit700_pm1database"
)

cursor = connection.cursor()

def check_word(word):   
    word1 = word.lower()
    word_list = [word1, word1.title(), word1.upper()]

    for i in word_list:
        query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{i}'")
        results = cursor.fetchall()
        
        if results:
            return results
    
    query1 = cursor.execute("SELECT Expression from Dictionary")
    keys = [b[0] for b in cursor.fetchall()]
    sim_word_list = []
    
    for i in word_list:
        if len(get_close_matches(i, keys)) > 0:
            sim_word_list.append(get_close_matches(i, keys)[0])

    sim_word = get_close_matches(word, sim_word_list)

    if len(sim_word) > 0:
        while True:
            user_new_word_y_n = input(f"Did you mean {sim_word[0]}?\n[yes] | [no] ")
            
            if user_new_word_y_n == "yes":
                query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{sim_word[0]}'")
                results = cursor.fetchall()
                return results
                
            elif user_new_word_y_n == "no":
                print("Word not found")
                return 0
                
            else:
                print('Type "yes" or "no"')
        
    else:
        print("Word not found")
        return 0

    

def definition(results):
    for result in results:
        print(result[1])

while True:
    word = input("Word: ")
    word = check_word(word)
    if word != 0:
        definition(word)