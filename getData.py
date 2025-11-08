import yfinance as yf
import pandas as pd
import ta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


startDate = '2004-01-01'  # Inclusive Date, so begins on Jan 1, 2004
endDate = pd.Timestamp.today().normalize().strftime('%Y-%m-%d')  # Exclusive Date, so ends yesterday

tickers = [ '^GSPC', # S&P 500
            '^DJI',  # Dow Jones Industrial Average
            '^IXIC',  # NASDAQ Composite
            '^GSPTSE',  # S&P/TSX Composite Index
            '^RUT',  # Russell 2000
            '^VIX',  # CBOE Volatility Index
            '^NYA',  # NYSE Composite Index
           ]

def getData(tickers, startDate, endDate):
    tic = yf.Ticker(tickers)
    
    data = tic.history(start=startDate, end=endDate)
    
    if data.empty:
        return None
    
    data['RSI'] = ta.momentum.RSIIndicator(close=data['Close']).rsi()
    data['MACD_Diff'] = ta.trend.MACD(close=data['Close']).macd_diff()
    data['Volatility'] = data['Close'].pct_change().std()
    data['SPOF'] = tic.get_info().get('shortPercentOfFloat')
    
    info = tic.get_info()
    
    staticFields = {
        'Ticker': tickers,
        'Name' : info.get('shortName'),
        'Industry' : info.get('industry'),
        'Currency' : info.get('currency'),
        'Sector' : info.get('sector')
    }
    
    for key, value in staticFields.items():
        data[key] = value
        
    return data.reset_index()

panel = []

for ticker in tickers:
    df = getData(ticker, startDate, endDate)
    if df is not None:
        panel.append(df)
        
panel = pd.concat(panel, ignore_index=True)

load_dotenv("secret.env")
db_user = "root"
db_password = os.getenv("DB_PASSWORD")
db_host = "localhost"
db_database = "stock_data"

engine = create_engine(f"mysql+mysqlconnector://root:{db_password}@localhost/stock_data")
panel.to_sql("stock_panel", con=engine, if_exists='replace', index=False)