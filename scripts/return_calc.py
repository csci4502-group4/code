# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:34:38 2019

@author: Levi
"""
import sys
import pandas as pd


def main(argv):
    
    # Correctly parse in the arguments
    file = pd.read_csv(argv[1])
    start_date = argv[2]
    end_date = argv[3]
    
    # Set up some variables 
    found_start = 0 
    found_end = 0
    i = 0
    
    while (i < len(file)):
        if (file.iloc[i,0] == start_date):
            found_start = 1
            start_close = file.iloc[i,4]
                
        if (file.iloc[i,0] == end_date):
            found_end = 1
            end_close = file.iloc[i,4]
                
        if (found_start == 1 and found_end == 1):            
            ret = (end_close - start_close)/start_close
            print("Return: ", ret)
            break
        i = i + 1
                
    if (found_start == 0):
        print("Date not present in data set: ", start_date)
  
    if (found_end == 0):
        print("Date not present in data set: ", end_date)
    

if __name__ == '__main__':
    argv = sys.argv
    main(argv)