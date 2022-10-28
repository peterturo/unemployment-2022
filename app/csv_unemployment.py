import os
from pprint import pprint
from statistics import mean

from pandas import read_csv
from dotenv import load_dotenv # <--- ADDITION
import plotly.express as px

load_dotenv() # <--- ADDITION

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

unemployment_url_csv = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

unemployment_df = read_csv(unemployment_url_csv)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date? 
# Display the unemployment rate using a percent sign.

latest = unemployment_df.iloc[0]

print("LATEST UNEMPLOYMENT RATE:", f"{latest['value']}%,", latest['timestamp'])
print("----------------")