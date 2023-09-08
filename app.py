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
        
        case "add":
            
            while True:
                try:

                    if os.path.exists(FILE_NAME):
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

                except KeyboardInterrupt:
                    sys.exit("\nYou stopped the program")

        case "quiz":
            quiz()

def write_file(file_name, word, translation):
    with open(file_name, "a") as csvfile:
        fieldnames = ["word", "translation"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, lineterminator= "\n")

        writer.writerow({'word': word, 'translation': translation})

def open_chcek_file(file_name, word, translation):
    with open(file_name) as csvfile:
        lines = csv.DictReader(csvfile)

        word_exists = any(word in line['word'] for line in lines)
            
        if not word_exists:
            write_file(file_name, word, translation)
        else:
            print("Word already exists")
            pass
           
def split(word_translation):
    word, translation = word_translation.split(",")
    return word, translation

def quiz():
    with open(FILE_NAME) as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            print(row['word'])

    




main()