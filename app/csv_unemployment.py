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



# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

# https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-criteria


csv_cy_data = unemployment_df[unemployment_df["timestamp"].str.contains("2022")]

print (f"AVERAGE UNEMPLOYMENT RATE IN 2022: {mean(csv_cy_data['value'])}%")
print("NO. OF MONTHS IN CALENDAR YEAR:", len(csv_cy_data))



# Challenge C
# 
# Plot a line chart of unemployment rates over time.

unemployment_csv = unemployment_df.to_dict("records")

for u in unemployment_csv:
    u["value"] = float(u["value"])

# help from https://www.geeksforgeeks.org/python-type-conversion-in-dictionary-values/


line_graph_csv = px.line(unemployment_csv, x="timestamp", y="value", 
               labels={
                        "timestamp": "Date","value": "Rate"
                        },
                     # axis labels help from https://plotly.com/python/figure-labels/
                    title="Unemployment Rates Over Time")

line_graph_csv.show()