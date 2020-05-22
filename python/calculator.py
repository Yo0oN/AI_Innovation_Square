#!/usr/bin/env python
# coding: utf-8

# ## 모듈
# ### 함수, 변수 또는 클래스들을 모아두어 다른곳에서도 사용할 수 있게 모아둔 묶음 

# In[ ]:


def add (a, b) :
    print('add called!')
    return a + b

def divide (a, b) :
    print('divide called!')
    return a / b

def multiply (a, b) :
    print('multiply called!')
    return a * b

def sub (a, b) :
    print('sub called!')
    return a - b

# print('모듈')

if __name__ == '__main__' :
    ret = add(10, 20)
    print(ret)
    ret = subtract(10, 20)
    print(ret)
    print('나는 모듈입니다.', __name__)

