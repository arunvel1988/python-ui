from flask import Flask
from users import users_bp, login_manager

app = Flask(__name__)
app.secret_key = "supersecret"  # needed for session handling

# Init Flask-Login
login_manager.init_app(app)

# Register blueprint
app.register_blueprint(users_bp)

@app.route("/")
def home():
    return "Welcome to the E-commerce Mall with Login"

if __name__ == "__main__":
    app.run(port=5002, debug=True)
