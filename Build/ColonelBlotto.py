# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:13:47 2020
Goal: Create a python program that can interact with data entered into an Excel
    spreadsheet or google doc for the answers to 
@author: Julian Chastain
"""

from typing import List

from pathlib import Path

import pyexcel

master = None
name = 2
low = 3
high = 13
def produce_class(custom_function = master):
    class strategy:
        def __init__(self, name = None, allocations = None):
            self.person = name
            self.allocations = [] if allocations is None else allocations
            self.score = 0
            
        def clash(self, other: 'strategy'):
            self.score += custom_function(self, other)
            
        def __eq__(self, other: 'strategy'):
            return self.score == other.score
        
        def __lt__(self, other: 'strategy'):
            return self.score < other.score
        
        def __repr__(self):
            return f'{self.person}: \t{self.score}'
     
    def default_function(first, second):
        value = 0
        for x,y in zip(first.allocations, second.allocations):
            if x > y:
                value += 1
        return value
        
    if custom_function is None:
        custom_function = default_function
        
    return strategy

def excel_to_list(file: str) -> List['strategy']:
    strategies = []
    lol = pyexcel.get_sheet(file_name=file, start_row=1).rows()
    for list_ in lol:
        strategies.append(produce_class()(list_[name], list_[low:high]))
    return strategies
        
    
def clasher(list_: List['strategy']) -> List['strategy']:
    second_list = []
    while(list_):
        st = list_.pop()
        for item in list_ + second_list:
            st.clash(item)
        second_list.append(st)
    return second_list

file = Path.cwd()
l = reversed(sorted(clasher(excel_to_list(str(next(file.rglob("*.xlsx")))))))
for s in l:
    print(s)


        

