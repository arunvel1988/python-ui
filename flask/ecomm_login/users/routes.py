from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
    template_folder="templates"   # 👈 add this
)


USERS = {"arun": {"password": "123"}}

# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id


login_manager = LoginManager()
login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in USERS and USERS[username]["password"] == password:
            login_user(User(username))
            return redirect(url_for("users.profile"))
        return " Invalid credentials", 401
    return render_template("login.html")

@users_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out!"

@users_bp.route("/profile")
@login_required
def profile():
    return f"Welcome {current_user.id}, this is your profile!"
