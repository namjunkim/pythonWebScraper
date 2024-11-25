from flask import Flask, render_template

app = Flask("JobScraper")

@app.route("/")
def home():
    return render_template("home.html", name="namjun")

@app.route("/search")
def home():
    return render_template("home.html", name="namjun")


app.run("0.0.0.0", port="8999")