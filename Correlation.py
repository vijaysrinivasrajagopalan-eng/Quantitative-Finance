from math import inf, nan
import numpy as nm
import pandas as pd
import plotly.express as pt
def reading_initial_data():
    btc_dataFrame=pd.read_csv("BTC1D22to25.csv")
    sol_dataFrame=pd.read_csv("Solana1D22to25.csv")
    btc_dataFrame.set_index('t',inplace=True)
    btc_dataFrame.drop(['Unnamed: 0'],axis=1,inplace=True)
    sol_dataFrame.set_index('t',inplace=True)
    sol_dataFrame.drop(['Unnamed: 0'],axis=1,inplace=True)
    return btc_dataFrame,sol_dataFrame

def calculate_percentage_change():
    btc_dataFrame,sol_dataFrame=reading_initial_data()
    btc_dataFrame['return']=round((btc_dataFrame['c']-btc_dataFrame['o'])*100/btc_dataFrame['o'],2)
    sol_dataFrame['return']=round((sol_dataFrame['c']-sol_dataFrame['o'])*100/sol_dataFrame['o'],2)
    print(max(btc_dataFrame['return']))
    #fig=pt.line(btc_dataFrame,x=btc_dataFrame.index,y=[btc_dataFrame['return'],sol_dataFrame['return']],title="Return Chart")
    #fig.show()
    calculate_variance(btc_dataFrame,sol_dataFrame)

def calculate_variance(dataFrame1,dataFrame2):
    for index,rows in dataFrame2.iterrows():
        if rows['return']==0:
            dataFrame2=dataFrame2.drop(index=index)
            dataFrame1=dataFrame1.drop(index=index)
    dataFrame1['Variance']=dataFrame1['return']/dataFrame2['return']
    print(dataFrame1['Variance'].mean())
    print(dataFrame1.head(2))
    print(dataFrame2.head(2))
   

calculate_percentage_change()

