import requests
from bs4 import BeautifulSoup
import time
start = time. time()

def scrapper(urls):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    try:
        raw_html = requests.get(url, headers=agent)
    except requests.exceptions.RequestException as e:
        return e
    html = BeautifulSoup(raw_html.text, 'html.parser')
    href = html.find_all('a')
    title = html.find('title')
    print(title.text)
    print(len(href))


url = input('Enter URL:')
scrapper(url)
end = time.time()
print(end - start)
