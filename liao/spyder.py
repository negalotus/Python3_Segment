import requests
from bs4 import BeautifulSoup


class catch_num(object):
    def all_url(self, url):
        main_url = 'https://www.liaoxuefeng.com'
        path = r'/home/ming/desktop/data.txt'
        title_list = []
        num_list = []
        #先抓起始页内目录的所有链接
        html = self.request(url)  #拿到网页
        soup = BeautifulSoup(html.text, 'lxml') #解析
        all_a = soup.find('div', class_='x-sidebar-left-content').find_all('a') #目录对应的文章链接，在<div class="x-sidebar-left-content">标签下的<a>标签内
        for a in all_a: #遍历目录对应文章链接
            title = a.get_text() #取目录标题
            href = a['href'] #取目录链接
            html_a = self.request(main_url + href) #相对地址补成绝对地址，抓每个链接内的阅读量
            html_soup = BeautifulSoup(html_a.text, 'lxml') #解析
            all_num = html_soup.find(
                'div', class_='x-wiki-info').find_all('span') #阅读量在<div class = 'x-wiki-info'>标签内下<span>标签内
            for num in all_num:
                title_list.append(title)
                num_list.append(int(num.get_text()[7:]))

        f = open(path, 'w+')
        f.write(str(title_list)+"\n")
        f.write(str(num_list))
        f.close()

    def request(self, url):
        headers = {
            'User-Agent':
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        }
        contents = requests.get(url, headers=headers)
        return contents
s
        


num = catch_num()
num.all_url(
    'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
)
