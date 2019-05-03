# -*- coding: utf-8 -*-
"""
Created on Thu May  2 03:15:31 2019

@author: Levi
"""

import pandas as pd
import math
from statistics import mean, stdev

a = pd.read_csv("D:\School\Spring Semester\CSCI 4502 Data Mining\Project_Data\Stocks\\ge.us.csv")

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
        

# SMA simple moving average
# for closing prices
sma_rise = []  
sma_fall = []

for i in range(10, length):
    sma_sum = 0
    for j in range(1, 11):
        sma_sum = sma_sum + a.iloc[i - j, 4]
    
    sma = sma_sum/10
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        sma_rise.append(sma)
    else:
        sma_fall.append(sma)
        
  
sma_rise_ave = mean(sma_rise)
sma_rise_std = stdev(sma_rise)

sma_fall_ave = mean(sma_fall)
sma_fall_std = stdev(sma_fall)      
 
# EMA   
ema_rise = []
ema_fall = []

ema_full = [0]
ema = 0
for i in range(1, length):
    ema = a.iloc[i, 4]*.1818 + ema_full[i-1]*.8181
    ema_full.append(ema)
    
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        ema_rise.append(ema)
    else:
        ema_fall.append(ema)
    

ema_rise_ave = mean(ema_rise)
ema_rise_std = stdev(ema_rise)

ema_fall_ave = mean(ema_fall)
ema_fall_std = stdev(ema_fall)


# MOM
mom_rise = []
mom_fall = []

mom = 0
for i in range(5, length):
    mom = (a.iloc[i,4]/a.iloc[i-5,4])*100
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        mom_rise.append(mom)
    else:
        mom_fall.append(mom)
 
mom_rise_ave = mean(mom_rise)
mom_rise_std = stdev(mom_rise)

mom_fall_ave = mean(mom_fall)
mom_fall_std = stdev(mom_fall)


# STCK K%
kper_rise = []  
kper_fall = []
kper_full = []
kper = 0
local_high = 0
local_low = 0
for i in range(15, length):
    local_low = min(a.iloc[i-14:i, 3])
    local_high = max(a.iloc[i-14:i, 2])
    
    kper = ((a.iloc[i, 4] - local_low)/(local_high - local_low))*100
    
    if (kper == math.inf):
        kper = 205
    
    if (math.isnan(kper)):
        kper = 0
    kper_full.append(kper)
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        kper_rise.append(kper)
    else:
        kper_fall.append(kper)
        
kper_rise_ave = mean(kper_rise)
kper_rise_std = stdev(kper_rise)

kper_fall_ave = mean(kper_fall)
kper_fall_std = stdev(kper_fall)
   


# STCK d%
dper_rise = []  
dper_fall = []

dper = 0
for i in range(3, length - 15):
    
    dper = (kper_full[i-3] + kper_full[i-2] + kper_full[i-1])/3
    

    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        dper_rise.append(dper)
    else:
        dper_fall.append(dper)
        
dper_rise_ave = mean(dper_rise)
dper_rise_std = stdev(dper_rise)

dper_fall_ave = mean(dper_fall)
dper_fall_std = stdev(dper_fall)


# MACD   
macd_rise = []
macd_fall = []


macd = 0
for i in range(length - 1):
    macd = a.iloc[i, 4] - ema_full[i-1]*.1818 + ema_full[i-1]
    
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        macd_rise.append(macd)
    else:
        macd_fall.append(macd)
    

macd_rise_ave = mean(macd_rise)
macd_rise_std = stdev(macd_rise)

macd_fall_ave = mean(macd_fall)
macd_fall_std = stdev(macd_fall)


# R%
rper_rise = []  
rper_fall = []

rper = 0
local_high = 0
local_low = 0
for i in range(15, length):
    local_low = min(a.iloc[i-14:i, 3])
    local_high = max(a.iloc[i-14:i, 2])
    
    rper = ((local_low - a.iloc[i, 4])/(local_high - local_low))*100
    
    if (rper == math.inf):
        rper = 205
    
    if (math.isnan(rper)):
        rper = 0
    
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        rper_rise.append(rper)
    else:
        rper_fall.append(rper)
        
