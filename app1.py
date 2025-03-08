# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 16:23:10 2025

@author: Hemal
"""

import streamlit as st
import yfinance as yf
import pandas as pd

st.title("DataCrest7")

ticker_symbol = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, MSFT)")

if st.button("Get Fundamentals"):
    if ticker_symbol:
        try:
            company = yf.Ticker(ticker_symbol)
            company_info = company.info

            company_fundamentals = {
                "Market Cap": company_info.get("marketCap"),
                "Beta": company_info.get("beta"),
                "PE Ratio": company_info.get("trailingPE"),
                "EPS": company_info.get("trailingEps"),
                "Dividend Yield": company_info.get("dividendYield"),
                "52 Week High": company_info.get("fiftyTwoWeekHigh"),
                "52 Week Low": company_info.get("fiftyTwoWeekLow"),
                "Average Volume": company_info.get("averageVolume"),
                "Profit Margin": company_info.get("profitMargins"),
                "Revenue": company_info.get("totalRevenue"),
                "Gross Profit": company_info.get("grossProfits"),
                "Operating Income": company_info.get("operatingIncome"),
                "Net Income": company_info.get("netIncome"),
                "Total Debt": company_info.get("totalDebt"),
                "Operating Cash Flow": company_info.get("operatingCashflow"),
                "Free Cash Flow": company_info.get("freeCashflow"),
                "Shares Outstanding": company_info.get("sharesOutstanding"),
                "Return on Assets": company_info.get("returnOnAssets"),
                "Return on Equity": company_info.get("returnOnEquity"),
                "Quick Ratio": company_info.get("quickRatio"),
                "Current Ratio": company_info.get("currentRatio"),
                "Total Cash": company_info.get("totalCash"),
                "Debt to Equity": company_info.get("debtToEquity"),
            }

            fundamentals_df = pd.DataFrame.from_dict(company_fundamentals, orient="index", columns=["Value"])
            fundamentals_df = fundamentals_df.dropna()
            
            st.subheader(f"Fundamentals of {company_info.get('shortName', ticker_symbol)}")
            st.table(fundamentals_df)
        
        except Exception as e:
            st.error(f"Error fetching data: {e}")
    else:
        st.warning("Please enter a valid ticker symbol.")
