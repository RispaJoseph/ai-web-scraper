import time
from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser...")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)


    try:
        driver.get(website)
        print("Page loaded...")
        time.sleep(10)
        return driver.page_source
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.body
    return str(body) if body else ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript", "header", "footer"]):
        tag.extract()

    text = soup.get_text(separator="\n")

    cleaned = "\n".join(
        line.strip() for line in text.splitlines() if line.strip()
    )

    return cleaned


def split_dom_content(dom_content, max_length=1000):
    return [
        dom_content[i:i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]