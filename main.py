from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefox_Service
from selenium.webdriver.firefox.options import Options


class WorldExpeditions:
    BASE_SEARCH_URL = 'https://worldexpeditions.com/advanced-search'
    SEARCH_PARAM = 'searchKeywords'

op = Options()
op.add_argument("--headless")
driver = webdriver.Firefox(executable_path='geckodriver.exe', options=op)
driver.get(WorldExpeditions.BASE_SEARCH_URL+'?searchKeywords=Bhutan')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.select('teaser'))