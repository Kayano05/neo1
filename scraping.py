import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'
}
for num in range(0,226,25):
    response = requests.get(f'https://movie.douban.com/top250?start={num}&filter=',headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    all_titles = soup.find_all('span',attrs={'class':'title'})
    for title in all_titles:
        title_strings = title.string
        if '/' not in title_strings:
            print(title_strings)