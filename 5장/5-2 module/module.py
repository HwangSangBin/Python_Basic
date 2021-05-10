# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 File
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 file

import mod1
print(mod1.sub(5,1))
# import만 사용하여 모듈 불러오기
from mod1 import add
print(add(5,7))
# from과 import를 사용하여 모듈 사용 간결화
from mod1 import add, sub
# 두 모듈 가져오기, 무수히 많아지면 불편
from mod1 import *
# 모든 모듈 가져오기
print(add(3,1))
print(sub(6,5))


import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solve(2))
# 모듈 속에 있는 class 사용
