from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
import numpy as np
from scipy.cluster.vq import kmeans,vq
import pandas as pd
import pandas_datareader as dr
from math import sqrt
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

#Load our data set and convert it into a list
data_table = pd.read(our_Data_set)
names = data_table[0][1:][0].tolist()

#Iterate through the data and create a list with all of the stock "Names"
#i.e. 'GOOG', 'AAPL', etc...
prices_list = []

for name in names:
    try:
        prices = dr.DataReader(ticker,,'01/01/2017')['Adj Close']
        prices = pd.DataFrame(prices)
        prices.columns = [name]
        prices_list.append(prices)
    except:
        pass
    prices_df = pd.concat(prices_list,axis=1)