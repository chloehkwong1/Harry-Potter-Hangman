# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:09:52 2020

@author: chloe
"""
import random
from harry_potter_characters_list import characters_list

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_name():
    name = random.choice(characters_list)
    return name

def create_dashes(name):
    name_dash = ""
    for letter in name:
        if letter is " ":
            name_dash += " "
        else:
            name_dash += "-"
    return name_dash

def guess_name(name, name_dash, hangman_pics_list):
    letters_guessed = []
    attempts_left = 10
    
    print("""Greetings fellow wizards and muggles! Welcome to Harry Potter Hangman.
          Will you be able to beat Voldemort and become a hero like Harry Potter?""")
    print("\n")
 
    while attempts_left > 0 and "-" in name_dash:
        print("Can you guess this name? " + str(name_dash))
        print("\n")
        print("You have guessed these letters so far: " + str(letters_guessed) + ".")
        letter = input("Please guess a letter!(or the full name if you're feeling lucky!'): ").upper()
        print("\n")
        
        if len(letter) == len(name_dash):
            if letter == name:
                name_dash = name
                print("Congratulations! You have figured out the name :). It was " + str(name) + "!")
            else:
                print("That name is incorrect, please try again.")
        elif len(letter) > 1:
            print("Oi! Only 1 letter at a time please.")
            print("\n")
        elif letter not in alphabet:
            print("That isn't a letter! Please try again.")
            print("\n")
        elif letter in letters_guessed:
                print("You've already guessed this letter. Choose a different one!")
                print("\n")
        elif letter not in letters_guessed and letter in name:
            indices_list = []
            for index in range(len(name)):
                if name[index] == letter:
                    indices_list.append(index)
            for index in indices_list:
                name_dash = name_dash[:index] + letter + name_dash[index+1:]  
            letters_guessed += letter
            if name_dash == name:
                print("Congratulations! You have figured out the name :). It was " + str(name) + "!")
            else:
                print("Congratulations! You guessed a letter correctly! Here is the name so far: " + str(name_dash))
                print("\n")
                
            
        else:
            letters_guessed.append(letter)
            if attempts_left == 1:
                print("You have " + str(attempts_left - 1) + " attempts left.")
                print("\n")
                print(hangman_pics_list[10 - attempts_left])
                print("\n")
                print("Sadly you did not manage to guess the name :( The answer is " + str(name) +". Better luck next time!")
                attempts_left -= 1
            else:   
                print("Uh oh... that isn't a letter in the name. Better luck next guess.")
                print("You have " + str(attempts_left - 1) + " attempts left.")
                print("\n")
                print(hangman_pics_list[10 - attempts_left])
                print("\n")
                attempts_left -= 1
    
    
    # if attempts_left == 0 and "-" in name_dash:
    #     print(hangman_pics_list[9])
    #     print("Sadly you did not manage to guess the name :( The answer is " + str(name) +". Better luck next time!")
    
    # else:
    #     if name_dash == name:
    #         print("Congratulations! You have figured out the name :)")
            
            
hangman_pics_list = ['''
                     
                     
      ===''', '''
       |
       |
       |
      ===''', '''
       +
       |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

def play_game():
    name = random_name()
    name_dash = create_dashes(name)
    guess_name(name, name_dash, hangman_pics_list)
    while input("Do you want to play again (Y/N)?").upper() == "Y":
        name = random_name()
        name_dash = create_dashes(name)
        guess_name(name, name_dash, hangman_pics_list)
        
if __name__ == "__main__":
    play_game()           

    
    
     
     
