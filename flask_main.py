from flask import Flask, render_template, request
from extract_job import extract_job

app = Flask("JobScraper")

db = {
}

@app.route("/")
def home():
    return render_template("home.html", name="namjun")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = extract_job(keyword)
        print(request.args)
        db[keyword] = jobs
    return render_template("search.html", name="namjun", keyword=keyword, jobs=jobs)


app.run("0.0.0.0", port="8999")