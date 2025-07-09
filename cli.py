from bot.futures_client import BinanceFuturesREST

def main():
    bot = BinanceFuturesREST()

    print("Welcome to MyTradingBot (CLI Version)\n")

    try:
        symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
        side = input("Enter side (BUY/SELL): ").strip().upper()
        order_type = input("Enter order type (MARKET / LIMIT / STOP_LIMIT): ").strip().upper()
        quantity = float(input("Enter quantity: ").strip())

        price = None
        stop_price = None

        if order_type in ["LIMIT", "STOP_LIMIT"]:
            price = float(input("Enter limit price: ").strip())
        if order_type == "STOP_LIMIT":
            stop_price = float(input("Enter stop price: ").strip())

        print("\nPlacing order...")

        result = bot.place_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            order_type=order_type,
            price=price,
            stop_price=stop_price
        )

        print("\nOrder Result:")
        for k, v in result.items():
            print(f"{k}: {v}")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
    