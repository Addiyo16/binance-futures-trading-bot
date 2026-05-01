def validate_order(symbol, side, order_type, quantity, price, stop_price):
    if not symbol:
        raise ValueError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT orders require a price")

    if order_type == "STOP":
        if price is None or stop_price is None:
            raise ValueError("STOP orders require both price and stopPrice")