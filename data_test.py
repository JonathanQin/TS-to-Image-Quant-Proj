import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#import os
#import quantsc as Qsc

def dataPreprocessing(data):
    
    """
    Transpose the data
    Action: Remove after hours trading datapoints
    Action: Normalize data values to [-1:1]
    """
    data_T = data.transpose() #or data.T
    print(data_T)
    dataVisualization(data_T)
    
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
    print(data.size)
    df = pd.DataFrame(data)
    df_prices = df.loc[:, "Adj Close"]
    print(df.index) #gives a pd series of df index, not considered a column in tranposition
    df_prices = df_prices.rename_axis("DateTime").reset_index()
    #df_prices.rename({"index" : "DateTime"})   This renaming method is ineffective
    print(df_prices.columns) #gives colummn names
    #print(df_prices)
    #print(df_prices.shape)
    df_AAPL = df_prices.loc[:, "DateTime" : "AAPL"]
    print(df_AAPL.shape, df_AAPL)
    dataPreprocessing(df_AAPL)

if __name__ == "__main__":
    main()