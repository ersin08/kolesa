import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

datefrom = '2015'

option = webdriver.ChromeOptions()
#option.add_argument('headless')
driver = webdriver.Chrome(options = option, service=Service(ChromeDriverManager().install()))

driver.get('https://kolesa.kz/')
driver.find_element("css selector", 'body > div.ui-container > div > nav > ul > li:nth-child(1) > span').click()
time.sleep(3)
driver.find_element("css selector", 'body > div.ui-container > div > section > div > form > div.main > div.primary > div.basic-settings > div.element-group.element-group-region.arrow-icon.element-type-region > div > div > div > div > div > ul > li:nth-child(1) > button > span').click()
driver.find_element("css selector", '#year\[from\]').send_keys(datefrom)
time.sleep(2)
driver.find_element("css selector",'body > div.ui-container > div > section > div > form > div.footer > div.primary > button > span').click()

elements1 = soup.find_all(attrs={"class":{"a-card__description"}}) #descrip
elements2 = soup.find_all(attrs={"class":{"a-card__param a-card__param--date"}}) #date
elements3 = soup.find_all(attrs={"class":{"a-card__param"}}) #city
elements4 = soup.find_all(attrs={"class":{"a-card__price"}}) #summ

summ = []
for i in range(len(elements4)):
    a = elements4[i].text
    a1 = "".join(j for j in a if  j.isdecimal())
    summ.append(a1)

description = []
for i in range(len(elements4)):
    d = elements1[i].text.strip()
    description.append(d)

date = []
for i in range(len(elements2)):
    d = elements2[i].text.strip()
    date.append(d)

city = []
for i in range(len(elements2)):
    c = elements3[i].text.replace("\n","").strip()
    if c.isalpha():
        city.append(c)

def data(elements, list):
    for i in range(len(elements)):
        d = elements[i].text.strip()
        list.append(d)

page = 2 #Задаем страницу и начинаем цикл
for page in range(10):
    html = f'https://kolesa.kz/cars/almaty/?year[from]=2015&page={page}'
    requiredHtml = requests.get(html)
    soup = BeautifulSoup(requiredHtml.text, 'html5lib')
    elements1 = soup.find_all(attrs={"class":{"a-card__description"}}) #descrip
    elements2 = soup.find_all(attrs={"class":{"a-card__param a-card__param--date"}}) #date
    elements3 = soup.find_all(attrs={"class":{"a-card__param"}}) #city
    elements4 = soup.find_all(attrs={"class":{"a-card__price"}}) #summ

    data(elements=elements1, list=description)
    data(elements=elements2, list=summ)

    for i in range(len(elements4)):
        a = elements4[i].text
        a1 = "".join(j for j in a if  j.isdecimal())
        if a1.isalnum():
            summ.append(a1)

    for j in range(len(elements3)):
        c = elements3[j].text.replace("\n","").strip()
        if c.isalpha()
            city.append(c)
    page +=1

df = pd.DataFrame(list(zip(city, date, description, summ)), \
columns = ['city', 'date', 'description', 'summ'])
df.to_csv('kolesa.csv', sep=';', encoding='utf-8', index=False)
print('df')

df = pd.DataFrame(list(zip(city, date, description, summ)), \
columns = ['city', 'date', 'description', 'summ'])
df.to_csv('kolesa.csv', sep=';', encoding='utf-8', index=False)