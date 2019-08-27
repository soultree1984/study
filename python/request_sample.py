import requests as rq

#DOM 으로 파싱해주는 LIB
from bs4 import BeautifulSoup

res = rq.get('https://naver.com')
#print(res.content) #인코딩해서보여줌
#print(res.text) #원본보여줌
#print(res.status_code)

soup = BeautifulSoup(res.content,'lxml')
b = soup.select('li.au_item') # css selector

for item in b:
    print(item.text,item.get('class'))

a = soup.select('a')
for item in a:
    print(item.text,item.get('href'))