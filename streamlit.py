import streamlit as st
from bot.core import MyTradingBot

st.set_page_config(page_title="MyTradingBot", layout="centered")
st.title("🚀 MyTradingBot - Binance Futures Testnet")

bot = MyTradingBot()

with st.form("order_form"):
    symbol = st.text_input("Trading Pair", value="BTCUSDT")
    side = st.selectbox("Order Side", ["BUY", "SELL"])
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001)

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = st.number_input("Price", min_value=0.01, step=0.1)
    if order_type == "STOP_LIMIT":
        stop_price = st.number_input("Stop Price", min_value=0.01, step=0.1)

    submit = st.form_submit_button("Place Order")

if submit:
    result = bot.place_order(
        symbol=symbol,
        side=side,
        quantity=quantity,
        order_type=order_type,
        price=price,
        stop_price=stop_price
    )

    st.subheader("📦 Order Response:")
    st.json(result)
