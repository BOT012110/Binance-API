from os import sep
from binance.client import Client
import pandas as pa


api_key = '<api_key>'
api_secret = '<api_secret>'

client = Client(api_key, api_secret)
inf_log_n_st = client.get_system_status()
print(f"Logged in. Status: {inf_log_n_st['status']}; message: {inf_log_n_st['msg']}")

command_list = ['1. Average', '2. Buy', '3. Balance', '4. Pair Info']
 
print("List of available commands: ", *command_list, sep="\n")
command = input("Enter the number of command: ")
print("")

set_quantity = 0
set_price = 0
current_pairs = 0


def info_about_pairs(symbol, time, look_back):
    frame = pa.DataFrame(client.get_historical_klines(symbol, time, look_back + " min ago UTC"))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pa.to_datetime(frame.index, unit='ms')
    frame = frame.astype('float')
    return frame



def strategy(symbol, quantity, that=False):
    data_frame = info_about_pairs(symbol, '1m', '30')
    price_change = (data_frame.Open.pct_change() + 1).cumprod() - 1
    if not that:
        if price_change[-1] < -0.002:
            order = client.create_order(
                symbol=symbol,
                side='BUY',
                type='MARKET',
                quantity=quantity
            )

            print(order)
            that = True
        else:
            print('****** No Trade? :( ******')

    if that:
        while True:
            data_frame = info_about_pairs(symbol, '1m', '30')
            since_buy = data_frame.loc[data_frame.index > pa.to_datetime(order['transactTime'], unit='ms')]

            if len(since_buy) > 0:
                since_buy_ret = (since_buy.Open.pct_change() + 1).cumprod() - 1
                if since_buy_ret[-1] > 0.0015 or since_buy_ret[-1] < 0.0015:
                    order = client.create_order(
                        symbol=symbol,
                        side='SELL',
                        type='MARKET',
                        quantity=quantity
                    )

                    print(order)
                    break


def average():
    while True:
        print('****** Enter pairs to see their average price or write "exit" ******')
        avr_pairs = input()
        if avr_pairs == 'exit':
            break
        
        print("")
        candles = client.get_avg_price(symbol=avr_pairs)
        print(candles)

        print('')
        print('****** See another? ******')
        avg_yesno = input()
        if avg_yesno == 'yes':
            continue
        if avg_yesno == 'no':
            break


def inf_pair():
    pair = input('Enter pair: ')
    inf = info_about_pairs(pair, "1m", '30')
    print(inf)


def balance():
    info = client.get_account()
    balances = info['balances']

    for i in balances:
        if float(i['free']) > 0:
            print(i)


while command != "Exit":
    if command == "1":
        average()

    elif command == "4":
        inf_pair()

    elif command == "2":
        print('****** Do you want to buy Crypto? ******')
        action = input()
        if action == 'yes':
            current_pairs = input("Enter pair: ")
            print("-------------------")
            quantity_qw = input('Enter quantity: ')
        else:
            break
        strategy(current_pairs, quantity_qw)

    elif command == "3":
        balance()

    else:
        print("***** Wrong command!!! *****")

    print("")
    command = input("Enter the number of command: ")
    print("")
