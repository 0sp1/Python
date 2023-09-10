FILE_NAME = "slowkaNiem.csv"
# FILE_NAME = input("File name: ")
import csv
import re
import random
import sys
import os

def main():
    quiz_game()

def quiz_game():
    
    user_input = input("""
Add new word = type 'Add'
Quiz = type 'Quiz'
                       
""").lower().strip()

    match user_input:
        
        case "add": # Adding new words start
            
            while True:
                try:

                    if os.path.exists(FILE_NAME): #checks if file dose exist if not rasies an error
                        word_translation = input("Give word and it's translation 'word,translation' make sure to spell it correcly: ").strip()
                        regex = re.search("(.+ )?.+,.+", word_translation)
                        if regex:
                            word, translation = split(word_translation)
                            open_chcek_file(FILE_NAME, word, translation)
                        else:
                            print("Incorrect input 'word,translation'")
                            pass
                    else:
                        sys.exit("File dose not exists")

                except KeyboardInterrupt:#Stops the program, ctrl + c
                    sys.exit("\nYou stopped the program") 

        case "quiz": #Quiz game start
            quiz()
        case _ :
            sys.exit("Invalid input")

def write_file(file_name, word, translation): # Writes words in to csv file 
    with open(file_name, "a") as csvfile:
        fieldnames = ["word", "translation"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, lineterminator= "\n")

        writer.writerow({'word': word, 'translation': translation})

def open_chcek_file(file_name, word, translation): # Opens and check if word exists in csv file 
    with open(file_name) as csvfile:
        lines = csv.DictReader(csvfile)

        word_exists = any(word in line['word'] for line in lines)
            
        if not word_exists:
            write_file(file_name, word, translation)
        else:
            print("Word already exists")
            pass
           
def split(word_translation): #Splits word in to two
    word, translation = word_translation.split(",")
    return word, translation

def quiz(): #Quiz game
    words = {}
    score = 0
    rounds = input("\nHow many rounds would you like to play: ")
    if rounds.isdigit():
        rounds = int(rounds)
        for _ in range(rounds):
            with open(FILE_NAME) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    words[row['word']] = row['translation']

            word, translation = get_word_and_translation(words)
            user = input(f"{word} = ")

            if user == translation:
                score += 1
                os.system("cls")
            else:
                trys = 3
                for _ in range(3):
                    print(f"Wrong answer you have {trys} left ")
                    user = input(f"{word} = ")
                    if not user == translation:
                        trys -= 1
                        os.system("cls")
                    else:
                        break
        print(f"Your score is: {score}")


                    
                




    else:
        print("Numbers of rounds must to be intager ")


    
    
def get_word_and_translation(words):
    random_key = random.choice(list(words.keys()))
    translation = words.get(random_key)
    return random_key, translation





main()