# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:37:21 2020

@author: Casper
"""


class MyFraction():
    def __init__(self, frac, digit):
        self.frac = frac
        self.digit = digit
        
    def __str__(self):
        return "{}, {}".format(self.frac, self.digit)
        
        