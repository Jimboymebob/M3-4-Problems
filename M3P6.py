purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = int(input("Enter quantity of shares: "))

# Calculate gain or loss
value_change = (current_price - purchase_price) * quantity

if value_change >= 0:
    print(f"Value Increase: ${value_change:.2f}")
else:
    # Using abs() to show a clean positive number for a "loss" label
    print(f"Value Decrease: -${abs(value_change):.2f}")
