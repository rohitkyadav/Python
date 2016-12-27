import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page < max_pages:
        url = "https://www.google.co.in/search?biw=1301&bih=683&q=hospitals&npsic=0&rflfq=1&rlha=0&tbm=lcl&tbs=lf:1,lf_ui:2&rlfi=hd:;si:&psj=1&psj=1#q=hospitals&tbs=lf:1,lf_ui:2&tbm=lcl&start=" + "page"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div', {'class': 'rlfl__tls rl_tls r-ivgXtrZBaNeU'}):
            href = "https://www.google.co.in" + link.get('href')
            title = link.string
            print("href")
            print("title")
        page += 1
trade_spider(10)       