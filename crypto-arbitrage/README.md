This is a bot that performs basic arbitrage between two coins on the Binance and Bybit exchanges.

The process is quite basic:
1. Determine the difference between a given coin.
2. Determine its deviation from the mean.
3. If the deviation exceeds the bid-ask spread plus a threshold, open a long position on one exchange and the opposite on the other.
4. If / when the deviation is reversed close the position.