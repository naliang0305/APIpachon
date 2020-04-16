from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin #href裡的/f去解決重複的問題
import time

driver = webdriver.Chrome()
url = 'https://www.dcard.tw/f'
driver.get(url)

inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('tensorflow')

driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)

html = driver.page_source
soup = bs(html, 'html.parser') #html結構樹

data = soup.find_all('span',{'class':'sc-6oxm01-2 hiTIMq'})
meta_datas = []
for x in data:
    meta_datas.append(x.text.strip())
# print(meta_datas)

#從meta_data裡面挑出看板
forums = [] #看版
author = []
time = []
for i in range(len(meta_datas)):
    if i%3 == 0:
        forums.append(meta_datas[i])
    if i%3 == 1:
        author.append(meta_datas[i])
    if i%3 == 2:
        time.append(meta_datas[i])

data_2 = soup.find_all('h2',{'class': 'sc-1v1d5rx-3 eihOFJ'})
titles = []
for x in data_2:
    titles.append(x.text) #.text拿到文字
# print(titles)
data_3 = soup.find_all('a',{'class':'sc-1v1d5rx-4 gCVegi'})
hrefs =[]
for x in data_3:
    hrefs.append(x['href'])

#/f/==>相對連結
links = []
for href in hrefs:
    links.append(urljoin(url, href))
# print(links)

for i in range(len(forums)):
    if forums[i] == "軟體工程師":
        print(forums[i],titles[i], links[i])