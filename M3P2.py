ticker = input("Enter the stock ticker symbol: ").upper()
shares = float(input(f"Enter number of shares for {ticker}: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print(f"Ticker: {ticker}")
print(f"Total Amount Invested: ${amount_invested:.2f}")
