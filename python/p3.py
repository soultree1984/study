# list => 요소가 dict
# dict => 키값에 따라 다양한 데이터 타입을 가지고 있는 경우
data_set = [
  {
    "price": "20,000원",
    "title": "우아조리 데일리포인트 미니숄더백"
  }, {
    "price": "222,000원",
    "title": "하이엔드파이톤 더블섹션토트백"
  }, {
    "price": "126,000원",
    "title": "마일드크랙 스트랩조리버킷백"
  }, {
    "price": "157,000원",
    "title": "트리플스퀘어 하이엔드벨트백"
  }, {
    "price": "26,000원",
    "title": "심플매듭스트랩 사각플랩백"
  }, {
    "price": "15,000원",
    "title": "만능크로스 미니멀플랩백"
  }, {
    "price": "182,000원",
    "title": "모노톤스퀘어 하이엔드카프백"
  }, {
    "price": "190,000원",
    "title": "이브하프문 레더드롭백"
  }, {
    #"price": "83,000원",
    "title": "럭크 미니멀리 핸디토트백"
  }
]

# 동일한 데이터 타입의 연속적인 저장
'''
print(len(data_set))

for data in data_set:
    price = data.get('price','0원')
    title = data.get('title')
    print(price,title)
'''

dataset2={
    'comments':[1,2,3,4],
    'total':4,
    'date':'20190908'
}

comments = dataset2['comments']
total = dataset2['total']
date = dataset2['date']

print(type(comments),comments)
print(type(total),total)
print(type(date),date)

