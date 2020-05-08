import time
from fake_useragent import UserAgent
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random
import json
import re


options = Options()
options.add_argument("window-size=1400,600")

ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)

url = 'https://www.immoweb.be/en/search/house-and-apartment/for-rent/gent/9000?countries=BE&orderBy=relevance&page=1'


links = []
infos = []
page = 1
url = re.sub('page=\d', f'page={page}', url)

while True:
    
    print(f'Starting on page {url}')
    
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("li", {"class": "search-results__item"})

    for i, result in enumerate(results):
        try:
            links.append(result.find('a', {'class': 'card__title-link'})['href'])
        except TypeError:
            continue


    for link in links:
        print(f'Processing: {link}')
        driver.get(link)
        time.sleep(random.randint(3, 15))
        detail_html = driver.page_source
        detail_soup = BeautifulSoup(detail_html, 'html.parser')
        detail_results = detail_soup.find_all("tr", {"class": "classified-table__row"})
        info_dict = {'url': link}
        for detail in detail_results:
            try:
                info = detail.find('th').get_text().strip()
                info_data = detail.find('td').get_text().strip()
                info_data = re.sub(' +', ' ', info_data).replace('\n', '')
                info_dict[info] = info_data
            except AttributeError:
                continue
        infos.append(info_dict)
    
    if len(soup.find_all('a', {'class': 'pagination__link--next'})) > 0:
        page += 1
        links = []
        url = re.sub('page=\d', f'page={page}', url)
        with open('data_url.json', 'w+') as f:
            json.dump(infos, f)
    else:
        print('None found')
        break
