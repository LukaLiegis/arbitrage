import asyncio
import websockets
import json
from src.arbitrage import check_arbitrage

BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
BYBIT_WS_URL = "wss://stream.bybit.com/realtime"
ARBITRAGE_THRESHOLD = 100  # Example threshold

# Global variables to store the latest prices
latest_binance_price = None
latest_bybit_price = None

async def binance_ws():
    global latest_binance_price
    async with websockets.connect(BINANCE_WS_URL) as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            latest_binance_price = float(data['p'])
            print(f"Binance BTC/USDT: {latest_binance_price}")
            check_arbitrage(latest_binance_price, latest_bybit_price, ARBITRAGE_THRESHOLD)

async def bybit_ws():
    global latest_bybit_price
    async with websockets.connect(BYBIT_WS_URL) as websocket:
        await websocket.send(json.dumps({"op": "subscribe", "args": ["trade.BTCUSD"]}))
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            if 'data' in data:
                latest_bybit_price = float(data['data'][0]['price'])
                print(f"Bybit BTC/USD: {latest_bybit_price}")
                check_arbitrage(latest_binance_price, latest_bybit_price, ARBITRAGE_THRESHOLD)

async def main():
    await asyncio.gather(binance_ws(), bybit_ws())

if __name__ == "__main__":
    asyncio.run(main())