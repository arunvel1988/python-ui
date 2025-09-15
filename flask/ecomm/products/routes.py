from flask import Blueprint

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/")
def list_products():
    return "List of products (Mobiles, Laptops, etc.)"

@products_bp.route("/<int:product_id>")
def product_detail(product_id):
    return f"Product details for item {product_id}"
