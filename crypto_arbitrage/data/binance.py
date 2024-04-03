import json
import websocket
import pandas as pd


def manipulation(source):
    """
    Manipulate the
    :param source:
    :return:
    """
    rel_data = source["k"]["c"]
    evt_time = pd.to_datetime(source["E"], unit="ms")
    df = pd.DataFrame(rel_data, columns=["close"], index=[evt_time])
    df.index.name = "timestamp"
    df = df.astype(float)
    df = df.reset_index()
    print(df)
    return df


def on_message(ws, message):
    """
    Callback function
    :param ws:
    :param message:
    :return:
    """
    message = json.loads(message)
    manipulation(message)


socket = "wss://fstream.binance.com/ws/" + asset

ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever()
