from flask import Flask

app = Flask("JobScraper")

@app.route("/")
def home():
    return "hello flask"


app.run("0.0.0.0", port="8999")