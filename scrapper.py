import requests
from bs4 import BeautifulSoup

url = input('Enter URL:')
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
raw_html = requests.get(url, headers=agent)
html = BeautifulSoup(raw_html.text, 'html.parser')
name = html.find_all("a", class_="ui large header left")
print("Name"+name[0].text)
rating = html.find_all("div", class_="rating-div")
print("Rating"+rating[0].text)
cost = html.find(text="two people (approx.)")
print(cost)
