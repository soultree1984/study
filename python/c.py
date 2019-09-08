# 틀
class C:
    def test1(self):
        print('hello1')

    def test2(self):
        print('hello2')

    def test3(self):
        print('hello3')

# 틀을 이용하여 생산
c1 = C()
c2 = C()
c3 = C()
c4 = C()
c5 = C()

# 사용
# .(마침표) 접근자
# a.b => a에 들어있는 b를 호출하세요.
c1.test1()
c2.test2()
c5.test3()

