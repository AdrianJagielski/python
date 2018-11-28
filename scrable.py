#!/usr/bin/python

import random
import argparse
'''Inicjalizacja wartosci za literki, utworzenie slownika'''
SCRABBLES_SCORES = [
                    (1, "E A O I N R T L S U"),
                    (2, "D G"),
                    (3, "B C M P"),
                    (4, "F H V W Y"),
                    (5, "K"),
                    (8, "J X"),
                    (10, "Q Z")
                    ]
LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES for letter in letters.split()}

dictionary_name = 'Dictionary'
dictionary_name += '.txt'



'''
Sprawdzanie czy istnieje 'dictionary' o takiej nazwie, 
jak nie to jest zapytanie o inna nazwe, lub wyjscie
z programu
'''


def check_dic(dictionary_name):
    try:
        open(dictionary_name, 'r')
    except FileNotFoundError:
        print("Couldn`t find ",dictionary_name," Make sure text file is in same directory\n ")
        decision = input("Would like to change dictionary name?(y/n)").upper()
        if decision == 'Y' or  decision == 'YES':
            dictionary_name = input("Enter dictionary name(without filename extension):")
            if '.' not in dictionary_name:
                dictionary_name += '.txt'
            check_dic(dictionary_name)
        else:
            exit()
    return (dictionary_name)

'''
utowrzenie parsera
'''


def createparser():

    parser = argparse.ArgumentParser(
        "leave blank for returning word with highest score in dictionary.txt\n     Else use:")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-w",
        "--word",
        default= "!!!",
        action="store",
        nargs='?',
        help="calculate value of a word that was passed as a command line argument example: (-w dog)"
    )
    group.add_argument(
        "-v",
        "--value",
        action="store",
        default=-1,
        nargs="?",
        type=int,
        help="return a word with given value: example: (-v 9)"
    )
    return (parser)


file = open(check_dic(dictionary_name), 'r')

class Scrabble():
    '''
    inicjalizacja zmiennych potrzebnych pozniej w programie
    words = lista zawierajaca slowa pochadzace z pliku tekstowego , podzielona na linie
     points = lista zawierajaca przeliczenie slow na wartosci punktowe
     value_words = lista slow pukntowanych za wartosc podana przy starcie
     temp = wartosci tymczasowa do utrzymyania najwiekszego wyniku
     '''
    words = []
    points = []
    value_words = []
    temp = 0
    parser = createparser()
    args = parser.parse_args()
    word = args.word
    value = args.value

    for line in file:
        for c in line.split():
            words.append(c)

    def __init__(self):
        pass

    def __str__(self):
        pass

    def mode_m(self, word):

        try:
            for char in word:
                if char.upper() in LETTER_SCORES:
                    Scrabble.temp = Scrabble.temp + LETTER_SCORES.get(char.upper())

            return(Scrabble.temp)
        except TypeError:
            return (
                "Value you given is not in alphabet please use: 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z' ")

    def mode_n(self, value):
        for word in Scrabble.words:
            temp = 0
            for char in word:
                if char.upper() in LETTER_SCORES:
                    temp = temp + LETTER_SCORES.get(char.upper())
            if temp == value:
                Scrabble.value_words.append(word)

        if not Scrabble.value_words:
            pass
        else:
            return(random.choice(Scrabble.value_words))

    def fun(self):

        if self.word and self.word!='!!!':
            print(Scrabble.mode_m(self,self.word))

        elif self.value and self.value!=-1:
            if Scrabble.mode_n(self,self.value):
                print(Scrabble.mode_n(self,self.value))

        elif self.value ==-1 and self.word =='!!!':
            print("word with highest score in dictionary is:")
            for word in Scrabble.words:
                temp = 0
                for char in word:
                    temp = temp + LETTER_SCORES.get(char.upper())
                Scrabble.points.append(temp)
            print(Scrabble.words[Scrabble.points.index(max(Scrabble.points))],"[",max(Scrabble.points) ,"]")
            return (Scrabble.words[Scrabble.points.index(max(Scrabble.points))])


if __name__ == '__main__':
    c1 = Scrabble()
    c1.fun()
