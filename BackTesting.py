#This File is used to backtest a strategy
import pandas as pd
import plotly.express as pt
INITIAL_CAPITAL = 1000

def plot_compare_index_24to25():
    dataFrame=pd.read_csv("Index24to25Oct.csv")  #Modify the File Name to Calculate For Different Years
    dataFrame=dataFrame[::-1]
    dataFrame.set_index("Date",inplace=True)
    dataFrame.drop(['Index Name'],axis=1,inplace=True)
    dataFrame=simulate_signal_trade_duplicate(dataFrame)
    dataFrame=calculate_returns(dataFrame,1000)
    plot_chart(dataFrame,['IndexReturns','StrategicReturn'])

def calculate_returns(dataFrame,initialCapital):
    initial_index_purchase=dataFrame.iloc[0]['Open']
    position_size=round(initial_index_purchase/initialCapital,2)
    dataFrame['IndexReturns']=round(INITIAL_CAPITAL+ ((dataFrame['Close']-initial_index_purchase)/position_size),2)
    #calculating_required_parameters(dataFrame)
    return dataFrame

def calculating_required_parameters(dataFrame):
    total_return_for_period_percent=round(((dataFrame.iloc[-1]['IndexReturns']-INITIAL_CAPITAL)/INITIAL_CAPITAL)*100,2)
    max_drawdown=min(dataFrame['IndexReturns'])
    max_value=max(dataFrame['IndexReturns'])
    print(f'The Initial Invested Value is {INITIAL_CAPITAL}')
    print(f'The Current Value of the Investment is {dataFrame.iloc[-1]['IndexReturns']} with a return percentage of {total_return_for_period_percent}')
    print(f'The Investment reached a minimum of {max_drawdown} and a peak of {max_value}')

def plot_chart(dataFrame,y_parameter):
    fig=pt.line(dataFrame,x=dataFrame.index,y=y_parameter,title="Average Return Chart")
    fig.show()

def get_take_profit(position_size,capital,order_price,tp_percent):
    take_profit_price=order_price+round((capital*tp_percent)/(position_size*100),2)
    print(f'The Take profit Price for Given Position and Order Price is {take_profit_price}')
    return take_profit_price
#This method is used to arrive the stop loss price for the ticker based on position size and total stop loss percentage expected from the trade
def get_stop_loss(position_size,capital,order_price,tp_percent):
    stop_loss_price=order_price-round((capital*tp_percent)/(position_size*100),2)
    print(f'The Stop Loss Price for Given Position and Order Price is {stop_loss_price}')
    return stop_loss_price
#Modify This Method to implement the strategy of algorithm 
def simulate_signal_trade(dataFrame):
    dataFrame['EMA5']=round(dataFrame['Close'].rolling(5).mean(),2)
    dataFrame['EMA9']=round(dataFrame['Close'].rolling(9).mean(),2)
    dataFrame['StrategicReturn']=0
    dataFrame=dataFrame.dropna()
    initial_capital=1000
    prev_ema5=dataFrame.iloc[0]['EMA5']
    prev_ema9=dataFrame.iloc[0]['EMA9']
    position=0
    take_profit=0
    stop_loss=0
    for index,value in dataFrame.iterrows():
        capital_left=0
        if value['EMA5']> value['EMA9'] and prev_ema9<=prev_ema5 and position==0 :
            position_size=round(initial_capital/value['Close'],2)
            take_profit=get_take_profit(position_size,initial_capital,value['Close'],5)
            stop_loss=get_stop_loss(position_size,initial_capital,value['Close'],2)
            order_price=value['Close']
            position=1
        elif position==1:
            if(value['Close'])>= take_profit:
                initial_capital+=(initial_capital*0.05)
                position=0
            elif(value['Close'])<=stop_loss:
                initial_capital-=(initial_capital*0.02)
                position=0
            else:
                capital_left=round((initial_capital/order_price)*value['Close'],2)
        prev_ema5=value['EMA5']
        prev_ema9=value['EMA9']
        if capital_left!=0:
            dataFrame.at[index,'StrategicReturn']=capital_left
            capital_left=0
        else:
            dataFrame.at[index,'StrategicReturn']=initial_capital
    print(dataFrame)
    return dataFrame
                
    
def simulate_signal_trade_duplicate(dataFrame):
    dataFrame['EMA5']=round(dataFrame['Close'].rolling(5).mean(),2)
    dataFrame['EMA9']=round(dataFrame['Close'].rolling(9).mean(),2)
    dataFrame['StrategicReturn']=0
    dataFrame=dataFrame.dropna()
    initial_capital=1000
    no_of_trades=0
    prev_ema5=dataFrame.iloc[0]['EMA5']
    prev_ema9=dataFrame.iloc[0]['EMA9']
    position=0
    take_profit=0
    stop_loss=0
    for index,value in dataFrame.iterrows():
        capital_left=0
        if value['EMA5']> value['EMA9'] and prev_ema9<=prev_ema5 and position==0 :
            position_size=round(initial_capital/value['Close'],2)
            order_price=value['Close']
            position=1
            no_of_trades+=1
        elif position==1 :
            if(value['EMA5']<=value['EMA9'] and value['Close']>=order_price):
                initial_capital +=(value['Close']-order_price)*position_size
                position=0
            if(value['EMA5']<=value['EMA9'] and value['Close']< order_price):
                initial_capital-=(order_price-value['Close'])*position_size
                position=0
            else:
                capital_left=round((initial_capital/order_price)*value['Close'],2)
        prev_ema5=value['EMA5']
        prev_ema9=value['EMA9']
        if capital_left!=0:
            dataFrame.at[index,'StrategicReturn']=capital_left
            capital_left=0
        else:
            dataFrame.at[index,'StrategicReturn']=initial_capital
    #print(dataFrame)
    print(no_of_trades)
    return dataFrame

plot_compare_index_24to25()
