import requests
import pymysql
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get("DB_PASSWORD")

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,inr&include_24hr_change=true")
data = response.json()

print(data)


connection = pymysql.connect(
     host="127.0.0.1",
    user="root",
    password=password,
    database="crypto_project"
)

cursor = connection.cursor()

now = datetime.now()

for coin, prices in data.items():
    cursor.execute(
        "INSERT INTO crypto_prices (coin, price_usd, price_inr, change_24h_percent, recorded_at) VALUES (%s, %s, %s, %s, %s)",
        (coin, prices["usd"], prices["inr"], prices["usd_24h_change"], now)
    )

connection.commit()
connection.close()

print ("Data inserted successfully!")