rper_rise_ave = mean(rper_rise)
rper_rise_std = stdev(rper_rise)

rper_fall_ave = mean(rper_fall)
rper_fall_std = stdev(rper_fall)


# ADL
adl_rise = []  
adl_fall = []

adl = [0]
adl_new = 0
local_high = 0
local_low = 0
for i in range(1,length):
    local_low = (a.iloc[i, 3])
    local_high = (a.iloc[i, 2])
    close = a.iloc[i, 4]
    denom = local_high - local_low
    if (denom == 0):
        mfm = ((close - local_low) - (local_high - close))/.00001
    else:
        mfm = ((close - local_low) - (local_high - close))/(local_high - local_low)
    mfv = mfm*(a.iloc[i, 5])

    adl_new = mfv + adl[-1]

    adl.append(adl_new)
    
    
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        adl_rise.append(adl_new)
    else:
        adl_fall.append(adl_new)
        
adl_rise_ave = mean(adl_rise)
adl_rise_std = stdev(adl_rise)

adl_fall_ave = mean(adl_fall)
adl_fall_std = stdev(adl_fall)


# CCI 
cci_rise = []  
cci_fall = []

local_high = 0
local_low = 0
typical_price = [0]
moving_average = [0]
mean_deviation = 0
typical_subset = 0
for i in range(20, length):
        
    for k in range(1, 21):
        typical_subset = (typical_subset + (a.iloc[i-k, 2] + a.iloc[i-k, 3] + a.iloc[i-k, 4])/3)
    
    typical_price.append(typical_subset)
    
    
for i in range(20, length):
    
    moving_average.append(sum(typical_price[-20:])/20)

mean_deviation_full = [1]
for i in range(20, length):
    for l in range(1, 19):
        mean_deviation = mean_deviation + abs(typical_price[-l] - moving_average[-l])    
    mean_deviation_full.append(mean_deviation/20)
    
for i in range(length-20):
    cci = (typical_price[i] - moving_average[i])/(.15*mean_deviation_full[i])
    
    if (a.iloc[i,4] - a.iloc[i,1] > 0):    
        cci_rise.append(cci)
    else:
        cci_fall.append(cci)
        
  
cci_rise_ave = mean(cci_rise)
cci_rise_std = stdev(cci_rise)

cci_fall_ave = mean(cci_fall)
cci_fall_std = stdev(cci_fall)   

# RSI

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

