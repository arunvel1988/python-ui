from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# -----------------------------
# OOP Classes
# -----------------------------
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def apply_discount(self):
        return self.price   # default

class Electronics(Product):
    def apply_discount(self):
        return self.price * 0.9   # 10% discount

class Clothing(Product):
    def apply_discount(self):
        return self.price * 0.8   # 20% discount


class Customer:
    def __init__(self, username):
        self.username = username
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def checkout(self):
        total = sum([p.apply_discount() for p in self.cart])
        return total


# -----------------------------
# Demo Data
# -----------------------------
products = {
    1: Electronics(1, "Laptop", 60000),
    2: Clothing(2, "T-shirt", 1000),
    3: Electronics(3, "Smartphone", 30000),
}

customer1 = Customer("arun")

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    html = """
    <h1>Mini E-commerce Store</h1>
    <h2>Products</h2>
    <ul>
        {% for p in products.values() %}
            <li>
                {{p.name}} - Rs.{{p.price}} 
                (<a href="{{ url_for('add_to_cart', product_id=p.id) }}">Add to Cart</a>)
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('view_cart') }}">View Cart</a>
    """
    return render_template_string(html, products=products)


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    product = products.get(product_id)
    if product:
        customer1.add_to_cart(product)
    return redirect(url_for("view_cart"))


@app.route("/cart")
def view_cart():
    html = """
    <h1>{{ customer.username }}'s Cart</h1>
    <ul>
        {% for p in customer.cart %}
            <li>{{p.name}} - Final Price: Rs.{{p.apply_discount()}}</li>
        {% endfor %}
    </ul>
    <p><b>Total Payable:</b> Rs.{{customer.checkout()}}</p>
    <a href="{{ url_for('home') }}">Continue Shopping</a>
    """
    return render_template_string(html, customer=customer1)


# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
