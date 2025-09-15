from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Helper: connect to DB
def get_db_connection():
    conn = sqlite3.connect("ecomm.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return redirect("/products")

# Show product list
@app.route("/products")
def list_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("db_list.html", products=products)

# Add new product (Form GET + POST)
@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        conn = get_db_connection()
        conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()
        return redirect("/products")

    return render_template("add_db.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
