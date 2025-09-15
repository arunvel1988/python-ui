from flask import Flask
from products.routes import products_bp
from cart.routes import cart_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)

@app.route("/")
def home():
    return "Welcome to Arunvel’s E-commerce Mall 🏬"

if __name__ == "__main__":
    app.run(port=5001, debug=True)
