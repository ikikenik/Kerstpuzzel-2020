# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:21:00 2020

@author: Casper
"""

import load
from fractions import Fraction
from myfraction import MyFraction
import re
import dutch_words

     
class FracCalculator():
    
    # constructor class: 
    #   alist: lijst met de breuk en de digit
    def __init__(self, alist, length):
        self.digit_list = alist
        self.found_fracs = []
        self.tracker = 0
        self.length = length
        self.vocab_added = False
        
    # gebruiken als je de zoekruimte wilt beperken tot bestaande nederlandse woorden:
    def add_dutch_vocab(self):
        self.vocab_added = True
        self.vocab = [i for i in dutch_words.get_ranked() if len(i) == self.length]
    
    # aanroepen om te starten met zoeken:
    def search(self, frac):
        self.goal_frac = frac
        
        self.check_frac(Fraction(0,1), "", self.length)
        print(self.found_fracs)
        return (self.found_fracs)
        
    # recursieve functie:
    def check_frac(self, current_frac, current_word, count):
        
        # base case 1 (if not in vocab)
        if(self.vocab_added and count < self.length):
            if not any(current_word.lower() in s for s in self.vocab):
                return
        
        # base case 2 (if frac too high):
        if(current_frac > self.goal_frac):
            return
                
        # base case 3 (if length reached):
        if(count == 0):
            print(current_word)
            # checken of de breuk overeenkomt met de gezochte breuk:
            if(current_frac == self.goal_frac):
                self.found_fracs.append(current_word)
        
        # base case 4: minimum possible still too high:
        if(current_frac + count*Fraction(1,20) > self.goal_frac):
            return
        
        # base case 5: maximum passible still too low:
        if(current_frac + count*Fraction(29,12) < self.goal_frac):
            return
        
        # als aan geen van alle bovenstaande voorwaarden is voldaan, verder zoeken:
        else:
            for i, item in enumerate(self.digit_list):
                
                # breuk optellen bij bestaande breuk, karakter toevoegen aan huidige woord:
                self.check_frac(current_frac + item.frac, current_word + item.digit, count - 1)
                
                # tracker output:
                if(count == self.length):
                    self.tracker = i/len(self.digit_list)
                    print("searching: {}%".format(round(self.tracker*100, 3)))
                if(count == self.length-1):
                    self.tracker += 1/(len(self.digit_list)*len(self.digit_list))
                    print("searching: {}%".format(round(self.tracker*100, 3)))
            
