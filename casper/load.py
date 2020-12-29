# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:27:04 2020

@author: Casper
"""

import pandas as pd
import os


def load_table():
    dfs = pd.read_excel(os.getcwd() + "\\data\\letters.xlsx", sheet_name=0)
    return dfs