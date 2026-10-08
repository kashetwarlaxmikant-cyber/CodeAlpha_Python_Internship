stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in the price list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n=== PORTFOLIO SUMMARY ===")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x "
          f"${stock_prices[stock]} = ${value}")

print("Total Investment: $", total_investment)

with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares x "
                   f"${stock_prices[stock]} = ${value}\n")

    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio_result.txt")
