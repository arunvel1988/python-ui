from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Running with python file.py"

if __name__ == "__main__":
    # Disable threaded mode + reloader to avoid Bad file descriptor
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=False, use_reloader=False)
