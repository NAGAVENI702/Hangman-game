import yfinance as yf

portfolio = {}

def add_stock(symbol, shares):
    portfolio[symbol] = portfolio.get(symbol, 0) + shares
    print(f"{shares} shares of {symbol} added.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    print("\n--- Portfolio Summary ---")
    total_value = 0
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"][0]
        value = shares * price
        total_value += value
        print(f"{symbol}: {shares} shares | Current Price: ₹{price:.2f} | Total Value: ₹{value:.2f}")
    print(f"Total Portfolio Value: ₹{total_value:.2f}\n")

# Menu
while True:
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter stock symbol (e.g. INFY.NS): ").upper()
        shares = int(input("Enter number of shares: "))
        add_stock(symbol, shares)
    elif choice == '2':
        symbol = input("Enter stock symbol to remove: ").upper()
        remove_stock(symbol)
    elif choice == '3':
        view_portfolio()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
