from flask import Flask, render_template, request
#from extractors.indeed import

app = Flask("JobScraper")

@app.route("/")
def home():
    return render_template("home.html", name="namjun")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print(request.args)
    return render_template("search.html", name="namjun", keyword=keyword)


app.run("0.0.0.0", port="8999")