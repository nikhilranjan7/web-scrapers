from selenium import webdriver
import requests
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get("http://play.typeracer.com/")

practice = browser.find_element_by_link_text('Enter a typing race')
practice.click()

text = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]/div/span[2]")