accuracy_sum = 0
ema_full_new = [0]
kper_full = [0, 0, 0]
adl = [0]
typical_price = [0]
moving_average = [0]
for i in range(train_length, length):

    sma_sum = 0
    for j in range(1, 11):
        sma_sum = sma_sum + a.iloc[i - j, 4]
    sma = sma_sum/10
    sma_rise_prob = class_probability(sma, sma_rise_ave, sma_rise_std)
    sma_fall_prob = class_probability(sma, sma_fall_ave, sma_fall_std)
    
    
    ema = a.iloc[i, 4]*.1818 + ema_full_new[i-train_length]*.8181
    ema_full_new.append(ema)
    
    ema_rise_prob = class_probability(ema, ema_rise_ave, ema_rise_std)
    ema_fall_prob = class_probability(ema, ema_fall_ave, ema_fall_std)
    
    mom = (a.iloc[i,4]/a.iloc[i-5,4])*100
    
    mom_rise_prob = class_probability(mom, mom_rise_ave, mom_rise_std)
    mom_fall_prob = class_probability(mom, mom_fall_ave, mom_fall_std) 
    
    
    local_low = min(a.iloc[i-14:i, 3])
    local_high = max(a.iloc[i-14:i, 2])
    
    kper = ((a.iloc[i, 4] - local_low)/(local_high - local_low))*100
    
    if (kper == math.inf):
        kper = 205
    
    if (math.isnan(kper)):
        kper = 0
    kper_full.append(kper)
    kper_rise_prob = class_probability(kper, kper_rise_ave, kper_rise_std)
    kper_fall_prob = class_probability(kper, kper_fall_ave, kper_fall_std) 
    
    
    dper = (kper_full[i-train_length-3] + kper_full[i-train_length-2] + kper_full[i-train_length-1])/3
    
    dper_rise_prob = class_probability(dper, dper_rise_ave, dper_rise_std)
    dper_fall_prob = class_probability(dper, dper_fall_ave, dper_fall_std) 
    
    
    macd = a.iloc[i, 4] - ema_full[i-1]*.1818 + ema_full[i-1]
    
    macd_rise_prob = class_probability(macd, macd_rise_ave, macd_rise_std)
    macd_fall_prob = class_probability(macd, macd_fall_ave, macd_fall_std)
    
    local_low = min(a.iloc[i-14:i, 3])
    local_high = max(a.iloc[i-14:i, 2])
    
    rper = ((local_low - a.iloc[i, 4])/(local_high - local_low))*100
    
    rper_rise_prob = class_probability(rper, rper_rise_ave, rper_rise_std)
    rper_fall_prob = class_probability(rper, rper_fall_ave, rper_fall_std)  
    
    
    local_low = (a.iloc[i, 3])
    local_high = (a.iloc[i, 2])
    close = a.iloc[i, 4]
    denom = local_high - local_low
    
    if (denom == 0):
        mfm = ((close - local_low) - (local_high - close))/.00001
    else:
        mfm = ((close - local_low) - (local_high - close))/(local_high - local_low)
    mfv = mfm*(a.iloc[i, 5])

    adl_new = mfv + adl[-1]

    adl.append(adl_new)
    
    adl_rise_prob = class_probability(adl_new, adl_rise_ave, adl_rise_std)
    adl_fall_prob = class_probability(adl_new, adl_fall_ave, adl_fall_std) 
    
    
    if (i == train_length):
        for j in range(train_length , length):
            for k in range(1, 21):
                typical_subset = (typical_subset + (a.iloc[j-k, 2] + a.iloc[j-k, 3] + a.iloc[j-k, 4])/3)
    
            typical_price.append(typical_subset)
    
        for i in range(train_length, length):
            moving_average.append(sum(typical_price[-20:])/20)

        mean_deviation_full = [1]
        for i in range(train_length, length):
            for l in range(1, 19):
                mean_deviation = mean_deviation + abs(typical_price[-l] - moving_average[-l])    
            mean_deviation_full.append(mean_deviation/20)
    
    
    cci = (typical_price[i-train_length] - moving_average[i-train_length])/(.15*mean_deviation_full[i-train_length])
    
    cci_rise_prob = class_probability(cci, cci_rise_ave, cci_rise_std)
    cci_fall_prob = class_probability(cci, cci_fall_ave, cci_fall_std)
    
    
    gain = a.iloc[i,4] - a.iloc[i,1]
    gain_total = 0
    fall_total = 0
    for j in range(i-14, i):
        gain_sub = a.iloc[j,4] - a.iloc[j,1]
        if (gain_sub > 0):
            gain_total = gain_total + gain_sub
        else:
            fall_total = fall_total + abs(gain_sub)
    rsi = 100 - (100/float(1 + (gain_total/14)/(fall_total/14)))      
    rsi_rise_prob = class_probability(rsi, rsi_rise_ave, rsi_rise_std)
    rsi_fall_prob = class_probability(rsi, rsi_fall_ave, rsi_fall_std)
    
    prob_rise = sma_rise_prob*ema_rise_prob*mom_rise_prob*kper_rise_prob*dper_rise_prob*macd_rise_prob*rper_rise_prob*adl_rise_prob*cci_rise_prob*rsi_rise_prob*total_rise_prob
    prob_fall = sma_fall_prob*ema_fall_prob*mom_fall_prob*kper_fall_prob*dper_fall_prob*macd_fall_prob*rper_fall_prob*adl_fall_prob*cci_fall_prob*rsi_fall_prob*total_fall_prob

    
    
    if (prob_rise > prob_fall):
        if (a.iloc[i,4] - a.iloc[i,1] > 0):
            accuracy_sum = accuracy_sum + 1
            
    else:
        if (a.iloc[i,4] - a.iloc[i,1] < 0):
            accuracy_sum = accuracy_sum + 1
        
print(total_rise_prob)
print(total_fall_prob)
        
accuracy = accuracy_sum/test_length
print("The Accuracy is....", accuracy)
     
        
        
        
        
        
        
        
    

