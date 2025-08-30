from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
import secrets

app = Flask(__name__)

# 🔑 Use a secure random secret key (protects sessions)
app.secret_key = secrets.token_hex(16)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Your login credentials
users = {"KendraDavis": "Kendra1234"}

@app.route("/")
def home():
    # Always show login page first
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials", 401
    return render_template("login.html")  # ✅ show login page

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    files = os.listdir(UPLOAD_FOLDER)
    return render_template("dashboard.html", user=session["user"], files=files)

@app.route("/agreements")
def agreements():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("agreements.html")

@app.route("/logout")
def logout():
    session.pop("user", None)  # ✅ remove only the user key
    return redirect(url_for("login"))  # ✅ back to login page

@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session or session["user"] != "KendraDavis":
        return "Unauthorized", 403

    if "agreement" not in request.files:
        return "No file uploaded", 400

    file = request.files["agreement"]
    if file.filename != "":
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return redirect(url_for("dashboard"))

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
