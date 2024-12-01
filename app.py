import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the dataset
data = pd.read_csv("C:\\Users\\yashs\\Desktop\\WebDev\\TradeWhisper\\nifty_index_data.csv")
data['Date'] = pd.to_datetime(data['Price'])

# Streamlit Page Configuration
st.set_page_config(page_title="Nifty 50 Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Nifty 50 Stock Market Dashboard</h1>", unsafe_allow_html=True)

# First Row: Key Metrics
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Latest Close Price", f"₹{data['Close'].iloc[-1]:,.2f}")
with col2:
    st.metric("Highest Price", f"₹{data['High'].max():,.2f}")
with col3:
    st.metric("Lowest Price", f"₹{data['Low'].min():,.2f}")
with col4:
    st.metric("Total Volume", f"{data['Volume'].sum():,}")

# Second Row: Line Charts for Close Price and Volume
st.subheader("Stock Trends")
col5, col6 = st.columns(2)
with col5:
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close Price'))
    fig1.update_layout(title="Close Price Over Time", xaxis_title="Date", yaxis_title="Price", height=300)
    st.plotly_chart(fig1, use_container_width=True)
with col6:
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=data['Date'], y=data['Volume'], name='Volume'))
    fig2.update_layout(title="Volume Over Time", xaxis_title="Date", yaxis_title="Volume", height=300)
    st.plotly_chart(fig2, use_container_width=True)

# Third Row: Candlestick Chart
st.subheader("Candlestick Chart")
col7, col8 = st.columns([2, 1])
with col7:
    fig3 = go.Figure()
    fig3.add_trace(go.Candlestick(x=data['Date'],
                                  open=data['Open'], high=data['High'],
                                  low=data['Low'], close=data['Close'],
                                  name='Candlestick'))
    fig3.update_layout(title="Price Movements (Candlestick)", xaxis_title="Date", yaxis_title="Price", height=300)
    st.plotly_chart(fig3, use_container_width=True)

# Fourth Row: Data Insights Table
with col8:
    st.subheader("Recent Data Snapshot")
    st.dataframe(data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].tail(10), height=300)
