import asyncio
import websockets
import json

BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
BYBIT_WS_URL = "wss://stream.bybit.com/realtime"

async def binance_ws():
    async with websockets.connect(BINANCE_WS_URL) as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            price = float(data['p'])
            print(f"Binance BTC/USDT: {price}")
            # Add logic to store or process the price

async def bybit_ws():
    async with websockets.connect(BYBIT_WS_URL) as websocket:
        await websocket.send(json.dumps({"op": "subscribe", "args": ["trade.BTCUSD"]}))
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            if 'data' in data:
                price = float(data['data'][0]['price'])
                print(f"Bybit BTC/USD: {price}")
                # Add logic to store or process the price

async def main():
    await asyncio.gather(binance_ws(), bybit_ws())

if __name__ == "__main__":
    asyncio.run(main())