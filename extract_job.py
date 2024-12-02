
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
def extract_job(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #page.goto("https://google.com")

    #page.screenshot(path="screenshot.png")

    #browser = p.chromium.launch(headless=False) #chromium 대신 firefox, safari등 가능

    #page = browser.new_page() #새탭 열기


    page.goto("https://www.wanted.co.kr/")
    #page.goto("https://www.wanted.co.kr/search?query=flutter")

    #time.sleep(3)

    page.click("button.Aside_searchButton__rajGo")

    #time.sleep(5)

    page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)

    #time.sleep(5)

    page.keyboard.down("Enter")

    #time.sleep(5)

    page.click("a#search_tab_position")

    #time.sleep(2)

    #for x in range(5) :
    #    page.keyboard.down("End")
    time.sleep(1)

    content = page.content()

    soup = BeautifulSoup(content, "html.parser")

    p.stop()

    jobs = soup.find_all("div", "JobCard_content__jt_Jf")
    links = soup.find_all("div", "JobCard_container__REty8")

    jobs_db = []


    for job in jobs:
        #link = job.find("img")["src"]
        title = job.find("strong", class_="JobCard_title__HBpZf").contents
        company_name = job.find("span", class_="JobCard_companyName__N1YrF").contents
        job_data = {
            "title":title,
            "company":company_name,
            "url":"www.www"
        }
        jobs_db.append(job_data)

    return jobs_db