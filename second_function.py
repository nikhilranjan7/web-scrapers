from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE_URL = "http://www.chicagoreader.com"

def get_category_link(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html.parser")
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.findall("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}

a=get_category_link("http://www.chicagoreader.com/chicago/best-chef/BestOf?oid=4088191")

for c in a:
    print(c)
