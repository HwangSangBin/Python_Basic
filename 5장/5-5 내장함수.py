# 내장 함수
# Don't Reinvent The Wheel
# 이미 있는 것을 다시 만드느라 쓸데없이 시간을 낭비하지 말라

# abs
# 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수
print(abs(3))
print(abs(-3))

# all
# 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 T, 거짓이 하나라도 있으면 F를 돌려준다.
# 반복 가능한 자료형: for문으로 그 값을 출력할 수 있는 것: 리스트, 튜플, 문자열, 딕셔너리, 집합 등
print(all([1,2,3]))
print(all([1,2,3,0]))
# 0이 거짓

# any
# x 중 하나라도 참이 있으면 T, 모두가 거짓일 때만 F
# all의 반대느낌
print(any([1,2,3,0]))
print(any([0, ""]))

# chr 
# 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력
# 아스키 코드: 0~ 127사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것
print(chr(85))
print(chr(126))

# dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
# 예는 리스트와 딕셔너리 객체 관련 함수를 보여주는 예
print(dir([1,2,3]))
print(dir({"1": "a"}))

# divmod
# 2개의 숫자를 입력 받고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
print(divmod(7,3))
print(7//3) # 몫
print(7%3)  # 나머지

# enumerate
# 열거하다.
# 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
# for문과 자주 사용된다.
for i, name in enumerate(["s", "a", "n", "g"]):
    print(i, name)
# 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

# eval
# 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 돌려줌
print(eval("3+5"))
print(eval('"sang"+"bin"'))
print(eval("divmod(4,3)"))

# filter
# 무언가를 걸러낸다.
# 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형
# 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환값이 참인 것만 걸러서 돌려줌
def positive(x):
    return x> 0
print(list(filter(positive, [1,-3,2,5,-8])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5])))

# hex
# 정수값을 입력받아 16진수로 변환
print(hex(43))
print(hex(45723))

# id(object)
# 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 돌려주는 함수
a = 3
print(id(3))
print(id(a))

# input
# 사용자의 입력을 받는 함수

# int
# 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수

# isinstace(object, class)
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스
# 입력받은 인스턴스가 클래스의 인스턴스인지를 판단하여 T or F 판별
class Person: pass
a = Person
print(isinstance(a, Person))

# len
# 입력값의 길이(요소의 전체 개수)를 돌려주는 함수
print(len("python"))
print(len([1,2,3,4]))

# list
# 반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수
print(list("python"))
print(list((1,2,3)))

# map(f, iterable)
# 함수와 반복 가능한 자료형을 입력받음
# 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)
# =========================== 변화 ===============================
def three_times(x):
    return x*3
print(list(map(three_times, [1,2,3,4,5])))

# max
# 최댓값

# min
# 최솟값

# oct 
# 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
print(oct(34))

# open(filename, mode)
# 파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수

# ord
# 문자의 아스키 코드 값을 돌려주는 함수
print(ord("a"))

# pow(x, y)
# x의 y 제곱한 결괏값
print(pow(5,2))

# range(start, stop, distance)
# for문과 함께 자주 사용
# 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려줌
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,3)))

# round
# 반올림
print(round(4.6))

# sorted
# 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
print(sorted([3,1,2]))
print(sorted("zero"))

# str
# 문자열 형태로 변환

# sum
# 모든 요소의 합 더해줌

# tuple 
# 반복 가능한 자료형을 입력받아 튜플 형태로 변형
print(tuple("abc"))
print(tuple([1, 2, 3]))

# type
# 입력값의 자료형 알려줌

# zip
# 동일한 개수로 이루어진 자료형을 묶어주는 역할
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6,7,8,9],[10,11,12],[13,14,15])))