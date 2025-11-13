import yfinance as yf
import pandas as pd
import ta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


startDate = '2004-01-01'  # Inclusive Date, so begins on Jan 1, 2004
endDate = '2014-01-01' #First training cutoff
#endDate = pd.Timestamp.today().normalize().strftime('%Y-%m-%d')  # Exclusive Date, so ends yesterday

tickers = [ # Market Indexes
            '^GSPC', # S&P 500
            '^DJI',  # Dow Jones Industrial Average
            '^IXIC',  # NASDAQ Composite
            '^GSPTSE',  # S&P/TSX Composite Index
            '^RUT',  # Russell 2000
            '^VIX',  # CBOE Volatility Index
            '^NYA',  # NYSE Composite Index
            
            # Communication Services
            
            # Consumer Discretionary
            
            # Consumer Staples
            
            # Energy
            
            # Financials
            
            # Healthcare
            'XLV', # Health Care Select Sector SPDR Fund ETF
            
                # Biotech
                'XBI', # SPDR S&P Biotech ETF
                'VRTX',  # Vertex Pharmaceuticals Incorporated / 105B
                'ALNY',  # Alnylam Pharmaceuticals, Inc. / 60B
                'INSM', # Insmed Incorporated / 40B
                'INCY',  # Incyte Corporation / 20B
                'IONS', # Ionis Pharmaceuticals, Inc. / 10B
                'ARWR',  # Arrowhead Pharmaceuticals, Inc. / 6B
                'HBP.TO', # Helix BioPharma Corp. / 0.2B
                
                # Diagnostics & Research
                # no ETF
                'TMO', # Thermo Fisher Scientific Inc. / 215B
                'IDXX', # IDEXX Laboratories, Inc. / 55B
                'EXAS', # Exact Sciences Corporation / 13B
                'NOTV', # Inotiv Inc. / 0.04B
                
                # Drug Manufacturers - General
                'PPH', # VanEck Pharmaceutical ETF
                'LLY', # Eli Lilly and Company / 865B
                'JNJ', # Johnson & Johnson / 450B
                'PFE', # Pfizer Inc. / 140B
                'BMY', # Bristol-Myers Squibb Company / 95B
                'BHC.TO', # Bausch Health Companies Inc. / 3B
                
                # Drug Manufacturers - Specialty & Generic
                # no eTF
                'TEVA', # Teva Pharmaceutical Industries Limited / 30B
                'NBIX', # Neurocrine Biosciences, Inc. / 15B
                'ALKS', # Alkermes plc / 5B
                'EBS', # Emergent BioSolutions Inc. / 0.5B
                'ANIK', # Anika Therapeutics Inc. / 0.3B
                
                # Health Information Services
                # no ETF
                'OMCL', # Omnicell, Inc. / 1.5B
                'HSTM', # HealthStream, Inc. / 0.7B
                'SLP', # Simulations Plus, Inc. / 0.35B
                
                # Healthcare Plans
                # no ETF
                'UNH', # UnitedHealth Group Incorporated / 350B
                'CVS', # CVS Health Corporation / 130B
                'HUM', # Humana Inc. / 30B
                
                # Medical Care Facilities
                # no ETF
                'THC', # Tenet Healthcare Corporation / 17B
                'UHS', # Universal Health Services, Inc. / 14B
                'BKD', # Brookdale Senior Living Inc. / 2B
                'CCEL', # Cryo-Cell International, Inc. / 0.03B
                
                # Medical Devices
                'IHI', # iShares U.S. Medical Devices ETF
                'ABT', # Abbott Laboratories / 225B
                'MDT', # Medtronic plc / 122B
                'STE', # STERIS plc / 26B
                'BIO', # Bio-Rad Laboratories, Inc. / 8B
                'IART', # Integra LifeSciences Holdings Corporation / 1B
                'CERS', # Cerus Corporation / 0.3B
                
                # Medical Distribution
                # no ETF
                'MCK', # McKesson Corporation / 105B
                'COR', # Censora, Inc. / 70B
                'CAH', # Cardinal Health, Inc. / 48B
                'HSIC', # Henry Schein, Inc. / 8B
                'EDAP', # EDAP TMS S.A. / 0.075B
                
                # Medical Instruments & Supplies
                # no ETF
                'ISRG', # Intuitive Surgical, Inc. / 200B
                'BDX', # Becton, Dickinson and Company / 55B
                'COO', # CooperCompanies Inc. / 15B
                'MMSI', #Merit Medical Systems, Inc. / 5B
                'SMTI', #Sanara MedTech Inc. / 0.2B
                
                # Pharmaceutical Retailers
                'PETS', #PetMed Express, Inc. / 60M
                'RDGT', #Ridge Tech, Inc / 0.02B
                
            # Industrials
            
            # Materials
            
            # Real Estate
            
            # Technology
            
            # Utilities

                # Diversified
                'SRE', #Sempra Energy / 60B
                'AES', #The AES Corporation / 10
                'CIG', #Companhia Energetica de Minas Gerais - CEMIG / 6B
                'AVA', #Avista Corporation / 3B
           ]

def getData(tickers, startDate, endDate):
    tic = yf.Ticker(tickers)
    
    data = tic.history(start=startDate, end=endDate)
    
    if data.empty:
        return None
    
    info = tic.get_info()
    
    data['Market Cap'] = info.get('marketCap') # Market Cap
    data['RSI'] = ta.momentum.RSIIndicator(close=data['Close']).rsi() # Relative Strength Index
    data['MACD'] = ta.trend.MACD(close=data['Close']).macd_diff() # Moving Average Convergence/Divergence or its momentum
    data['Volatility'] = data['Close'].pct_change().std() # Historical Volatility
    data['SPOF'] = info.get('shortPercentOfFloat') # Short Percent of Float
    
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

panelList = []
for ticker in tickers:
    df = getData(ticker, startDate, endDate)
    if df is not None:
        panelList.append(df)
        
panel = pd.concat(panelList, ignore_index=True)

staticFields = ['Ticker', 'Name', 'Industry', 'Currency', 'Sector']
stockFields = ['Open', 'High', 'Low', 'Close', 'Volume', 'RSI', 'MACD', 'Volatility', 'SPOF']

existingStockFields = [col for col in stockFields if col in panel.columns]
desiredOrder = ['Date'] + staticFields + existingStockFields

panel = panel[desiredOrder]

load_dotenv("secret.env")
db_user = "root"
db_password = os.getenv("DB_PASSWORD")
db_host = "localhost"
db_database = "stock_data"

engine = create_engine(f"mysql+mysqlconnector://root:{db_password}@localhost/stock_data")
panel.to_sql("stock_panel", con=engine, if_exists='replace', index=False)