def maxProfit(values):
    profit = 0
    maxProfit = 0
    maxProfitDays = ()
    for i in range(len(values)):
        buyPrice = values[i]
        for j in range(len(values[i:])):
            sellPrice = values[j+i]
            profit = sellPrice - buyPrice
            if profit > maxProfit:
                maxProfitDays = (i, i+j)
                maxProfit = profit
    return (maxProfit, maxProfitDays)


prices = [5, 0, 1, 3, 11, 2]

print(maxProfit(prices))

"""
Complexity is O(n^2) since we have n(n-1)/2 for the two nested loops
"""
