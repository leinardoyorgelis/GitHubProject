import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=python+programming+language"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

search_results = soup.find_all('div', class_='r')
for result in search_results:
    print(result.text)
