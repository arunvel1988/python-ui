import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Load secret key from environment variable (fallback for dev)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "devsecret")

# Fake product DB (in real world → use RDS/Postgres/MySQL)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 100},
]

@app.route("/")
def home():
    return render_template("home.html", products=PRODUCTS)

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("view_cart"))

@app.route("/cart")
def view_cart():
    cart_items = [p for p in PRODUCTS if p["id"] in session.get("cart", [])]
    return render_template("cart.html", cart=cart_items)

if __name__ == "__main__":
    # Local dev only
    app.run(host="127.0.0.1", port=5000, debug=True)
