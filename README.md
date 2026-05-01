# Binance Futures Testnet Trading Bot

##  Overview

This project is a command-line (CLI) trading bot built in Python that interacts with the Binance Futures Testnet using REST APIs.
It enables users to place MARKET, LIMIT, and STOP orders while demonstrating clean architecture, input validation, and robust logging.

---

## Key Features

* Place **MARKET**, **LIMIT**, and **STOP (Stop-Limit)** orders
* Supports both **BUY** and **SELL** sides
* CLI interface using `argparse`
* Input validation with clear error messages
* Structured logging of requests, responses, and errors
* Modular architecture (API client, order logic, validation, logging)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Handles API communication
│   ├── orders.py          # Builds order parameters
│   ├── validators.py      # Input validation logic
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
```

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 30000
```

### STOP Order (Stop-Limit)

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP --qty 0.001 --price 30900 --stop_price 31000
```

---

## API Configuration

API credentials are loaded using environment variables.

Create a `.env` file in the project root:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
```

>  Note: `.env` is excluded from version control for security.

---

##  API Details

* Base URL: `https://testnet.binancefuture.com`
* API Type: REST (HMAC SHA256 signed requests)

---

##  Note on Testnet Access

In certain regions, accessing Binance Futures Testnet may redirect to KYC verification flows on the main Binance platform.

The application is fully implemented according to the Binance Futures Testnet API specification.
However, successful execution depends on access to valid testnet API credentials.

---

##  Logging

All activity is logged to:

```
bot.log
```

Logs include:

* API requests
* API responses
* Errors and exceptions

---

##  Assumptions

* The user has valid Binance Futures Testnet API credentials
* Internet connectivity is available
* Orders are executed in a simulated (testnet) environment

---

##  Conclusion

This project demonstrates a structured and modular approach to building a trading bot using REST APIs, with a focus on reliability, validation, and maintainability.
It reflects practical backend development skills applicable to real-world trading and financial systems.
