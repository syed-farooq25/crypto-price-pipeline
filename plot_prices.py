import pymysql
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os


load_dotenv()
password = os.environ.get("DB_PASSWORD")

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password=password,
    database="crypto_project"
)

cursor = connection.cursor()
cursor.execute("SELECT coin, price_usd, recorded_at FROM crypto_prices ORDER BY recorded_at")
rows = cursor.fetchall()
connection.close()

bitcoin_times, bitcoin_prices = [], []
ethereum_times, ethereum_prices = [], []

for coin, price, time in rows:
    if coin == "bitcoin":
        bitcoin_times.append(time)
        bitcoin_prices.append(price)
    else:
        ethereum_times.append(time)
        ethereum_prices.append(price)

plt.plot(bitcoin_times, bitcoin_prices, marker="o", label="Bitcoin (USD)")
plt.plot(ethereum_times, ethereum_prices, marker="o", label="Ethereum (USD)")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.title("Crypto Price History")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("price_chart.png")
print("Chart saved as price_chart.png")