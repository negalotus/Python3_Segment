import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

main_url = 'https://www.liaoxuefeng.com'

all_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'

start_html = requests.get(all_url, headers=headers)

#---

soup = BeautifulSoup(start_html.text, 'lxml')

all_a = soup.find('div', class_='x-sidebar-left-content').find_all('a')


for a in all_a:
    title = a.get_text()
    href = a['href']
    link = main_url + href
    html = requests.get(link, headers=headers)
    html_soup = BeautifulSoup(html.text, 'lxml')
    all_num = html_soup.find('div', class_='x-wiki-info').find_all('span')
    for num in all_num:
        f = open(r'/home/ming/desktop/data.txt','a+')
        f.write('%s %s\n'%(title,num.get_text()[7:]))
        f.close()
