from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://passportindia.gov.in/AppOnlineProject/online/LocatePoliceStation")

states=[]
for i in range(2,37):
    state_unit = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/select/option[%s]"%str(i))
    state_unit = state_unit.text
    states.append(state_unit)

for i in range(0,34):
    districts=[]

    state = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/select")
    state.send_keys(states[i])
    state.send_keys(Keys.ENTER)
    time.sleep(3)
    no_districts=0
    try:
        for j in range(2,100):
            district_unit = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/select/option[%s]"%str(j))
            district_unit = district_unit.text
            districts.append(district_unit)
            no_districts = no_districts+1
    except:
        for k in range(0,no_districts):
            district = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/select")
            district.send_keys(districts[k])
            district.send_keys(Keys.ENTER)
            go = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[3]/td/input")
            go.click()
            no_stations=browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/form/div[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td/span[1]")
            no_stations=no_stations.text.split(' ')
            no_stations=no_stations[0]
            print(no_stations)
