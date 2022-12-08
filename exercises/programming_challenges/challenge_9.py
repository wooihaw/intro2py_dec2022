# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:53:28 2022

@author: wooihaw
"""
from random import choice, shuffle
animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot',
'gorilla', 'dolphin', 'snake']

while True:
    answer = choice(animals)
    word = list(answer)
    shuffle(word)
    anagram = ''.join(word)
    guess = input(f"What is this animal -> '{anagram}'? ")
    if guess == answer:
        print("You are a genius")
    elif guess.lower() == 'q':
        break
    else:
        print(f"You are wrong. The answer is {answer}")
    