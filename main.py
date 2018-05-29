#!/usr/bin/python

import random
import argparse

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


class Scrabble:
    file = open('Dictionary.txt', 'r')

    words = []
    for line in file:
        for c in line.split():
            words.append(c)
    points = []

    def __init__(self):
        self.word = args.word
        self.value = args.value

    def mode_m(self, word):

        temp = 0
        try:
            for char in word:
                temp = temp + LETTER_SCORES.get(char.upper())
            return(temp)
        except TypeError:
            return (
                "Value you given is not in alphabet please use: 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z' ")

    def mode_n(self, value):

        value_words = []
        for word in Scrabble.words:
            temp = 0
            for char in word:
                temp = temp + LETTER_SCORES.get(char.upper())
            if temp == value:
                value_words.append(word)

        if not value_words:
            pass
        else:
            return (random.choice(value_words))

    def fun(self):

        if self.word:
            print(Scrabble.mode_m(self,self.word))

        elif self.value:
            if Scrabble.mode_n(self,self.value):
                print(Scrabble.mode_n(self,self.value))
        else:
            print("word with highest score in dictionary is:")
            for word in Scrabble.words:
                temp = 0
                for char in word:
                    temp = temp + LETTER_SCORES.get(char.upper())
                Scrabble.points.append(temp)
            print(Scrabble.words[Scrabble.points.index(max(Scrabble.points))])


if __name__ == '__main__':

    parser = argparse.ArgumentParser("-w for checking value of [word] -v for checking word with given score [value],leave blank for returning word with highest score in dictionary.txt")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-w",
        "--word",
        default="",
        action="store",
        nargs='?',
        help="calculate value of a word that was passed as a command line argument example: (-w dog)"
    )
    group.add_argument(
        "-v",
        "--value",
        action="store",
        default=0,
        nargs="?",
        type=int,
        help="return a word with given value: example: (-v 9)"
    )
    args = parser.parse_args()
    c1 = Scrabble()
    c1.fun()












