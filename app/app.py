from flask import Flask, render_template, redirect, url_for, request # type: ignore
import sqlite3

app = Flask(__name__)


## Database connection ##
def get_db_connection():
    conn = sqlite3.connect("users.db")
    return conn


## Database initialization ##
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE  IF NOT EXISTS users (
        "id"	INTEGER,
        "username"	TEXT,
        "password"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)
    conn.commit()
    conn.close()

## Home route ##
@app.route("/")
def home():
    return render_template("home.html")


##Registration route ##
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")


##Login route ##
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()
        if user:
            return redirect(url_for("dashboard"))
    return render_template("login.html")


## Dashboard route##
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)