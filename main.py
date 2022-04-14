from binance.client import Client
from binance.enums import *
import pandas as pa

api_key = 'nNrfv2MweJDgY8eJCWAT9XbCrRj4E3n4pzgok7EgdBgfhFjvqoOGVJBgM4OniH05'
api_secret = 'PVUiJMl5N4mar1WkP3WRwM7Z4Fh9JcB1jxnoT6e5lk0PHIBVr8h0g35pLVo28GV4'

client = Client(api_key, api_secret)
inf_log_n_st = client.get_system_status()
print(f"Logged in. Status: {inf_log_n_st['status']}; message: {inf_log_n_st['msg']}")

print("Commands: 'average'; 'buy' ; 'balance'; 'infpairs'")
command = input()

set_quantity = 0
set_price = 0
current_pairs = 0


def info_about_pairs(symbol, time, look_back):
    frame = pa.DataFrame(client.get_historical_klines(symbol, time, look_back + "min ago UTC"))
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
        if price_change[-1] > 0.002:
            order = client.create_order(
                symbol=symbol,
                side='BUY',
                type='MARKET',
                quantity=quantity
            )
            print(order)
            that = True
        else:
            print('No Trade? :(')
    if that:
        while True:
            data_frame = info_about_pairs(symbol, '1m', '30')
            since_buy = data_frame.loc(data_frame.index > pa.to_datetime(order['transactTime'], unit='ms'))
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
        print('Enter pairs to see their average price')
        print('Enter "exit" to go to start')
        avr_pairs = input()
        if avr_pairs == 'exit':
            break

        candles = client.get_avg_price(symbol=avr_pairs)
        print(candles)

        print('See another?')
        avg_yesno = input()
        if avg_yesno == 'yes':
            continue
        if avg_yesno == 'no':
            break


def infpairs():
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
    if command == "average":
        average()

    elif command == "infpairs":
        infpairs()

    elif command == "buy":
        print('Do you want to buy Crypto?')
        action = input()
        if action == 'yes':
            current_pairs = input("Enter pairs: ")
            quantity_qw = input('Enter quantity: ')
        else:
            break
        strategy(current_pairs, quantity_qw)

    elif command == "balance":
        balance()

    else:
        print("***** Wrong command *****")

    command = input("Enter command ")

# while True:
#     see_pair_yesno = (input('Want to average pair price (no or yes): '))
#     if see_pair_yesno == 'yes':
#         avr_pairs = input('Set pairs to see average price (like "SOLBNB"): ')
#         candles = client.get_avg_price(symbol=avr_pairs)
#         print(candles)
#
#         avg_yesno = (input('See another? '))
#         if avg_yesno == 'yes':
#             continue
#         if avg_yesno == 'no':
#             break
#     if see_pair_yesno == 'no':
#         break

# while True:
#     action = input('Do you want buy Crypto? ')
#     if action == 'yes':
#         print('Enter "exit" to go to start')
#         current_pairs = input('Enter pairs (like "SOLBNB"): ')
#         if current_pairs == 'exit':
#             break
#
#         print('Use average price?')
#         use_avg_price = input()
#
#         if use_avg_price:
#             candles = client.get_avg_price(symbol=current_pairs)
#             set_price = candles['price']
#         else:
#             set_price = float(input('Enter price: '))
#             print('Enter "exit" to go to start')
#             if set_price == 'exit':
#                 break
#
#         print("U can set max quantity according to your balance or set it manually")
#         choose_qunat = input('Enter "max" or "mnl": ')
#         if choose_qunat == 'max':
#             candles = client.get_avg_price(symbol=current_pairs)
#             balance = client.get_asset_balance(asset=current_pairs)
#             max_quantity = float(balance['free']) / float(candles['price'])
#             set_quantity = round(max_quantity, 2)
#         else:
#             set_quantity = input("Enter quantity: ")
#
#         order = client.order_limit(
#             symbol=current_pairs,
#             quantity=set_quantity,
#             price=set_price
#         )
#     if action == 'no':
#         break
