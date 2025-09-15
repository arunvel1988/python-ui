import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)


db_config = {
    "host": "your-rds-endpoint.rds.amazonaws.com",
    "user": "admin",
    "password": "yourpassword",
    "database": "ecommerce"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/rds/products", methods=["GET"])
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows), 200

@app.route("/rds/products", methods=["POST"])
def add_product():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (data["name"], data["price"]))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product added"}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5006, debug=True)
