#!/usr/bin/env python
# coding: utf-8

# ## 모듈
# ### 함수, 변수 또는 클래스들을 모아두어 다른곳에서도 사용할 수 있게 모아둔 묶음 

# In[ ]:

class Calc :
    def __init__(self) :
        print('Calc 생성자 호출')
        self.a = 0
        self.b = 0
        self.c = 0
        
    def add (self, a, b) :
        print('add called!')
        self.a = a
        self.b = b
        self.c = self.a + self.b
        return self.c

    def divide (self, a, b) :
        print('divide called!')
        self.a = a
        self.b = b
        self.c = self.a / self.b
        return self.c

    def multiply (self, a, b) :
        print('multiply called!')
        self.a = a
        self.b = b
        self.c = self.a * self.b
        return self.c

    def sub (self, a, b) :
        print('sub called!')
        self.a = a
        self.b = b
        self.c = self.a - self.b
        return self.c

    # print('모듈')

if __name__ == '__main__' :
    m1 = Calc()
    
    ret = m1.add(10, 20)
    print(ret)
    
    ret = subtract(10, 20)
    print(ret)
    
    print('나는 모듈입니다.', __name__)

