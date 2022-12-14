import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
from time import sleep

from mychrome import MyChrome

GOOGLE_NEWS_SEARCH_URL = "https://news.google.com/search"


# Google ニュースを検索
def search_in_google_news(keyword: str, outPath: str, headlessMode: bool = True):

    session = MyChrome(headlessMode).open_session()

    url = GOOGLE_NEWS_SEARCH_URL + '?q=' + keyword
    session.get(url)

    html = session.page_source.encode('utf-8')
    result_dict = _scrape_news_page(html, session)

    session.close()
    session.quit()

    if result_dict:
        export_dict_to_json(outPath, result_dict)

def _scrape_news_page(html: bytes, session: webdriver):
    print("ニュースページのスクレイピング")

    soup = BeautifulSoup(html, 'lxml')  # lxml はパーサ
    result_dict: dict = {}

    # 1記事の構成
    # <div jslog="識別子">
    #   <a href="記事のURL">
    #   <div class="xrnccd">
    #       ...
    #           <h3 class="ipQwMb ekueJc RD0gLb">
    #               <a href="./articles/CBMiSmh0dHBzOi8vbmV3cy55YWhvby5jby5qcC9hcnRpY2xlcy8yNWU3ODdhZDZmODg2OTlmMGRmOTZiYWY0ZTAzNGM1OTRlMmZkZGI10gEA?hl=ja&amp;gl=JP&amp;ceid=JP%3Aja" class="DY5T1d RZIKme">「iOS 16」でモバイルデータ使用を節約--オフにした方がよい4設定（ZDNet Japan） - Yahoo!ニュース</a>
    #           <h3 class="ipQwMb ekueJc RD0gLb">
    #               <a href="./articles/CAIiEGuAj6xdE1EiuL__EEW4PWEqGQgEKhAIACoHCAowl--JCzCtppwDMMWWowY?uo=CAUiJGh0dHBzOi8vamV0c3RyZWFtLmJ6L2FyY2hpdmVzLzE2MDA0NNIBAA&amp;hl=ja&amp;gl=JP&amp;ceid=JP%3Aja" class="DY5T1d RZIKme">iOS 16ダウンロード問題修正！iOS「Google TV」v3.4アップデート</a></h3>

    h3_list = soup.findAll('h3', class_='ipQwMb ekueJc RD0gLb')
    for h3 in h3_list:
        anchor = h3.find('a')
        # タイトル: URL
        result_dict[anchor.text] = get_anchor_url(session, anchor.text)

    return result_dict

def get_anchor_url(session: webdriver, anchor_text: str):

    # 対象要素
    element = session.find_element(By.LINK_TEXT, anchor_text)

    url = element.get_attribute('href')
    return url


def export_dict_to_json(path: str, result_dict: dict):
    print("[debug] export_to_json() dict:" +  str(result_dict) + ", path:" + path)

    json_file = open(path, mode="w", encoding='utf-8', )
    json.dump(result_dict, json_file, indent=2, ensure_ascii=False)
    json_file.close()


