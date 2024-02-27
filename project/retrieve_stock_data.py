import yfinance as yf
import sys
from pathlib import Path
import pandas as pd
import time
from datetime import datetime


def d_or_w(day_or_week):
    if day_or_week == '' or day_or_week == 'b':
        return 'both'
    elif day_or_week == 'd':
        return 'day'
    else:
        return 'week'


# list of tickers to download
tickers = ['LLY', 'NVO', 'JNJ', 'MRK', 'ABBV', 'ROG.SW',
           'NVS', 'AZN', 'PFE', 'AMGN', 'PPH', 'IHE', 'PJP']
tickers.sort()
left = len(tickers)

# check if user input is valid
try:
    day_or_week = sys.argv[1]
    print('day_or_week', day_or_week)
# if not, ask for input
except:
    day_or_week = input('\n\nd or w candles? (or \'b\' for both)\n\n')
day_or_week = d_or_w(day_or_week)

# download data
print("Downloading "+day_or_week+" candles:")

# get current time
current_time = datetime.now()
time_formatted = current_time.strftime("%I:%M %p")
date_formatted = current_time.strftime("%b %d, %Y")
print(f"Time Started: {time_formatted}, {date_formatted}")

# for each ticker, download data and save to file
for symbol in tickers:
    symbol = symbol.strip()
    try:
        if day_or_week == 'day' or day_or_week == 'both':
            # edit to change timeframe
            data_day = yf.download(
                # change period to get specific data, or interval for different timeframe
                symbol, period="2501d", interval="1d", progress=False)
            Path('pharma-data/day').mkdir(parents=True, exist_ok=True)
            data_day.to_pickle('pharma-data/day/'+symbol+'.pkl')
            print('Saved Daily: '+symbol+'.pkl')
            time.sleep(2)

        if day_or_week == 'week' or day_or_week == 'both':
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
print('\n\n----- Finished downloading '+day_or_week+' candles: -----\n\n')
current_time = datetime.now()
time_formatted = current_time.strftime("%I:%M %p")
date_formatted = current_time.strftime("%b %d, %Y")
print(f"Time Ended: {time_formatted}, {date_formatted}")
