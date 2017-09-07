import requests
from bs4 import BeautifulSoup
import smtplib  
from email.mime.text import MIMEText   
from email.header import Header  
import sys

from email import encoders


def spyder_neau(start_url,main_url = 'http://jwc.neau.edu.cn'):
    headers = {
        'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }
    
    start_html = requests.get(start_url, headers=headers)
    
    #---
    
    soup = BeautifulSoup(start_html.text, 'lxml')
    
    all_a = soup.find_all('a', class_='c60062')
    
    
    for a in all_a:
        title = a.get_text().replace(" ","").replace("\r","").replace("\n","")
        href = a['href']
        link = main_url + href
        #print(title)
        if title.find("智育")==-1:
            pass
        else:
            send_mail(link)

def send_mail(check_link):
    
    default_encoding = 'utf-8'  
    if sys.getdefaultencoding() != default_encoding:  
        reload(sys)  
        sys.setdefaultencoding(default_encoding)  
    link = check_link
    smtpHost = ''  
    smtpPort = ''  
    sslPort  = ''  
    fromMail = ''  
    toMail   = ''  
    username = ''  
    password = ''  
    
    subject  = u'智育成绩已出'  
    body     = u'点击查看 ' + check_link  
    
    encoding = 'utf-8'  
    mail = MIMEText(body.encode(encoding),'plain',encoding)  
    mail['Subject'] = Header(subject,encoding)  
    mail['From'] = fromMail  
    mail['To'] = toMail   
    
    try:  
        #纯粹的ssl加密方式，通信过程加密，邮件数据安全  
        smtp = smtplib.SMTP_SSL(smtpHost,sslPort)  
        smtp.ehlo()  
        smtp.login(username,password)  
        #发送邮件  
        smtp.sendmail(fromMail,toMail,mail.as_string())  
        smtp.close()  
        #print("OK")
    except Exception as e:  
        #print(e) 
        pass

    
url = 'http://jwc.neau.edu.cn/wejlist.jsp?a3t=20&a3p=1&a3c=3&urltype=tree.TreeTempUrl&wbtreeid=1888'
spyder_neau(url)

