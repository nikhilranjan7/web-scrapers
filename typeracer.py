from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get("http://play.typeracer.com/")

time.sleep(5)

practice = browser.find_element_by_link_text('Enter a typing race')
practice.click()

time.sleep(3)

input_block = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')


text = input('What\'s the text?\n').split(' ')

for word in text:
    input_block.send_keys(word)
    input_block.send_keys(' ')
