"""
File: data_test.py
Authors: Jonathan Qin
Description: Pre-project test and experimentation with data processing
"""

from time import time
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

#import os
#import quantsc as Qsc

def dataPreprocessing(data):
    """_summary_
    transpose, clean, normalize data
    
    Args:
        data (df): dataframe of time series
    """
    #removing weekends
    #Convert DateTime column to datetime object
    data = data[data['DateTime'].dt.weekday < 5].reset_index(drop=True)
    
    #remove after hours

    #remove holidays
        
    #tranpose, columns become indices
    data_T = data.transpose() #or data.T    
    dataVisualization(data_T)
    
def gramianAngularField():
    pass
    

    
def dataVisualization(data):
    """
    display time series data

    Args:
        data (df): time series data to be displayed
    """
    plt.figure()
    #plt.plot(data)
    plt.title(data.index[1])
    plt.xlabel("DateTime")
    plt.ylabel("Price")
    
    x = data.loc[data.index[0], :]
    y = data.loc[data.index[1], :]
    
    plt.plot(x, y)
    plt.show()
    

def main():
    stock_list = ['SPY', 'PFE', 'AAPL']
    data = yf.download(stock_list, start = "2012-8-16", end = "2022-8-20", interval= "1d")
    df = pd.DataFrame(data)
    df_prices = df.loc[:, "Adj Close"] #can also use df.drop(["unwanted columns"])
    #print(df.index) #gives a pd series of df index, not considered a column in tranposition
    df_prices = df_prices.rename_axis("DateTime").reset_index()
    #df_prices.rename({"index" : "DateTime"})   This renaming method is ineffective
    #print(df_prices.columns) #gives colummn names
    df_SPY = df_prices.loc[:, ["DateTime", "SPY"]]

    #print(df_SPY.shape, df_SPY)
    dataPreprocessing(df_SPY)

if __name__ == "__main__":
    main()