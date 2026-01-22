import pandas as pd
import yfinance as yf

# Read the cleaned market info
cleaned_path = 'Cleaned_Market_Info_with_DJI.csv'
out_path = 'Cleaned_Market_Info_with_Russell.csv'

print('Reading', cleaned_path)
df = pd.read_csv(cleaned_path, index_col=0, parse_dates=True)

# Ensure index is datetime
try:
    df.index = pd.to_datetime(df.index)
except Exception:
    # if index looks numeric like 19260701, try parsing with format
    df.index = pd.to_datetime(df.index.astype(str), format='%Y%m%d', errors='coerce')

# Download Dow Jones (^DJI) using yfinance for the same date range
start = df.index.min().strftime('%Y-%m-%d')
end = (df.index.max() + pd.Timedelta(days=1)).strftime('%Y-%m-%d')
stock = yf.download('^RUT', start=start, end=end, progress=False)

# Use Close prices and name column 'DJI'
if 'Close' in stock.columns:
    stock_close = stock['Close'].copy()
    stock_close.name = 'RUT'
else:
    # fallback: if download returned a single column, use that
    if stock.shape[1] == 1:
        stock_close = stock.iloc[:, 0].copy()
        stock_close.name = 'RUT'
    else:
        raise SystemExit('Could not find Close column in downloaded RUT data: ' + ','.join(map(str, dji.columns)))

# Align with cleaned df index; forward-fill missing dates
# Normalize DJ index to remove time component
if hasattr(stock_close.index, 'normalize'):
    stock_close.index = stock_close.index.normalize()

# Reindex and forward fill to match cleaned dates
stock_aligned = stock_close.reindex(df.index)
stock_aligned = stock_aligned.ffill()

df['RUT'] = stock_aligned
df.to_csv(out_path, index=True)
