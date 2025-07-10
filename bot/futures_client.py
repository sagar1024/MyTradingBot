import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import API_KEY, API_SECRET, BASE_URL

class BinanceFuturesREST:
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET.encode()
        self.base_url = BASE_URL
    
    def _get_timestamp(self):
        server_time = requests.get(f"{self.base_url}/fapi/v1/time").json()["serverTime"]
        return server_time

    def _sign(self, data: dict):
        query_string = urlencode(data)
        signature = hmac.new(self.api_secret, query_string.encode(), hashlib.sha256).hexdigest()
        return f"{query_string}&signature={signature}"

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }
    
    def place_order(self, symbol, side, quantity, order_type="MARKET", price=None, stop_price=None):
        endpoint = "/fapi/v1/order"
        url = self.base_url + endpoint
        
        #Converting STOP_LIMIT to STOP i.e Binance APIs expected type
        binance_order_type = "STOP" if order_type == "STOP_LIMIT" else order_type

        data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": self._get_timestamp(),
            "recvWindow": 10000
        }

        if order_type in ["LIMIT", "STOP"]:
            data["timeInForce"] = "GTC"

        if price:
            data["price"] = price
        if stop_price:
            data["stopPrice"] = stop_price

        signed_data = self._sign(data)
        try:
            response = requests.post(url, headers=self._headers(), params=signed_data)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
        