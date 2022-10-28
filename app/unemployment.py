import os
import json
from pprint import pprint
from statistics import mean

import requests
from dotenv import load_dotenv # <--- ADDITION

load_dotenv() # <--- ADDITION

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#pprint(parsed_response)


# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

#breakpoint()

latest = parsed_response["data"][0]
print(f"LATEST UNEMPLOYMENT RATE: {latest['value']}%, {latest['date']}")
print("----------------")



# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

unemployment_data = parsed_response["data"]

cy_rates = []

cy_data = [u for u in unemployment_data if "2022" in u["date"]]

for c in cy_data:
    cy_rates.append(float(c["value"]))


print (f"AVERAGE UNEMPLOYMENT RATE IN 2022: {mean(cy_rates)}%")
print("NO. OF MONTHS IN CALENDAR YEAR:", len(cy_rates))
