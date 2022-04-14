# Binance-API
Script that allows you to buy cryptocurrency using simple strategy. You also can use it to see: your Binance account balance; average price of pair; minute data of pair (High price, Low, Volume etc.) 
## How To Start
1. Download and unzip archive
2. Create new virtual environment in progect folder (optional)
3. Install requirements.txt
4. Open the progect and run the code
## How to use it
At the beggining you will need to open main.py and enter your api_key and api_secret to start trading with your account. 
Then run the code program will ask you to choose one of the 4 options:

1. Avarage - by selecting this option you can write a tradind pair and see it current average price based on 5 minut interval. ![Снимок экрана (20)](https://user-images.githubusercontent.com/47400349/163309233-c4d04002-8c98-4f7e-af4f-09d2eb390f13.png)
2. Balance - you can see all your account balances that above 0, if you have money in BTC, ETH, SOL, the program will show you only these balances.!
3. Buy - by selecting this option, you will be able to trade cryptocurrency according to the strategy specified in the program. Before starting trading, you will be asked to choose a trading pair and the quantity to buy. Then the program itself will perform the actions of buying and selling. ![Снимок экрана (18)](https://user-images.githubusercontent.com/47400349/163308788-0174dc81-e7ce-4818-93f0-5715caeac4ac.png)
As you can see, my program can successfully trade at a loss :)
![Снимок экрана (22)](https://user-images.githubusercontent.com/47400349/163308683-4f6038e6-9dc2-4c9a-9248-a9e7339fc9b8.png)
4. Inf_pair - this option will allow you to see the history of the trading pair in the time interval. The table shows the data: Opening prices (Open) High prices (High); Low prices (Low); Closing prices (Close) and Volume (Volume) ![Снимок экрана (21)](https://user-images.githubusercontent.com/47400349/163309206-ffca8612-6407-4740-89a7-190e6b2bfbfa.png)

## About choose option
1. The answer options are only yes or no, in some cases exit, to exit an action or program
2. When you are asked to enter a trading pair, you should enter it in the following format - BNBBTC, BTCBNB, SOLUSDT, etc.
3. The quantity values are entered in decimal format - 0.222; 400.0; 0.002 etc.

For AgentApp:
- каким сервисом воспользовались (интегрировались, чьё АПИ использовали):
    Binance API - крупная криптовалютная биржа.
- количество запросов
    не знаю
- список используемых библиотек (requirements.txt)
    pandas, python-binance
- используется ли база данных
    нет
- сделано, как веб-сервер, или как скрипт
    скрипт
- прочее (может есть асинхронные задачи, докер, ci/cd, ...)
    нету
- сколько времени (в часах на это потрачено, примерно)
    6 часов, но не подряд, делал в течении дня
## Дайте знать если ознакомились со всей работой
