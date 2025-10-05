#This File is used to analyse the Daily,Weekly and Monthly Risk exposure and Return Signals to avoid Over Trading and loss of Capital on a wrong market and calculating other parameters for smooth trade operations.
import pandas as pd

def daily_limit(starting_capital,current_portfolio_value):
    if(current_portfolio_value<=(starting_capital-(starting_capital*0.01))):
        print("The Algorithm has reached a max drawdown limit for the day. Trading to be paused for the day")

#This method is used to arrive the take profit price for the ticker based on position size and total profit percentage expected from the trade
def get_take_profit(position_size,order_price,tp_percent):
    take_profit_price=round(order_price+(order_price*((order_price*tp_percent)/(position_size*100))/100),2)
    print(f'The Take profit Price for Given Position and Order Price is {take_profit_price}')

#This method is used to arrive the stop loss price for the ticker based on position size and total stop loss percentage expected from the trade
def get_stop_loss(position_size,order_price,tp_percent):
    stop_loss_price=round(order_price-(order_price*((order_price*tp_percent)/(position_size*100))/100),2)
    print(f'The Stop Loss Price for Given Position and Order Price is {stop_loss_price}')

