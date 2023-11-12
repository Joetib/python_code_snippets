# Let's create a simple stock market tracker in Python
# We will use the yfinance library to fetch stock data
# Install yfinance using
# >> pip install yfinance

import yfinance as yf
def track_stock(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    print(data)

symbol = input("Enter stock symbol: ")

track_stock(symbol)

# Output
# >> Enter stock symbol: AAPL
# >>                  Open        High         Low       Close    Volume  Dividends  Stock Splits
# >> Date
# >> 2023-11-04  133.520004  133.610001  126.760002  129.410004  143301900          0             0
# >> 2023-11-05  128.889999  131.740005  128.429993  131.009995   97664900          0            0
# >> ...                ...         ...         ...         ...        ...        ...           ...
# Please Like and Subscribe