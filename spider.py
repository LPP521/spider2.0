from bs4 import BeautifulSoup
import requests
from urllib import request
import re
from selenium import webdriver


def getImg(html):
    img_re=re.compile(r'(?<=src=")\S+?jpg')
    print("the type of html is :",type(html))
    img_list=img_re.findall(html)
    for i in range(len(img_list)):
        print("img_list[%d]=%s" % (i,img_list[i]))
        request.urlretrieve(img_list[i],'%s.jpg' % i)
        print("完成图片下载......")
        print("一共抓到了%d张图片" % len(img_list))
    req = request.Request(address, headers=headers)
    page = request.urlopen(req).read()
    r = page.decode('utf-8')
    result = []
    soup = BeautifulSoup(r, "html.parser")
    print(soup)

headers = {'User-Agent' : r'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)' }
address = "http://www.americanas.com.br"

def main(address,headers):
    driver = webdriver.Chrome()
    driver.get('www.creativecow.net')
    print(driver.title)
    driver.quit()




if __name__=='__main__':
    main(address,headers)