from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"  # used to encode/decode JWT


USERS = {"arun": "123"}

# -------------------
# LOGIN - Generate JWT
# -------------------
@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        # Token expires in 30 minutes
        token = jwt.encode(
            {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

# -------------------
# PROTECTED ROUTE - requires JWT
# -------------------
@app.route("/api/cart")
def api_cart():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        # Decode the token
        decoded = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        user = decoded["user"]
        return jsonify({"message": f"Hello {user}, your cart is empty!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

# -------------------
# RUN SERVER
# -------------------
if __name__ == "__main__":
    app.run(port=5003, debug=True)
