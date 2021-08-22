from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import pandas as pd
def get_address(url):
    liss=[]
    driver = webdriver.Chrome()
    driver.get(url)
    #//div[@style="width:360px;"]
    time.sleep(0.1)
    many=driver.find_elements_by_xpath("//div[@style='width:360px;']")
    for one in many[1:]:
        liss.append(one.text)
    driver.close()
    return liss

url = "https://indiarailinfo.com/trains/special/15/"
driver = webdriver.Chrome()
driver.get(url)
flag=0
time.sleep(0.2)
driver.maximize_window()
time.sleep(0.1)
while(flag!=1):
    try:
        driver.find_element_by_class_name("nextbtn").click()
        time.sleep(random.randint(20,100)/10)
    except NoSuchElementException:
        flag = 1
        print("F")
# //*[@id="MainBody"]/div[3]/div[6]/div[2]/div[3]/div[2]
flag=0


data=['08477', 'Kalinga Utkal Festival Special (PT)', 'COVR', 'ECoR', 'Src/Dest Changed.', 'Jan 27', 'Jun 30', 'PURI', '20:45', 'YNRK', '21:50', '49h 5m', '62', 'S M T W T F S', '2S SL 3A 2A', '2389 km', '49 km/hr', '08478']
mat=[]
trains=driver.find_elements_by_xpath("//div[@style='line-height:20px;']")
for train in trains:
    lis=[train.find_element_by_xpath("./div[1]").text,train.find_element_by_xpath("./div[2]").text,train.find_element_by_xpath("./div[3]").text,train.find_element_by_xpath("./div[4]").text,train.find_element_by_xpath("./div[5]").text,train.find_element_by_xpath("./div[6]").text,train.find_element_by_xpath("./div[7]").text,train.find_element_by_xpath("./div[8]").text,train.find_element_by_xpath("./div[9]").text,train.find_element_by_xpath("./div[10]").text,train.find_element_by_xpath("./div[11]").text,train.find_element_by_xpath("./div[12]").text,train.find_element_by_xpath("./div[13]").text,train.find_element_by_xpath("./div[14]").text,train.find_element_by_xpath("./div[15]").text,train.find_element_by_xpath("./div[16]").text,train.find_element_by_xpath("./div[17]").text,train.find_element_by_xpath("./div[18]").text]
    C=train.find_element_by_xpath("./div[1]")           ##CLICK
    driver.execute_script("arguments[0].click();", C)
    time.sleep(2)
    info=driver.find_element_by_xpath("(//h2[text()='Rake/Coach Position'])[last()]")
    #(//h2[text()='Rake/Coach Position'])[4]

    coaches=info.find_elements_by_xpath("..//div[@class='num']")
    lis2=[]
    for coach in coaches:
        lis2.append(coach.text)
    lis.append(lis2)

    link=driver.find_elements_by_link_text("Time-Table")[-1]
    temp=link.get_attribute("href")
    lis2=get_address(temp)
    lis.append(lis2)
    print(temp)
    print(len(lis))
    print(lis)
    mat.append(lis)
    time.sleep(0.1)
df=pd.DataFrame(mat)
driver.close()
df.to_csv("Scraped.csv")


