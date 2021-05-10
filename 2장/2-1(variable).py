# 변수(variable)
# 파이썬에서 변수 = 객체를 가리키는 것이라고 말할 수 있음

a = 1
b = "B"
c = [1, 2, 3]
# 변수 example
a = c
# a와 c 는 동일한 값이 됨
a = c[:]
c[1]  = 4
print(a)
# c 값이 바뀌더라도 a 값은 처음의 c 값과 같음
from copy import copy
a = copy(c)
# a = c[:] 와 같음
