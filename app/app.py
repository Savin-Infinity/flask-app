from flask import Flask, render_template, redirect, url_for, request  # type: ignore

app = Flask(__name__)

gusername = ""
gpassword = ""


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == gusername and password == gpassword:
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        global gusername, gpassword
        gusername = username
        gpassword = password
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)