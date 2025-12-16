from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join("data", "metals.db")

@app.route("/")
def health():
    return jsonify({"status": "Gold & Silver API is running"})

@app.route("/prices", methods=["GET"])
def get_prices():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT metal, price, currency, updated_at
        FROM metal_prices
        ORDER BY updated_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    data = [
        {
            "metal": row[0],
            "price": row[1],
            "currency": row[2],
            "updated_at": row[3]
        }
        for row in rows
    ]

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
