import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?query=%s&where=%s&start=%d'

page = 2
pageSize = page + 10 - 1;

if(page == 1):
    pageSize = 1

reqUrl = url%('python','post',pageSize)

print(reqUrl)

res = requests.get(reqUrl)

soup = BeautifulSoup(res.content,'lxml')
items = soup.select('ul#elThumbnailResultArea li.sh_blog_top')

for item in items:
    
    thumbItem = item.select('div.thumb img.sh_blog_thumbnail')
    titleItem = item.select('dl dt a.sh_blog_title')
    dateItem = item.select('dl dd.txt_inline')[0].text
    descItem = item.select('dl dd.sh_blog_passage')[0].text

    if(len(thumbItem)):
        print("1. Thumnail Src : ",thumbItem[0].get('src').strip())

    print("2. Title : ", titleItem[0].get('title').strip())
    print("   Title Link : ", titleItem[0].get('href').strip())
    print("3. Date : ", dateItem.strip())
    print("4. Desc : ",descItem.strip())

    print('')

#list
'''
tag : ul
id : elThumbnailResultArea
class : type01
    
    tag : li
    id : sp_blog_{n}
    class : sh_blog_top

    ul#elThumbnailResultArea li.sh_blog_top
'''

#info
'''
    tag : div
    class : thumb 

        tag : a

            tag : img
            class : sh_blog_thumbnail

    tag : dl
'''