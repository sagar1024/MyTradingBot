from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, BASE_URL
from bot.logger import get_logger

class MyTradingBot:
    def __init__(self):
        self.logger = get_logger()
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
        try:
            order_type = order_type.upper()
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params.update({"price": price, "timeInForce": "GTC"})
            elif order_type == "STOP_MARKET":
                params.update({"stopPrice": stop_price, "timeInForce": "GTC"})
            elif order_type == "STOP_LIMIT":
                if not stop_price or not price:
                    raise ValueError("Stop and limit prices required for STOP_LIMIT")
                params.update({
                    "stopPrice": stop_price,
                    "price": price,
                    "timeInForce": "GTC"
                })

            self.logger.info(f"Order Params: {params}")
            response = self.client.futures_create_order(**params)
            self.logger.info(f"Order Response: {response}")
            return response

        except BinanceAPIException as e:
            self.logger.error(f"API error: {e}")
            return {"error": str(e)}
        except Exception as e:
            self.logger.error(f"General error: {e}")
            return {"error": str(e)}
