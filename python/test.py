helloworld = "hello world" # 파이썬 주석
print(helloworld);
print(helloworld[0]);
print(helloworld[1]);
print(helloworld[-1]);

print(helloworld.replace('hello','welcome to'));

print("=======================================")

helloworld = '19,000원';

result1 = helloworld.find(','); 
result2 = helloworld.find('000'); # 해당 문자열의 시작 인덱스 값 리턴.
result3 = helloworld.find('?'); # 해당 문자열이 없으면 -1 리턴.

print(result1); 
print(result2); 
print(result3); 

print("=======================================")

price = '19000';
priceSum = price + price;
priceLength = len(price);
somenumber =  1

print(priceSum);
print(price * 3); # 숫자면 곱셈, 문자열이면 갯수만큼 합쳐진다.
print(priceLength);
print(int(price) * 3);
print(str(price));

print("=======================================")

msg = 'price: %s, somenumber : %d'%(price,somenumber); # formatting ( %s %d %f ) 
print(msg);

print("=======================================")

variable = [1,2,3,4,5,6,7,8,9];
print(variable);
#print(variable * 2);

variable.append(10);
print(variable);

variable.append(11);
print(variable);

variable.append(12);
print(variable);
print(len(variable))

print("=======================================")

variable = [1,2,3]
last = variable.pop()
print(last);
print(variable);

print("=======================================")
productsIds = [1,2,3];
none = productsIds.remove(1)
print(productsIds);


print("=======================================")
productsIds = [3,2,1,5,4,6,1,1,1];
productsIds.sort();
print(productsIds);

productsIds.reverse();
print(productsIds);

countCnt = productsIds.count(1) # 1이 몇개나 있는지?
print(countCnt)

extends = [7,8,9];
productsIds.extend(extends);
print(productsIds);

print("=======================================")
dict = [
        {'name':'name1','age':10},
        {'name':'name2','age':11},
        {'name':'name3','age':12},
        {'name':'name4','age':13},
        {'name':'name5','age':14},
        {'name':'name6','age':15}
       ];
print(dict);
print(dict[0]['name']);
print(dict[0]['age']);

dict = {'name':'name1','age':10};
print(dict);
print(dict['name']);
print(dict['age']);

print("=======================================")
dict = {'name':'name1','age':10};
print(dict.get('name'));
print(dict.get('size','M'));
print(dict.keys());
print(dict.values());
print(dict.items());
del dict['name'];
print(dict);
print(dict.clear());

dict.setdefault('size','M');
print(dict); # M
dict.setdefault('size','L'); # 없을떄 기본값으로 세팅하기 때문에 이미 위에서 세팅이 되서 L은 입력되지 않음.
print(dict); # M

print("=======================================")
productsIds = [1,1,1,1,1,2,3,4];
print(productsIds);
print(set(productsIds)); 
print(list(set(productsIds))); # dict to list

print("=======================================")

result = isinstance(10,int);
print(result)

result2 = isinstance(10,str);
print(result2)

result3 = isinstance('10',int);
print(result3)

result4 = isinstance('10',str);
print(result4)

print('1234'.isdigit());
print('1234오'.isdigit());

result5 = type(1);
result6 = type('1');
result7 = type(['1']);
result8 = type({'name':'name1','age':27});
result9 = type([{'name':'name1','age':27},{'name':'name2','age':28}]);

print(result5);
print(result6);
print(result7);
print(result8);
print(result9);

print("=======================================")

if 1 < 0 or 1 > 0:
    print("excute")
print("end")

print("=======================================")

if 1 < 0 or 1 < 0:
    print("excute")
print("end")

print("=======================================")
print(not (1 < 0) ) 

print("=======================================")

data = 'hello world';

for idx in range(0,100):
    print(idx,data);

print("=======================================")

data = [];
data.append({'name':'name1','age':27});
data.append({'name':'name2','age':28});
data.append({'name':'name3','age':29});    
data.append({'name':'name4','age':30});
data.append({'name':'name5','age':31});

for obj in data:
    print(obj);