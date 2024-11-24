import requests
from bs4 import BeautifulSoup


url = "https://remoteok.com/remote-javascript-jobs"

res = requests.get(url, headers={
"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
})

#print(res.status_code)
#print(res.content)

all_jobs = []

keyword = [
    "java",
    "python",
    "golang"
]




for k in keyword:

    url = f"https://remoteok.com/remote-{k}-jobs"

    res = requests.get(url, headers={
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    })


    soup = BeautifulSoup(res.content, "html.parser")
    table = soup.find("table")
    jobs = table.find_all("td", class_="company")[1:]
    for job in jobs:
        #print(job)
        title = job.find("h2", itemprop="title").text
        region = job.find("div", class_="location").text
        company = job.find("h3", itemprop="name").text
        url = job.find("a").get("href")
        job_data = {
            "title":title,
            "company":company,
            "position":k,
            "region":region,
            "url":f"https://remoteok.com/{url}"
        }
        all_jobs.append(job_data)



print(all_jobs)


