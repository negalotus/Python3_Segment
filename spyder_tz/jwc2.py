import requests
from bs4 import BeautifulSoup

def spyder_neau(start_url):
    headers = {
        'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }
    
    main_url = 'http://jwc.neau.edu.cn'
    
    #start_url = 'http://jwc.neau.edu.cn/wejlist.jsp?a3t=20&a3p=1&a3c=100&urltype=tree.TreeTempUrl&wbtreeid=1888'
    
    start_html = requests.get(start_url, headers=headers)
    
    #---
    
    soup = BeautifulSoup(start_html.text, 'lxml')
    
    all_a = soup.find_all('a', class_='c60062')
    
    
    for a in all_a:
        title = a.get_text().replace(" ","").replace("\r","").replace("\n","")
        href = a['href']
        link = main_url + href
        print(title, link)
        
spyder_neau('http://jwc.neau.edu.cn/wejlist.jsp?a3t=20&a3p=1&a3c=100&urltype=tree.TreeTempUrl&wbtreeid=1888')