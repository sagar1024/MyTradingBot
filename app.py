import streamlit as st
from bot.core import MyTradingBot
from datetime import datetime

# Page Config
st.set_page_config(page_title="MyTradingBot", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .footer-text {
            position: fixed;
            bottom: 10px;
            left: 0;
            right: 0;
            text-align: center;
            font-size: 0.9rem;
            color: gray;
        }
        .main-title {
            text-align: center;
            font-size: 2.2rem;
            font-weight: 600;
            margin-top: 10px;
            margin-bottom: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom Header
st.markdown('<div class="main-title">MyTradingBot - Binance Futures Testnet</div>', unsafe_allow_html=True)

# Instantiate bot
bot = MyTradingBot()

# Initialize order type in session state
if "order_type" not in st.session_state:
    st.session_state.order_type = "MARKET"

# Select Order Type outside form (allows dynamic rerun)
order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_LIMIT"],
    index=["MARKET", "LIMIT", "STOP_LIMIT"].index(st.session_state.order_type),
    key="order_type",  # Will update session_state.order_type
)

# Main form
with st.form("order_form"):
    st.subheader("Place Order")

    symbol = st.text_input("Trading Pair", value="BTCUSDT")
    side = st.radio("Order Side", ["BUY", "SELL"], horizontal=True)
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001)

    price = None
    stop_price = None

    if st.session_state.order_type in ["LIMIT", "STOP_LIMIT"]:
        price = st.number_input("Limit Price", min_value=0.01, step=0.1)
    if st.session_state.order_type == "STOP_LIMIT":
        stop_price = st.number_input("Stop Price", min_value=0.01, step=0.1)

    submit = st.form_submit_button("Submit Order")

# Handle submission
if submit:
    st.info("Sending order to Binance Futures Testnet...")

    result = bot.place_order(
        symbol=symbol,
        side=side,
        quantity=quantity,
        order_type=st.session_state.order_type,
        price=price,
        stop_price=stop_price
    )

    if "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        st.success("Order submitted successfully.")
        st.subheader("Order Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Symbol:**", result.get("symbol", "N/A"))
            st.write("**Side:**", result.get("side", "N/A"))
            st.write("**Order Type:**", result.get("type", "N/A"))
            st.write("**Status:**", result.get("status", "N/A"))
            st.write("**Order ID:**", result.get("orderId", "N/A"))

        with col2:
            st.write("**Quantity:**", result.get("origQty", "N/A"))
            st.write("**Executed Quantity:**", result.get("executedQty", "N/A"))
            st.write("**Limit Price:**", result.get("price", "N/A"))
            st.write("**Stop Price:**", result.get("stopPrice", "N/A"))
            st.write("**Average Price:**", result.get("avgPrice", "N/A"))

        st.markdown("---")
        st.caption("Full raw response (for debugging):")
        st.json(result)

# Footer
st.markdown(
    f"""
    <div class="footer-text">
        © {datetime.now().year} MyTradingBot — For testing and demonstration purposes only.
    </div>
    """,
    unsafe_allow_html=True
)
