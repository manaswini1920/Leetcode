def time_to_buy(prices):
    min_price=float('inf')
    profit=0
    for i in range(len(prices)):
        if prices[i]<min_price:
            min_price=prices[i]
        elif (prices[i]-min_price)>profit:
            profit=prices[i]-min_price
    return profit
print(time_to_buy([7,1,4,6]))