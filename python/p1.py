#구구단
'''
2*1=2
2*2=2
...
5*5=25
5*6=30
...
9*8=72
9*9=81
'''

# 반복문 - 반복문 중첩
for i in range(2,9): # iterator : 반복자
    
    for j in range(1,9):
        print(i, '*' ,j , '=', i*j)
    print('end')
    print()