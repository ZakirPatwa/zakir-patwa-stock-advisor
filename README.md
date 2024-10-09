# Stock Trading Advisor

## A fully functional Stock Trading Advisor using Open AI and GNews API, written in Python

Welcome to the Stock Trading Advisor, an AI application made to help users make decisions in
the stock market. This application is able to analyze real-time stock data and global trends by using
machine learning algorithms to provide the best personalized investment recommendations. The goal of
this unique application is to make the user’s job easier in the world of stock trading, whether they
are a beginner or an experienced trader.

## For Developers: Comments are included in the code explaining functions and chunks of code. These will help explain how the program works.

## For Users and Developers: To run the program, many packages are required. Packages include: 

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
import urllib.request

After importing the latest versions of the packages, you should be able to run the code without errors. 

After running the program, the browser will prompt you to enter in a stock. Any stock works. You may include
more than one stock at a time. The program will then take the stock data and generate news articles on the
stock. If you are running the news and pros and cons program, the program will display the pros and cons
of the given stock. If you are running the news and interactive graph program, the program will display
an interactive graph showing the stock data with candlestick patterns. This information could be useful
to make financial decisions based on the stock such as buying, selling, holding, long term, short term, etc.

## If you find a bug or a possible improvement to this project, please submit an issue in the issues tab above. Thank you!

