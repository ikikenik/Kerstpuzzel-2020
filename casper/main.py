# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:26:29 2020

@author: Casper
"""
# common:
from fractions import Fraction
import re
import dutch_words

# custom: 
from fraccalculator import FracCalculator
import load
from myfraction import MyFraction


def find_word_with_fraction(fraction, length, add_dutch_vocab = False):
    # tabel laden
    table = load.load_table()
    # tabel omzetten in lijst
    frac_digit_list = create_list(table)
    # calculator aanmaken
    fc = FracCalculator(frac_digit_list, length)
    
    # mogelijk woordenboek toevoegen
    if(add_dutch_vocab):
        fc.add_dutch_vocab()
    
    # zoeken naar breuk en de lijst met mogelijkheden returnen
    return fc.search(fraction)
    
   

# functie om de tabel in een lijst met opties om te zetten:
    # hier gebruik in mijn eigen gemaakte class "myfraction"
    # functie is een beetje slordig
def create_list(table):
    alist = []
    for name, values in table.iteritems():
        for i, value in enumerate(values):
            if( value == "?"):
                    alist.append(MyFraction(Fraction(i+1, name), value))
            if re.match(r"\w", str(value)):
                if(str(value) != "nan"):
                    if(not str(value).isdigit()):
                        alist.append(MyFraction(Fraction(i+1, name), value))
    return alist
                
        
if __name__ == '__main__':
    """
    frac = Fraction(463,195)
    word_length = 2
    
    r1 = find_word_with_fraction(frac, word_length, True)
    
    frac = Fraction(121,48)
    word_length = 2
    r2 = find_word_with_fraction(frac, word_length, True)
    
    frac = Fraction(521,273)
    word_length = 3
    r3 = find_word_with_fraction(frac, word_length, True)
    
    frac = Fraction(62,99)
    word_length = 2
    r4 = find_word_with_fraction(frac, word_length, True)
    """
    frac = Fraction(1749257 , 652080)
    word_length = 5
    r5 = find_word_with_fraction(frac, word_length, True)
    
    # optie 2:
    # result = find_word_with_fraction(frac, word_length, add_dutch_vocab=True)
    
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    
    
    