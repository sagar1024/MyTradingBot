# import requests
# from binance.client import Client
# from binance.exceptions import BinanceAPIException
# from config import API_KEY, API_SECRET, BASE_URL
# from bot.logger import get_logger

# class MyTradingBot:
    
#     def __init__(self):
#         self.logger = get_logger()
#         session = requests.Session()
#         session.headers.update({'User-Agent': 'binance/python'})

#         self.client = Client(API_KEY, API_SECRET, requests_params={"session": session})
#         self.client.FUTURES_URL = BASE_URL
#         self.client.FUTURES_API_URL = BASE_URL
#         self.client.FUTURES_TESTNET_URL = BASE_URL
#         self.client.FUTURES_USE_SERVER_TIME = True

#         print("FUTURES_URL =>", self.client.FUTURES_URL)

#         try:
#             balance = self.client.futures_account_balance()
#             print("Futures Account Balance =>", balance)
#         except Exception as e:
#             print("Error fetching futures balance:", e)
    
#     def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
#         try:
#             order_type = order_type.upper()
#             params = {
#                 "symbol": symbol.upper(),
#                 "side": side.upper(),
#                 "type": order_type,
#                 "quantity": quantity
#             }

#             if order_type == "LIMIT":
#                 params.update({"price": price, "timeInForce": "GTC"})
#             elif order_type == "STOP_MARKET":
#                 params.update({"stopPrice": stop_price, "timeInForce": "GTC"})
#             elif order_type == "STOP_LIMIT":
#                 if not stop_price or not price:
#                     raise ValueError("Stop and limit prices required for STOP_LIMIT")
#                 params.update({
#                     "stopPrice": stop_price,
#                     "price": price,
#                     "timeInForce": "GTC"
#                 })

#             self.logger.info(f"Order Params: {params}")
#             response = self.client.futures_create_order(**params)
#             self.logger.info(f"Order Response: {response}")
#             return response
        
#         except BinanceAPIException as e:
#             self.logger.error(f"API error: {e}")
#             self.logger.error(f"Full response: {e.response.text}")
#             return {"error": f"{e} | Full response: {e.response.text}"}

#         except Exception as e:
#             self.logger.error(f"General error: {e}")
#             return {"error": str(e)}

from bot.futures_client import BinanceFuturesREST

class MyTradingBot:
    def __init__(self):
        self.client = BinanceFuturesREST()

    def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
        return self.client.place_order(symbol, side, quantity, order_type, price, stop_price)
