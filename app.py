from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "my_secret_key"   # Change this to a random secret later


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return redirect(url_for("login"))


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        connection = sqlite3.connect("app.db")
        cursor = connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO auth_users(username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            connection.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))
            
        except sqlite3.IntegrityError:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        finally:
            connection.close()

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = sqlite3.connect("app.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM auth_users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        connection.close()

        if user:

            db_id, db_username, db_password = user

            if password == db_password:

                session["username"] = db_username

                return redirect(url_for("dashboard"))

            else:
                flash("Incorrect password!", "danger")
                return redirect(url_for("login"))

        else:
            flash("User not found!", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "username" in session:

        return f"""
        <h1>Dashboard</h1>

        <h2>Welcome {session['username']}</h2>

        <a href="/logout">Logout</a>
        """

    return redirect(url_for("login"))


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect(url_for("login"))


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True) 