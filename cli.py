import argparse
import os
from dotenv import load_dotenv

from Bot.client import BinanceClient
from Bot.orders import create_order_params
from Bot.validators import validate_order
from Bot.logging_config import setup_logging

# 🔐 Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


# ✅ Pretty success output
def print_success(response):
    print("\n" + "=" * 40)
    print("✅ ORDER EXECUTED SUCCESSFULLY")
    print("=" * 40)
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
    print("=" * 40 + "\n")


# ❌ Pretty error output
def print_error(response):
    print("\n" + "=" * 40)
    print("❌ ORDER FAILED")
    print("=" * 40)
    print(response)
    print("=" * 40 + "\n")


def main():
    setup_logging()

    # 🔴 Check if keys exist
    if not API_KEY or not API_SECRET:
        print("❌ ERROR: API_KEY or API_SECRET not found in .env file")
        return

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True)
    parser.add_argument("--price")
    parser.add_argument("--stop_price")

    args = parser.parse_args()

    try:
        # ✅ Validation
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price,
            args.stop_price
        )

        # ✅ Create params
        params = create_order_params(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price,
            args.stop_price
        )

        # ✅ Confirmation UI
        print("\n🔍 ORDER SUMMARY")
        print(f"Symbol : {args.symbol}")
        print(f"Side   : {args.side}")
        print(f"Type   : {args.type}")
        print(f"Qty    : {args.qty}")
        print(f"Price  : {args.price}")
        print(f"Stop   : {args.stop_price}")

        confirm = input("\nProceed with order? (y/n): ")

        if confirm.lower() != "y":
            print("❌ Order cancelled")
            return

        # ✅ API call
        client = BinanceClient(API_KEY, API_SECRET)
        response = client.place_order(params)

        # ✅ Output
        if response and "orderId" in response:
            print_success(response)
        else:
            print_error(response)

    except Exception as e:
        print(f"\n⚠️ ERROR: {str(e)}")


if __name__ == "__main__":
    main()