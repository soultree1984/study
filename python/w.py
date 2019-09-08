import requests as rq
import pprint 
import json

url='https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=comic&templateId=webtoon&pool=cbox3&lang=ko&country=KR&objectId=626907_267&categoryId=&pageSize=100&indexSize=10&groupId=&listType=OBJECT&pageType=default&page=1&refresh=false&sort=NEW&_=1567922441134'

headers={
    "Referer":"https://comic.naver.com/webtoon/detail.nhn?titleId=626907&no=267&weekday=wed",
    "Content-Type":"application/javascript"
}

res = rq.get(url,headers=headers)
result = str(res.text).replace("_callback(","").replace(");","")

convertedResult = json.loads(result)
commentList = convertedResult['result']['commentList']
#pprint.pprint(convertedResult)

for comment in commentList:
    contents = comment['contents']
    userName = comment['userName']
    print('%s: %s'%(userName,contents))
