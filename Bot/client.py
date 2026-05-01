import time
import hmac
import hashlib
import requests
import logging

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _sign(self, params):
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, params):
        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": self.api_key}

        try:
            logging.info(f"REQUEST: {params}")

            response = requests.post(
                BASE_URL + "/fapi/v1/order",
                headers=headers,
                params=params
            )

            logging.info(f"RESPONSE: {response.text}")

            return response.json()

        except Exception as e:
            logging.error(f"ERROR: {str(e)}")
            return {"error": str(e)}