import os
from datetime import datetime
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from agno.agent import Agent
from agno.models.nebius import Nebius
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# -------------------------
# ENV
# -------------------------
load_dotenv()

# -------------------------
# AGENT
# -------------------------
agent = Agent(
    name="xAI Finance Agent",
    model=Nebius(
        id="meta-llama/Llama-3.3-70B-Instruct",
        api_key=os.getenv("NEBIUS_API_KEY"),
    ),
    tools=[DuckDuckGoTools(), YFinanceTools()],
    instructions=[
        "You MUST call the available tools to get real data.",
        "ALWAYS print numeric values in markdown tables.",
        "Include stock price, market cap, PE, PB, EPS, dividend yield, beta, "
        "52-week high and low.",
        "If comparing two stocks, output a side-by-side table."
    ],
    markdown=True,
)

OUTPUT_DIR = "reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -------------------------
# PRICE FETCH (DIRECT)
# -------------------------
def get_price_df(symbol: str):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")

    if df.empty:
        raise ValueError(f"No price data for {symbol}")

    df = df.reset_index()
    df = df[["Date", "Close", "Volume"]]
    df.columns = ["date", "close", "volume"]

    return df


# -------------------------
# GRAPHING
# -------------------------
def plot_comparison(symbols):
    plt.figure()

    for sym in symbols:
        df = get_price_df(sym)
        base = df["close"].iloc[0]
        normalized = df["close"] / base * 100
        plt.plot(df["date"], normalized, label=sym)

    plt.title("📈 1Y Normalized Performance Comparison")
    plt.ylabel("Growth Index (100 = start)")
    plt.xlabel("Date")
    plt.legend()

    path = os.path.join(OUTPUT_DIR, "comparison.png")
    plt.savefig(path)
    plt.close()
    return path


def plot_returns(symbol):
    df = get_price_df(symbol)
    df["returns"] = df["close"].pct_change()

    plt.figure()
    plt.plot(df["date"], df["returns"])
    plt.title(f"{symbol} — Daily Returns")

    path = os.path.join(OUTPUT_DIR, f"{symbol}_returns.png")
    plt.savefig(path)
    plt.close()
    return path


def plot_volume(symbol):
    df = get_price_df(symbol)

    plt.figure()
    plt.bar(df["date"], df["volume"])
    plt.title(f"{symbol} — Trading Volume")

    path = os.path.join(OUTPUT_DIR, f"{symbol}_volume.png")
    plt.savefig(path)
    plt.close()
    return path


# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="AI Finance Agent")

st.title("📊 AI Finance Agent Dashboard")

stocks = st.text_input(
    "Enter stocks (comma separated)",
    placeholder="AAPL,MSFT",
)

if st.button("Run Analysis") and stocks:

    with st.spinner("Running AI Agent..."):

        result = agent.run(
            f"Analyze and compare these stocks: {stocks}"
        )

        content = result.content if hasattr(result, "content") else str(result)

        st.markdown(content)

        symbols = [s.strip().upper() for s in stocks.replace("vs", ",").split(",")]

        if len(symbols) > 1:
            comp = plot_comparison(symbols)
            st.image(comp, caption="Normalized Performance")

        for sym in symbols:
            r = plot_returns(sym)
            st.image(r, caption=f"{sym} Daily Returns")

            v = plot_volume(sym)
            st.image(v, caption=f"{sym} Trading Volume")

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        md_path = os.path.join(OUTPUT_DIR, f"dashboard_{ts}.md")

        with open(md_path, "w") as f:
            f.write(content)

        st.success("Report saved!")
        st.code(md_path)
