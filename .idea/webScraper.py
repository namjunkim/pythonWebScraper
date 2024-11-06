import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)
#print(response.content)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
#print(jobs)

for job in jobs:
    title = job.find("span", class_="title").text
    #region = job.find("span", class_="region").text
    company, position, region = job.find_all("span", class_="company")
    company = company.text
    position = position.text
    region = region.text
    print(title, company, position, region)
    #print(title, "-----", region)

#a = [1,2,3,4,5,6,7,8,9]
#b =a[1]
#c = a[0:5] #start 0 to before 5
#d = a[1:]
#e = a[1:-1] #last element delete

#letters = ["a", "b", "c"]
#aa, bb, cc = letters
#aa<=a
#bb<=b
#cc<=c

