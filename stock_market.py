import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title("Stock Market App")

st.write("Display Yahoo Finance data")

ticker_symbol = st.text_input("Enter the stock ticker symbol","AAPL")

ticker_data = yf.Ticker(ticker_symbol)
starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2022-01-01"))
ending_date = st.date_input("Enter the ending date", value=pd.to_datetime("today"))

hist = ticker_data.history(start=starting_date, end=ending_date)

st.write(hist)

# st.write("This plot is for volume of the Stock")
# st.line_chart(hist.Volume) # xaxis as the index and we provide yaxis

# st.write("This is the price of the stock market")
# st.line_chart(hist.Close)

# #column
# col1, col2, col3 = st.columns(3)

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

col1, col2 =st.columns(2)

with col1:
    st.header("This plot is for volume of the Stock")
    st.line_chart(hist.Volume)

with col2:
    st.header("This plot is for price of the stock market")
    st.line_chart(hist.Close)
