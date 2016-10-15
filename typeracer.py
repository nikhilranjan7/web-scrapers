from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://play.typeracer.com/")
time.sleep(10)

sign_in = browser.find_element_by_link_text('Sign In')
sign_in.click()
username = browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr[2]/td/div/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input').send_keys('nikhilranjan7')
password = browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr[2]/td/div/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input').send_keys('//')
submit= browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr[2]/td/div/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button').click()

join = browser.find_element_by_link_text('Enter a typing race').click()

input_block = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')

final_part = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]/div/span[4]')
first_word = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]/div/span[2]')

text = first_word.text + ' ' + final_part.text
text = text.split(' ')

time.sleep(8)

for word in text[:-1]:
    input_block.send_keys(word)
    input_block.send_keys(' ')
