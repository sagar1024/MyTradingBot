from bot.futures_client import BinanceFuturesREST

class MyTradingBot:
    def __init__(self):
        self.client = BinanceFuturesREST()

    def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
        return self.client.place_order(symbol, side, quantity, order_type, price, stop_price)
