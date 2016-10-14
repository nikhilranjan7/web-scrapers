from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE_URL = "http://www.chicagoreader.com"

def get_category_link(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html.parser")
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

a=get_category_link("http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228")

for c in a:
    print(c)
