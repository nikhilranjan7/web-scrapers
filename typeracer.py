from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://play.typeracer.com/?rt=tf59qn1jxdm8")
time.sleep(10)

practice = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a')
practice.click()

input_block = browser.find_element_by_class_name('txtInput')

final_part = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]/div/span[4]')
first_word = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]/div/span[2]')

text = first_word.text + ' ' + final_part.text
text = text.split(' ')

time.sleep(8)

for word in text[:-1]:
    input_block.send_keys(word)
    input_block.send_keys(' ')
