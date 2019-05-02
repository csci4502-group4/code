# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:28:19 2019

@author: Levi
"""

import pandas as pd
import math
from statistics import mean, stdev

a = pd.read_csv("D:\School\Spring Semester\CSCI 4502 Data Mining\Project_Data\Stocks\\msft.us.csv")


length = len(a)


train_length = int(length * .75)
test_length = length - train_length
rise = pd.DataFrame(columns={'Open', 'High', 'Low', 'Close', 'Volume'})
fall = pd.DataFrame(columns={'Open', 'High', 'Low', 'Close', 'Volume'})
total_prob_sum = 0

for i in range(length):
    if (a.iloc[i,4] - a.iloc[i,1] > 0):
        total_prob_sum = total_prob_sum + 1
        
total_rise_prob = total_prob_sum/length
total_fall_prob = 1 - total_rise_prob

for i in range(train_length):
    if (a.iloc[i,4] - a.iloc[i,1] > 0):
        rise = rise.append(a.loc[i])
        rise = rise.reindex(a.columns, axis=1)
    else:
        fall = fall.append(a.loc[i])
        fall = fall.reindex(a.columns, axis=1)
        
rise_ave = rise.mean(axis=0)
fall_ave = fall.mean(axis=0)

rise_std = rise.std(axis=0)
fall_std = fall.std(axis=0)

rsi_rise = []
rsi_fall = []

for i in range(14, train_length):
    
    gain = a.iloc[i,4] - a.iloc[i,1]
    gain_total = 0
    fall_total = 0
    for j in range(i-14, i):
        gain_sub = a.iloc[j,4] - a.iloc[j,1]
        if (gain_sub > 0):
            gain_total = gain_total + gain_sub
        else:
            fall_total = fall_total + abs(gain_sub)
        
    if (gain > 0):
        rsi_rise.append(100 - (100/float(1 + (gain_total/14)/(fall_total/14))))
    else:
        rsi_fall.append(100 - (100/float(1 + (gain_total/14)/(fall_total/14))))

rsi_rise_ave = mean(rsi_rise)
rsi_rise_std = stdev(rsi_rise)

rsi_fall_ave = mean(rsi_fall)
rsi_fall_std = stdev(rsi_fall)

def class_probability(x, mean, std):
    return (1 / (math.sqrt(2*math.pi) * std)) * math.exp(-(math.pow(x-mean,2)/(2*math.pow(std,2))))



prob_rise = 0
prob_fall = 0

accuracy_sum = 0

for i in range(train_length, length):
    rise_cond_prob = 1
    fall_cond_prob = 1
    
    for j in range(len(rise_ave)-1):
        rise_cond_prob = rise_cond_prob * class_probability(float(a.iloc[i,j+1]), rise_ave[j], rise_std[j])
        fall_cond_prob = fall_cond_prob * class_probability(float(a.iloc[i,j+1]), fall_ave[j], fall_std[j])
        
     
    sum_span = 1
    for k in range(i-14, i):
        sum_span = sum_span + (float(a.iloc[k,4]) - float(a.iloc[k,1]))
    
    if (sum_span == 0):
        rsi_val = 0
    else:        
        rsi_val = (100 - (100/sum_span))   
    
    rise_cond_prob = rise_cond_prob * class_probability(rsi_val, rsi_rise_ave, rsi_rise_std)
    fall_cond_prob = fall_cond_prob * class_probability(rsi_val, rsi_fall_ave, rsi_fall_std)
      
    
    prob_rise = rise_cond_prob*total_rise_prob
    prob_fall = fall_cond_prob*total_fall_prob
    
    
    if (prob_rise > prob_fall):
        if (a.iloc[i,4] - a.iloc[i,1] > 0):
            accuracy_sum = accuracy_sum + 1
            
    else:
        if (a.iloc[i,4] - a.iloc[i,1] < 0):
            accuracy_sum = accuracy_sum + 1
        
print(total_rise_prob)
print(total_fall_prob)
        
accuracy = accuracy_sum/test_length
print("Shitty accuracy is....", accuracy)
    
    
    
    
    
    
    
    