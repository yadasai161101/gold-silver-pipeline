import os
import requests
import sqlite3
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOLD_API_KEY")
DB_PATH = "data/metals.db"

# Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

URLS = {
    "GOLD": "https://www.goldapi.io/api/XAU/USD",
    "SILVER": "https://www.goldapi.io/api/XAG/USD"
}

HEADERS = {
    "x-access-token": API_KEY
}

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metal_prices (
            metal TEXT,
            price REAL,
            currency TEXT,
            updated_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def fetch_and_store():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        for metal, url in URLS.items():
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            data = response.json()

            price = data["price"]
            currency = data["currency"]
            updated_at = datetime.utcnow().isoformat()

            cursor.execute("""
                INSERT INTO metal_prices (metal, price, currency, updated_at)
                VALUES (?, ?, ?, ?)
            """, (metal, price, currency, updated_at))

        conn.commit()
        print("Pipeline executed successfully")

    except Exception as e:
        logging.error(str(e))
        print("Pipeline failed")

    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    fetch_and_store()
