import pandas as pd
from pandas._libs import index

#This Function is used to read candle data from csv file and returns the last 200 rows
def read_candle_data():
    dataFrame=pd.read_csv("candleDataFinal.csv")
    dataFrame=dataFrame.tail(200)
    dataFrame=dataFrame.drop(['Unnamed: 0'],axis=1)
    dataFrame=dataFrame.set_index('t')
    return dataFrame

#This Method Calculates the Support and Resistance of the given dataframe and returns a buy or sell signal if the price is within a threshold of the support/resistance
def calculate_support_resistance(dataFrame,threshold):
    support=dataFrame['c'].min()
    resistance=dataFrame['c'].max()
    support_range =float(support*(threshold/100))
    resistance_range=float(resistance*(threshold/100))
    current_price=float(dataFrame.iloc[-1]['c'])
    if(current_price <=support+support_range and current_price>=support-support_range):
        print("The price is inside Support Zone. Initiate Buy Order")
    elif(current_price <=resistance+resistance_range and current_price >= resistance-resistance_range):
        print("The price is reaching Resistance Zone. Initiate Sell Order")
    else:
        print(f"The Price is Trading within range {support_range} & {resistance_range}")
    print(f'The Support is {support} and resistance is {resistance} and the current price is {current_price}')


dataFrame=read_candle_data()
calculate_support_resistance(dataFrame,2)
