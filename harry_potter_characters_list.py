# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:19:30 2020

@author: chloe
"""
import csv
with open("characters.csv") as characters:
    characters_reader = csv.DictReader(characters)
    characters_list = []
    for character in characters_reader:
        character_upper = character["name"].upper()
        characters_list.append(character_upper)
    
    

