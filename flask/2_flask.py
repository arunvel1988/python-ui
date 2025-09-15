from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Home — Welcome to the tiny e-comm demo"

@app.route("/products")
def products():
    return "Products summary page"

@app.route("/product/<int:product_id>")
def product(product_id):
    return f"Product detail page for id={product_id}"

@app.route("/go-products")
def go_products():
    # demo of url_for (server-side link building)
    return f"Use this path to products: {url_for('products')}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
