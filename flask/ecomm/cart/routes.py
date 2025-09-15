from flask import Blueprint

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/")
def view_cart():
    return "Items in your cart"

@cart_bp.route("/checkout")
def checkout():
    return "Checkout page"
