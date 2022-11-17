from ctypes.wintypes import tagRECT
import os
from typing import ItemsView
import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup


def get_soup(url):
    r= requests.get(url)
    if r.status_code==200:
        return BeautifulSoup(r.text,'html5lib')
    return None

    def get_products(soup):
        target=soup.find('div',class_='1YokD2_3Mn1Gg')
        if target is not None:
            items =target.find_all('div',class_='_1AtVbEcol-12-12')
            print(f'Found{len(items)}items')
            return items

def extract_one(item):
    data={}
    title =item.find('div',class_='_4rR01T')
    sell_price =items.find('div',class_='30jeq3_1_WHN1')
    orig_price =item.find('div',class_='_3I9_wc_27ucVY')
    rating =item.find('div',class_='_3LWZ1K')
    num_ratings =item.find('span',class_='_2_R_DZ')
    if title:
        data['title']=title.text.strip()
    if sell_price:
        data['sell_price']=sell_price.text.strip()
    if orig_price:
        data['orig_price']=orig_price.text.strip()
    if rating:
        data['rating']=rating.text.strip()
    if num_ratings:
        data['num_ratings']=num_ratings.text.strip()
        
    def main(query ='tv'):
        base_url ='https://www.flipkart.com/search'
        pos =1
    while True:
        url=f'{base_url}?q={query}&page={pos}'
        print(url)
        soup=get_soup(url)
    if soup is None:
        print('No data found')
    break

    items =get_products(soup)
    for item in items:
        data= extract_one(item)
        all_products.append(data)
        pos+=1
if len(all_products)>0:
    time=datetime.datetime.now().strftime("%Y%m%d_H%M%S")
    df =pd.DataFrame(all_products).tocsv(f'flipkart_{query}_{datetime.datetime.now().strftime'})

    if_name_=='_main_':
    main()

