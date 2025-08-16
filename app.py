from flask import Flask, render_template, request, redirect, url_for, session
import os
import csv

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # change this to something secure

# ---------- CSV STORAGE ----------
if not os.path.exists("messages.csv"):
    with open("messages.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Message"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with open("messages.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        return "✅ Thanks! Your message has been saved."
    return render_template("contact.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "password123":
            session["admin"] = True
            return redirect(url_for("view_messages"))
        else:
            return "❌ Invalid credentials. Try again."
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))

# ---------- ADMIN PAGE ----------
@app.route("/admin/messages")
def view_messages():
    if not session.get("admin"):
        return redirect(url_for("login"))

    messages = []
    with open("messages.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(row)

    return render_template("messages.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
