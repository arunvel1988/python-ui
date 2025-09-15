from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    products = [
        {"id": 1, "name": "Socks", "price": 49},
        {"id": 2, "name": "T-shirt", "price": 299},
    ]
    return render_template("index.html", title="Ecomm Home", products=products)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
