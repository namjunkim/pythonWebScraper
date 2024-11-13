from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto("https://google.com")

page.screenshot(path="screenshot.png")


def plus(a, b):
    return a+b

print(plus(1,2))

print(plus(b=2, a=1))