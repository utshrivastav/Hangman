#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:27:44 2017

@author: utshrivastav
"""

import random
import string

WORD_LIST = 'words.txt'

def loadWords():
    '''outputs a bunch of random words
    '''
    print('Loading the words into the game\'s memory...\n')
    fileContent = open(WORD_LIST,'r')
    fileLine = fileContent.readline()
    words = fileLine.split()
    l = len(words)
    print('Total '+str(l)+' words loaded')
    return words

def chooseWord(words):
    '''expects a list of words as input
    and returns a random word as output
    '''
    return random.choice(words)
    
words = loadWords()

def isWordGuessed(secretWord,lettersGuessed):
    '''takes two arguments, one is a secret number and the other is a letter guessed
    outputs a boolean value depending upon whether that guessed letter occurs in the secret word
    '''
    flag = True
    for i in lettersGuessed:
        if i in secretWord:
            pass
        else:
            flag = False
            
    return flag

def getGuessedWord(secretWord,lettersGuessed):
    '''takes in two arguments, secret word and the list of letters guessed so far
    outputs a string which is the formed word from the guesses
    '''
    l = ''
    for i in secretWord:
        if i in lettersGuessed:
            l = l+i
        else:
            l = l+str('_ ')
            
    return l

def getAvailableLetters(lettersGuessed):
    '''takes list of letters guessed as input
    and outputs string of alphabets which are not yet to be guessed
    '''
    l = ''
    for i in string.ascii_lowercase:
        if i in lettersGuessed:
            pass
        else:
            l = l+i
            
    return l

def guessAlreadyMade(g,lettersGuessed):
    if g in lettersGuessed:
        return True
    else:
        return False

def hangman(secretWord):
    '''main game function
    '''   
    length = len(secretWord)
    counter = length
    mainLoop = True
    guessList = []
    print('The length of the secret word is',length,'\n')
    i = 0
    while mainLoop:
        guess = input('Enter a word to make a guess..\n')
        guessLower = guess.lower()
        if i == 0:
            guessList.append(guessLower)
            i += 1
        else:
            flagGuess = guessAlreadyMade(guessLower,guessList)
            if flagGuess:
                print('You have already made this guess..\n')
                continue
                
            else:
                guessList.append(guessLower)
                
        flag = isWordGuessed(secretWord,guessLower)
        answer = getGuessedWord(secretWord,guessList)
        lettersToGuess = getAvailableLetters(guessList)
        if flag:
            print('You have guessed correctly\n')
            print(answer)
            
        else:
            print('You have guessed incorrectly\n')
            print(answer)
            counter -= 1
        print('The letters available are '+lettersToGuess+'\n')
        print('You have '+str(counter)+' chances left!\n')   
        if answer == secretWord:
            print('You have won the game!!!\n')
            mainLoop = False
            print(secretWord)
        elif counter == 0:
            print('You have lost the game!!!\n')
            mainLoop = False
            print(secretWord)
            
secretWord = chooseWord(words).lower()
hangman(secretWord)