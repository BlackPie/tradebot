import random

import ccxt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



kraken = ccxt.kraken({
    'apiKey': 'Naf/nCE2g2ji/mkz/bCQh0y8odokUSjMpK+TRJXMzSyWB06nCqfjXNs1',
    'secret': 'xmu/rAfZfE1e1dllNSHIKzM0JR7v0uO67PqK3LTjo3ICpZQQCCjzJXNdqWFuZ2Pw7gcsZvDsRHrHm5uPneaXOw==',
})
data = kraken.fetch_ohlcv('BTC/USD', '1h')
timestamps = [x[0] for x in data]
values = [x[4] for x in data]
timeseries = zip(timestamps, values)


def is_it_time_to_buy(timestamp, value, timeseries) -> bool:
    # TODO: implement this
    return random.random() <= 0.02


def is_time_to_sell(timestamp, value, timeseries) -> bool:
    # TODO: implement this
    return random.random() <= 0.02


orders = list()
bought = 0
profit = 0
plt.plot(timestamps, values)

for timestamp, value in timeseries:
    if not bought and is_it_time_to_buy(timestamp, value, timeseries):
        bought = 1
        orders.append((timestamp, value))

    if bought and is_time_to_sell(timestamp, value, timeseries):
        bought = 0
        orders.append((timestamp, value))


if len(orders) % 2:
    orders = orders[:-1]

for index in range(0, len(orders), 2):
    profit += orders[index + 1][1] - orders[index][1]
    plt.plot(orders[index][0], orders[index][1], 'go', label='bought')
    plt.plot(orders[index + 1][0], orders[index + 1][1], 'ro', label='sold')

green_patch = mpatches.Patch(color='green', label='buy')
red_patch = mpatches.Patch(color='red', label='sell')
plt.legend(handles=[green_patch, red_patch])
plt.show()

print(" ")
print("=========  SUMMARY  =========")
print("TOTAL PROFIT:  ", profit)
print("NUMBER OF ORDERS:  ", len(orders))
