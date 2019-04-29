#Calculate average annual percentage return and volatilities over a theoretical one year period
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

###Create an arbitrary model based on the stock market being open 252 days per year
returns = prices_df.pct_change().mean() * 252
returns = pd.DataFrame(returns)
returns.columns = ['final']
returns['change'] = prices_df.pct_change().std() * sqrt(252)

###https://www.pythonforfinance.net/2018/02/08/stock-clusters-using-k-means-algorithm-in-python/
data = np.asarray([np.asarray(returns['final']),np.asarray(returns['change'])]).T
 
X = data
distorsions = []
for k in range(2, 20):
    k_means = KMeans(n_clusters=k)
    k_means.fit(X)
    distorsions.append(k_means.inertia_)
 
