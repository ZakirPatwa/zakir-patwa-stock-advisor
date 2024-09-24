
import streamlit as st

from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from datetime import datetime
import asyncio
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import requests
import json
# This library will be used to fetch the API.
import urllib.request


st.set_page_config(page_title = "Dater", page_icon = "🌌️", layout = "wide", initial_sidebar_state = "expanded")
st.title("Dater 👁️‍🗨️️")

OPENAI_API_KEY = "Enter OPENAI Api Key"

class Dater:
    
    def __init__(self):
        self.llm = OpenAI(model_name = "gpt-4o", temperature = 0, streaming = True, api_key = OPENAI_API_KEY)
        self.tools = load_tools(["ddg-search"])
        self.agent = initialize_agent(self.tools, self.llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = False, handle_parsing_errors=True)

    async def get_stock_symbol(self, company_name):
        st_callback = StreamlitCallbackHandler(st.container())
        search_results = self.agent.run(company_name + " stock symbol(s). Return only the symbols separated by spaces. Don't add any type of punctuantion", callbacks = [st_callback])
        symbols = search_results.split(" ")
        return symbols

    async def get_stock_history(self, symbol, date):
        ticker = yf.Ticker(symbol)
        data = ticker.history(start = "2015-01-01", end = date)
        return data

    async def get_gnews_api(self):
        url = "https://gnews.io/api/v4/top-headlines?lang=en&token=<Enter GNews Api Key>"
        response = requests.get(url)
        news = response.json()
        return news 

    async def get_gnews_api_spec(self, search_term):
          
        apikey = "Enter GNews Api Key"
        search_term = "nvidia"
        url = f"https://gnews.io/api/v4/search?q={search_term}&lang=en&country=us&max=10&apikey={apikey}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            articles = data["articles"]
            return articles

        
        

    async def run(self):
        date_now = datetime.now()
        date_year = date_now.year
        date_month = date_now.month
        date_day = date_now.day
        date_day_ = date_now.strftime("%A")

        date_d = "{}-{}-{}".format(date_year, date_month, date_day)

        st.title(":blue[Welcome!:]")
        st.header("_Trading Bot App_")
        st.subheader(f" :green[_{date_d}_]")
        st.subheader(date_day_, divider = 'rainbow')

        company_name = st.text_input("Enter a company name:")

        if company_name:

            symbols = await self.get_stock_symbol(company_name)

            for symbol in symbols:

                
                left_column, right_column = st.columns(2)

                with left_column:
                    apikey = "Enter Gnews Api Key"
                    search_term = "nvidia"
                    url = f"https://gnews.io/api/v4/search?q={search_term}&lang=en&country=us&max=10&apikey={apikey}"

                    with urllib.request.urlopen(url) as response:
                        data = json.loads(response.read().decode("utf-8"))
                        articles = data["articles"]

                        for i in range(len(articles)):
                            #print(f"Title: {articles[i]['title']}")
                            #print(f"Description: {articles[i]['description']}")
                            st.write(f"**Title:** {articles[i]['title']}")
                            st.write(f"**Description:** {articles[i]['description']}")
                            st.write(f"**URL:** {articles[i]['url']}")
                            st.markdown("""---""")
       
                            break
                with right_column:
                    plot_placeholder = st.empty()

                st.markdown("""---""")

                df = await self.get_stock_history(symbol, date_d)

                data_date = df.index.to_numpy()
                data_open_price = df['Open'].to_numpy()
                data_high_price = df['High'].to_numpy()
                data_low_price = df['Low'].to_numpy()
                data_close_price = df['Close'].to_numpy()

                feg = go.Figure(data = [go.Candlestick(x = data_date, open = data_open_price, high = data_high_price, low = data_low_price, close = data_close_price)])
                feg.update_layout(title_text = "Full Data")
                feg.update_layout(xaxis_rangeslider_visible = False)

                plot_placeholder.plotly_chart(feg, use_container_width = True)
            

if __name__ == "__main__":
    dater = Dater()
    asyncio.run(dater.run())