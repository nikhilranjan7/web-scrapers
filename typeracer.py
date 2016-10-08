from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
'''browser.get("http://play.typeracer.com/")

time.sleep(5)

practice = browser.find_element_by_link_text('Enter a typing race')
practice.click()

time.sleep(3)
'''
browser.get("http://play.typeracer.com/?rt=trnikhilranjan7")
time.sleep(10)

practice = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a')
practice.click()

text = input('What\'s the text?\n').split(' ')


input_block = browser.find_element_by_class_name('txtInput')

for word in text:
    input_block.send_keys(word)
    input_block.send_keys(' ')
