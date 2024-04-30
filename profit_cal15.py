def calculate_profit(cost_price, selling_price):
    profit = selling_price - cost_price
    return profit

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit = calculate_profit(cost_price, selling_price)

print(f"The profit is: {profit:.2f}")