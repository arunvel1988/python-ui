from flask import Flask, request, g

app = Flask(__name__)


PRODUCTS = ["Laptop", "Phone", "Headphones"]

# ------------------------
# BEFORE REQUEST
# ------------------------
@app.before_request
def before_request():
    print(f"Incoming request: {request.method} {request.path}")
    # Example: set default cart in g
    g.cart = []

# ------------------------
# AFTER REQUEST
# ------------------------
@app.after_request
def after_request(response):
    print(f"Response status: {response.status}")
    # Example: add custom header to track version
    response.headers["X-Ecomm-Version"] = "1.0"
    return response

# ------------------------
# TEARDOWN REQUEST
# ------------------------
@app.teardown_request
def teardown_request(exception):
    if exception:
        print(f"Exception occurred: {exception}")
    else:
        print("Request finished, cleanup if needed")

# ------------------------
# ROUTES
# ------------------------
@app.route("/")
def home():
    return "Welcome to E-commerce Mall"

@app.route("/products")
def list_products():
    # Use g.cart for demonstration
    g.cart.append("Sample Product Added")
    return {"products": PRODUCTS, "cart": g.cart}

if __name__ == "__main__":
    app.run(port=5004, debug=True)
