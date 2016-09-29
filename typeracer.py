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
browser.get("http://play.typeracer.com/?rt=trgargoyle08")

input_block = browser.find_element_by_class_name('txtInput')

text = input('What\'s the text?\n').split(' ')

practice = browser.find_element_by_link_text('join race')
practice.click()

for word in text:
    input_block.send_keys(word)
    input_block.send_keys(' ')
