import yfinance as yf
import sys
from pathlib import Path
import pandas as pd
import time
from datetime import datetime


def timeframe_picker(choice):
    if choice == '' or choice == 'b':
        return 'both'
    elif choice == 'd':
        return 'day'
    else:
        return 'week'


# list of tickers to download
tickers = ['LLY', 'NVO', 'JNJ', 'MRK', 'ABBV', 'MRNA',
           'NVS', 'AZN', 'PFE', 'AMGN', 'PPH', 'IHE', 'PJP']
tickers.sort()
left = len(tickers)

# check if user input is valid
try:
    choice = sys.argv[1]
    print('choice', choice)
# if not, ask for input
except:
    choice = input('\n\nd or w candles? (or \'b\' for both)\n\n')
choice = timeframe_picker(choice)

# download data
print("Downloading "+choice+" candles:")

# get current time
current_time = datetime.now()
time_formatted = current_time.strftime("%I:%M %p")
date_formatted = current_time.strftime("%b %d, %Y")
print(f"Time Started: {time_formatted}, {date_formatted}")

# for each ticker, download data and save to file
for symbol in tickers:
    symbol = symbol.strip()
    try:
        if choice == 'day' or choice == 'both':
            # edit to change timeframe
            data_day = yf.download(
                # change period to get specific data, or interval for different timeframe
                symbol, period="3000d", interval="1d", progress=False)
            Path(
                'pharma-data/raw-data/stocks-for-overdose').mkdir(parents=True, exist_ok=True)
            data_day.to_pickle(
                'pharma-data/raw-data/stocks-for-overdose/'+symbol+'.pkl')
            print('Saved Daily: '+symbol+'.pkl')
            time.sleep(2)

        if choice == 'week' or choice == 'both':
            # edit to change timeframe
            data_week = yf.download(
                symbol, period="800wk", interval="1wk", progress=False)
            Path('pharma-data/week').mkdir(parents=True, exist_ok=True)
            data_week.to_pickle('pharma-data/week/'+symbol+'.pkl')
            print('Saved Weekly: '+symbol+'.pkl')
            time.sleep(2)
    # if an error occurs, print the error
    except Exception as e:
        print(f"An error occurred: {e}")
        print('...and cant get html: '+symbol)
    # print how many tickers are left to download
    left = left - 1
    print(str(left)+' tickers left')
print('\n\n----- Finished downloading '+choice+' candles: -----\n\n')
current_time = datetime.now()
time_formatted = current_time.strftime("%I:%M %p")
date_formatted = current_time.strftime("%b %d, %Y")
print(f"Time Ended: {time_formatted}, {date_formatted}")
