from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
PRODUCTS = []  # in-memory store (resets each run)

@app.route("/", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        if not name or not price:
            return "Missing name or price", 400
        PRODUCTS.append({"id": len(PRODUCTS) + 1, "name": name, "price": price})
        return redirect(url_for("list_products"))
    return render_template("add.html")

@app.route("/products")
def list_products():
    return render_template("list.html", products=PRODUCTS)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=False)
