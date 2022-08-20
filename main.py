from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefox_Service
from selenium.webdriver.firefox.options import Options


class WorldExpeditions:
    BASE_SEARCH_URL = 'https://worldexpeditions.com/advanced-search'
    SEARCH_PARAM = 'searchFromDate=2022-08-30&searchToDate=2022-08-30&searchFromDateActual=2022-08-30&searchToDateActual=2022-08-30'

# op = Options()
# op.add_argument("--headless")
# driver = webdriver.Firefox(executable_path='geckodriver.exe', options=op)
# driver.get(WorldExpeditions.BASE_SEARCH_URL+'?searchKeywords=Bhutan')
# html = driver.page_source

with open('data/bhutan_search_result.html',) as f:
    soup = BeautifulSoup(f, 'html.parser')
teasers = soup.select('teaser')
results = []
for teaser in teasers:
    title = teaser.find('h3').text
    links = set()
    for link in teaser.find_all('a', href=True):
        links.add(link.attrs['href'])
    results.append((title, links))


