from flask import Flask, jsonify, request

app = Flask(__name__)
PRODUCTS = []

@app.route("/api/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        return jsonify(PRODUCTS), 200

    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "invalid input"}), 400

    p = {"id": len(PRODUCTS) + 1, "name": data["name"], "price": data["price"]}
    PRODUCTS.append(p)
    return jsonify(p), 201

@app.route("/api/products/<int:pid>", methods=["GET", "PUT", "DELETE"])
def product_detail(pid):
    p = next((x for x in PRODUCTS if x["id"] == pid), None)
    if not p:
        return jsonify({"error": "not found"}), 404

    if request.method == "GET":
        return jsonify(p), 200
    if request.method == "PUT":
        data = request.get_json() or {}
        p["name"] = data.get("name", p["name"])
        p["price"] = data.get("price", p["price"])
        return jsonify(p), 200
    # DELETE
    PRODUCTS.remove(p)
    return jsonify({"message": "deleted"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004, debug=False)

