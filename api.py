import os
import pymysql
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()
password = os.environ.get("DB_PASSWORD")

app = Flask(__name__)

def clean_rows(rows):
    for row in rows:
        row["price_usd"] = float(row["price_usd"])
        row["price_inr"] = float(row["price_inr"])
        row["change_24h_percent"] = float(row["change_24h_percent"])
    return rows


@app.route("/prices")
def prices():
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password=password,
        database="crypto_project",
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.coin, c.price_usd, c.price_inr, c.change_24h_percent, c.recorded_at
        FROM crypto_prices c
        JOIN (
            SELECT coin, MAX(recorded_at) AS latest
            FROM crypto_prices
            GROUP BY coin
        ) m
        ON c.coin = m.coin AND c.recorded_at = m.latest
    """)
    rows = cursor.fetchall()
    connection.close()
    return jsonify(clean_rows(rows))

if __name__ == "__main__":
    app.run()