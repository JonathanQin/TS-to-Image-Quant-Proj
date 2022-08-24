"""
File: data_test.py
Authors: Jonathan Qin
Description: Pre-project test and experimentation with data processing
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#import os
#import quantsc as Qsc

def dataPreprocessing(data):
    
    """
    Action: Transpose the data
    Action: Clean Non-trading days
    Action: Normalize data values to [-1:1]
    """
    data_T = data.transpose() #or data.T
    print(data_T)
    
    start_date = data_T.iloc[0, 0] #iloc gives specific object, loc gives row/col
    end_date = data_T.iloc[0, -1]
    #print(start_date.shape)
    #print(end_date.shape)
    print(start_date)
    print(end_date)
    
    #dataVisualization(data_T)
    
    
def dataVisualization(data):
    plt.figure()
    #plt.plot(data)
    plt.title("AAPL Equity")
    plt.xlabel("DateTime")
    plt.ylabel("Price")
    
    x = data.loc["DateTime", :]
    y = data.loc["AAPL", :]
    
    plt.plot(x, y)
    plt.show()
    

def gramianAngularField():
    pass

def main():
    stock_list = ['AAPL', 'PFE', 'QQQ']
    data = yf.download(stock_list, start = "2022-8-1", end = "2022-8-24", interval= "1h")
    #print(data.size)
    df = pd.DataFrame(data)
    df_prices = df.loc[:, "Adj Close"]
    #print(df.index) #gives a pd series of df index, not considered a column in tranposition
    df_prices = df_prices.rename_axis("DateTime").reset_index()
    #df_prices.rename({"index" : "DateTime"})   This renaming method is ineffective
    #print(df_prices.columns) #gives colummn names
    df_AAPL = df_prices.loc[:, "DateTime" : "AAPL"]
    #print(df_AAPL.shape, df_AAPL)
    dataPreprocessing(df_AAPL)

if __name__ == "__main__":
    main()