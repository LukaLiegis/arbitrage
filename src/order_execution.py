import requests
import time
import hmac
import hashlib

# Binance API credentials
BINANCE_API_KEY = 'your_binance_api_key'
BINANCE_API_SECRET = 'your_binance_api_secret'

# Bybit API credentials
BYBIT_API_KEY = 'your_bybit_api_key'
BYBIT_API_SECRET = 'your_bybit_api_secret'

def binance_place_order(symbol, side, quantity, price):
    base_url = 'https://api.binance.com'
    endpoint = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price,
        'timestamp': timestamp
    }
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = hmac.new(BINANCE_API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    headers = {
        'X-MBX-APIKEY': BINANCE_API_KEY
    }
    params['signature'] = signature
    response = requests.post(base_url + endpoint, headers=headers, params=params)
    return response.json()

def bybit_place_order(symbol, side, quantity, price):
    base_url = 'https://api.bybit.com'
    endpoint = '/v2/private/order/create'
    timestamp = int(time.time() * 1000)
    params = {
        'api_key': BYBIT_API_KEY,
        'symbol': symbol,
        'side': side,
        'order_type': 'Limit',
        'qty': quantity,
        'price': price,
        'time_in_force': 'GoodTillCancel',
        'timestamp': timestamp
    }
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = hmac.new(BYBIT_API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    params['sign'] = signature
    response = requests.post(base_url + endpoint, params=params)
    return response.json()

def place_order(exchange, side, amount, price):
    if exchange == "binance":
        return binance_place_order('BTCUSDT', side, amount, price)
    elif exchange == "bybit":
        return bybit_place_order('BTCUSD', side, amount, price)