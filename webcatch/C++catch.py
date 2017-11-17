
import requests
from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页

html = urlopen('https://cis.temple.edu/~ingargio/cis71/code/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all('a')
a = 'http://www.cs.caltech.edu/~cs138/138a/examples/mergesort/'
for t2 in t1:
    t3 = t2.get('href')
    # print(t3)
    if t3[-4:] !='html' and t3 != a and t3[-3:] !='dat':
        print(t3)
        print("downloading with requests")
        url = 'https://cis.temple.edu/~ingargio/cis71/code/'+t3
        r = requests.get(url)
        with open("C:\\Users\\Administrator\\Desktop\\catch代码\\"+t3, "wb") as code:
            code.write(r.content)


