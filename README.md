# MyTradingBot - Binance Futures Testnet

MyTradingBot is a lightweight cryptocurrency trading bot built for the **Binance Futures Testnet**, allowing you to place real-time test trades using a CLI interface or a Streamlit-based UI. It supports **MARKET**, **LIMIT**, and **STOP (stop-limit)** order types and is designed for testing and demonstrational purpose only.

---

## Features

- Place orders on Binance Futures Testnet
- Supports MARKET, LIMIT, and STOP (stop-limit) orders
- Two interfaces: Command Line Interface (CLI) and Streamlit Web App
- Simple modular codebase
- Live timestamp sync with Binance server
- Debug-friendly responses and structured logging

---

## Tech Stack

- Python 3
- Streamlit (for UI)
- Binance Futures Testnet API
- Requests (for HTTP)

---

## Project Setup

Follow these steps to set up **MyTradingBot** on your local machine:

---

### 1. Clone the Repository

```
bash
git clone https://github.com/your-username/MyTradingBot.git
cd MyTradingBot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```
bash
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows
```

### 3. Install Required Dependencies

```
bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a file named config.py in the project root directory:

```
python
API_KEY = "your_binance_testnet_api_key"
API_SECRET = "your_binance_testnet_api_secret"
BASE_URL = "https://testnet.binancefuture.com"
```

Make sure you generate keys from: https://testnet.binancefuture.com/en/futures/BTCUSDT → [API Management]

### 5. Run the Bot

CLI Mode

```
bash
python cli.py
```

Web UI (Streamlit)

```
bash
streamlit run streamlit_app.py
```

You're now ready to test trade on Binance Futures Testnet!

Developed by: SAGAR GURUNG
